import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
CLI_SIMULATOR_FILE_PATH = os.path.join(ROOT_DIR, 'cde_cli', 'cde_cli_simulator.py')
CDE_API_USER_PASSWORD_ENV_VAR = "CDE_API_USER_PASSWORD"
