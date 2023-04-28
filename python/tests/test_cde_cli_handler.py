import json
import unittest

import os
from json import JSONDecodeError

from cde_cli.cde_cli_processor import CdeCliJsonParser
from definitions import ROOT_DIR, CLI_SIMULATOR_FILE_PATH, RESOURCES_DIR


class Test(unittest.TestCase):
    def setUp(self):
        os.environ["CDE_API_USER_PASSWORD"] = "pass"

    def tearDown(self) -> None:
        #self.tmp_file.remove()
        pass

    def _verify_job_names_starting_with_prefix(self, job_names, prefix):
        good_names = True
        for job in job_names:
            if not job.startswith(prefix):
                good_names = False
                break
        self.assertEqual(True, good_names)

    def _generate_script(self, statements):
        import tempfile, shutil
        self.tmp_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)

        with open(self.tmp_file.name, 'w') as f:
            for s in statements:
                if s == "":
                    f.write("\n")
                else:
                    f.write(s)

        print("Generated file: " + self.tmp_file.name)
        self.tmp_file.close()

    @staticmethod
    def _create_parser(script):
        cmd = [
            "python",
            "-u",  # Unbuffered stdout and stderr
            script,
        ]
        parser = CdeCliJsonParser(cmd)
        return parser

    def _assert_json_objs_equal(self, raw_file_input, json_str: str):
        json_obj_raw_file = json.loads(raw_file_input)
        json_obj_str = json.loads(json_str)
        self.assertEqual(json_obj_str, json_obj_raw_file)

    def test_cde_cli_handler_e2e_usage_with_simulator(self):
            parser = self._create_parser(CLI_SIMULATOR_FILE_PATH)
            job_names = parser.parse_job_names()

            some_random_expected_job_names = ["test-basic-dag-1682476744-0247",
                                              "test-basic-dag-1682476744-0201",
                                              "test-basic-dag-1682476744-0148",
                                              "test-basic-dag-1682476744-0219",
                                              "test-basic-dag-1682476744-0000"]

            all_found = all(job in job_names for job in some_random_expected_job_names)
            self.assertEqual(all_found, True)
            self._verify_job_names_starting_with_prefix(job_names, prefix="test-basic-dag")


            file_path = os.path.join(RESOURCES_DIR, "job-list-250dag.json")
            with open(file_path) as f:
                data = f.read()

            self._assert_json_objs_equal(data, "\n".join(parser.proc_handler.stored_lines))

    def test_cde_cli_handler_script_with_error(self):
        self._generate_script("import bla")
        parser = self._create_parser(self.tmp_file.name)

        with self.assertRaises(Exception) as context:
            parser.parse_job_names()

        # Underlying process failed. stderr from process: Traceback (most recent call last):
        #   File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
        #   File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
        # ModuleNotFoundError: No module named 'bla'
        self.assertIn('Underlying process failed. Command was', str(context.exception))
        self.assertTrue("ModuleNotFoundError: No module named 'bla'" in str(context.exception))

    def test_cde_cli_handler_script_with_error2(self):
        self._generate_script("")
        parser = self._create_parser(self.tmp_file.name)

        with self.assertRaises(Exception) as context:
            parser.parse_job_names()

        self.assertEqual(JSONDecodeError, type(context.exception))

    def test_cde_cli_handler_script_line_without_newline(self):
        self._generate_script("print('blabla', end='')")
        parser = self._create_parser(self.tmp_file.name)

        with self.assertRaises(Exception) as context:
            parser.parse_job_names()

        self.assertEqual(JSONDecodeError, type(context.exception))

    def test_cde_cli_handler_print_line_and_wait_for_input(self):
        script_lines = ["print(\"WARN: Plaintext or insecure TLS connection requested, take care before continuing. Continue? yes/no [no]\", end='')",
                        "",
                        "i = input()"]
        self._generate_script(script_lines)
        parser = self._create_parser(self.tmp_file.name)
        with self.assertRaises(Exception) as context:
            parser.parse_job_names()

        self.assertEqual(JSONDecodeError, type(context.exception))