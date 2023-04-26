import errno
import io
import json
import os
import subprocess
from builtins import ValueError
from typing import List, Tuple, Callable

"""
Some great examples are copied from here: https://realpython.com/python-subprocess/#communication-with-processes
"""


class CdeCliJsonParser:
    def __init__(self, cmd: List[str]):
        self.proc_handler = CdeCliJsonParser.create_default_for_cde_cli(cmd)

    @staticmethod
    def create_default_for_cde_cli(cmd: List[str]):
        if not os.getenv("CDE_API_USER_PASSWORD"):
            raise ValueError("Please set environment variable: CDE_API_USER_PASSWORD")
        actions = [
            LineAction("WARN: Plaintext or insecure TLS connection requested", SubprocessHandler.send_input, ["yes"]),
            LineAction("API User Password:", SubprocessHandler.send_input, [os.getenv("CDE_API_USER_PASSWORD")])]
        ignore_output = ["cde job list "]
        return SubprocessHandler(cmd, ignore_output, actions)

    def run(self):
        self.proc_handler.run()

    def parse_job_names(self):
        self.proc_handler.run()
        return self.get_jobs(filter_type="airflow")

    def get_jobs(self, filter_type=None):
        json_str = "\n".join(self.proc_handler.stored_lines)
        parsed_json = json.loads(json_str)

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
    def __init__(self, cmd: List[str], ignore_output: List[str], line_handlers: List[LineAction], print_all=True):
        self.cmd = cmd
        self.ignore_out_lines = ignore_output
        self.line_actions = line_handlers
        self.max_empty_lines_at_end = 5  # This is a hacky way to decide when input is over
        self.empty_lines_at_end = 0
        self.exit_code = None
        self.print_all = print_all
        self.stored_lines = []

    def read_lines(self, process) -> List[str]:
        orig_exit_code = self.exit_code
        self.exit_code = process.poll()
        exited = orig_exit_code != self.exit_code

        # This won't work with cde cli, needs more investigation
        # line = process.stdout.readlines().decode('utf-8')
        ret_lines = []
        data = process.stdout.read1().decode('utf-8')

        # HACK: Special case for json data :(
        if data.startswith("[") and not data.endswith("]"):
            # Assuming not all the json content has been read
            all_data = data
            while process.poll() is None:
                data = process.stdout.read1().decode('utf-8')
                all_data += data
            return all_data.split("\n")

        if "\n" in data:
            lines = data.split("\n")
            lines = [l.strip() for l in lines]
            ret_lines.extend(lines)
        else:
            ret_lines.append(data.strip())

        if self.exit_code is None and not exited:
            return ret_lines

        # Process exited
        while True:
            line = process.stdout.readline().decode('utf-8')
            if not line:
                self.empty_lines_at_end += 1
            else:
                ret_lines.append(line.strip())
            if self.empty_lines_at_end >= self.max_empty_lines_at_end:
                return ret_lines

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

                    # unhandled + not ignores --> store
                    print(line)
                    self.stored_lines.append(line)

                if self.exit_code is not None:
                    break

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
        "cde_cli_simulator.py",
    ]
    parser = CdeCliJsonParser(cmd)
    print(parser.parse_job_names())
