import errno
import io
import json
import logging
import os
import subprocess
from builtins import ValueError
from json import JSONDecodeError
from typing import List, Tuple, Callable

from definitions import CLI_SIMULATOR_FILE_PATH, CDE_API_USER_PASSWORD_ENV_VAR

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)


class CdeCliJsonParser:
    def __init__(self, cmd: List[str]):
        self.proc_handler = CdeCliJsonParser.create_default_for_cde_cli(cmd)

    @staticmethod
    def create_default_for_cde_cli(cmd: List[str]):
        if not os.getenv("%s" % CDE_API_USER_PASSWORD_ENV_VAR):
            raise ValueError("Please set environment variable: %s" % CDE_API_USER_PASSWORD_ENV_VAR)
        actions = [
            LineAction("WARN: Plaintext or insecure TLS connection requested", SubprocessHandler.send_input, ["yes"]),
            LineAction("API User Password:", SubprocessHandler.send_input, [os.getenv("%s" % CDE_API_USER_PASSWORD_ENV_VAR)])]
        ignore_output = ["cde job list "]

        # stdout.readline() and stdout.readlines() won't work with the output of cde cli.
        # These methods would block forever as cde cli wouldn't print a newline at the end of the line, apparently.
        # line = process.stdout.readlines().decode('utf-8')
        # line = process.stdout.readline().decode('utf-8')
        def looped_data_read_func(data):
            return data.startswith("[") and not data.endswith("]")

        return SubprocessHandler(cmd, ignore_output, actions,
                                 looped_data_read_func=looped_data_read_func)

    def run(self):
        self.proc_handler.run()

    def parse_job_names(self):
        self.proc_handler.run()
        if self.proc_handler.exit_code != 0:
            raise ValueError("Underlying process failed. "
                             "Command was: {} "
                             "stderr from process: {}".format(self.proc_handler.cmd, self.proc_handler.stderr))
        return self.get_jobs(filter_type="airflow")

    def get_jobs(self, filter_type=None):
        LOG.info("Decoding json: %s", self.proc_handler.stored_lines)
        json_str = "\n".join(self.proc_handler.stored_lines)
        try:
            parsed_json = json.loads(json_str)
        except JSONDecodeError as e:
            LOG.error("Invalid json output from cde cli process. output was: '%s'", json_str)
            raise e

        job_names = []
        for job in parsed_json:
            if filter_type:
                if job["type"] == filter_type:
                    job_names.append(job["name"])
            else:
                job_names.append(job["name"])
        return job_names


class LineAction:
    def __init__(self, line, action, args: List[str]):
        self.line = line
        self.action = action
        self.args = args

    def handle(self, handler, process, input_line):
        if input_line.startswith(self.line):
            self.action(handler, self, process, *self.args)
            return True

        return False

    def __str__(self):
        return "{}: line: {}, action: {}, args: {}".format(self.__class__, self.line, self.action, self.args)


class SubprocessHandler:
    def __init__(self, cmd: List[str],
                 ignore_output: List[str],
                 line_handlers: List[LineAction],
                 looped_data_read_func: Callable[[str], bool],
                 print_all=True):
        self.cmd = cmd
        self.ignore_out_lines = ignore_output
        self.line_actions = line_handlers
        self.looped_data_read_func = looped_data_read_func
        self.print_all = print_all
        self.stderr = None
        self.exit_code = None
        self.exited = False
        self.stored_lines = []

    def read_lines(self, process) -> List[str]:
        orig_exit_code = self.exit_code
        self.exit_code = process.poll()
        self.exited = orig_exit_code != self.exit_code
        data = process.stdout.read1().decode('utf-8')

        if self.exited and not data:
            return []

        if self.looped_data_read_func:
            if self.looped_data_read_func(data):
                all_data = data
                while process.poll() is None:
                    data = process.stdout.read1().decode('utf-8')
                    all_data += data
                return all_data.split("\n")

        if "\n" in data:
            lines = data.split("\n")
            return [l.strip() for l in lines]
        else:
            return [data.strip()]

    @staticmethod
    def send_input(handler, action, proc, *input):
        for i in input:
            try:
                if not i:
                    raise ValueError("Input was none. Line action: {}".format(action))
                encoded_line = i.encode('utf-8')
                proc.stdin.write(encoded_line)
                proc.stdin.write(b"\n")
                proc.stdin.flush()
            except IOError as e:
                if e.errno != errno.EPIPE and e.errno != errno.EINVAL:
                    raise

    def run(self):
        with subprocess.Popen(
                self.cmd,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
        ) as process:
            while True:
                lines = self.read_lines(process)
                for line in lines:
                    if self._check_for_ignores(line):
                        continue
                    if self._check_for_handlers(line, process):
                        continue

                    print(line)
                    # unhandled + not ignores --> store
                    self.stored_lines.append(line)

                if self.exited:
                    break

            if self.exit_code != 0:
                self.stderr = process.stderr.read1().decode('utf-8')

    def _check_for_handlers(self, line, process):
        handled = False
        for action in self.line_actions:
            if action.handle(self, process, line):
                handled = True
                break
        if handled:
            if self.print_all:
                print(line)
        return handled

    def _check_for_ignores(self, line):
        ignored = False
        for ignored_line in self.ignore_out_lines:
            if line.startswith(ignored_line):
                ignored = True
                break
        if ignored:
            if self.print_all:
                print(line)
        return ignored


if __name__ == '__main__':
    cmd = [
        "python",
        "-u",  # Unbuffered stdout and stderr
        CLI_SIMULATOR_FILE_PATH,
    ]
    parser = CdeCliJsonParser(cmd)
    print(parser.parse_job_names())
