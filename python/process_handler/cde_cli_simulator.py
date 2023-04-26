TEST_OUTPUT = """
[
 {
    "name": "test-spark-1682437002-0244",
    "type": "spark",
    "created": "2023-04-25T15:40:18Z",
    "modified": "2023-04-25T15:40:18Z",
    "retentionPolicy": "keep_indefinitely",
    "mounts": [
      {
        "resourceName": "test_1682437002_0004"
      }
    ],
    "spark": {
      "file": "test-spark-1682437002-0244.py",
      "driverMemory": "1g",
      "driverCores": 1,
      "executorMemory": "1g",
      "executorCores": 1
    },
    "schedule": {
      "enabled": false,
      "user": "csso_snemeth"
    }
  },
  {
    "name": "test-spark-1682437002-0245",
    "type": "spark",
    "created": "2023-04-25T15:40:18Z",
    "modified": "2023-04-25T15:40:18Z",
    "retentionPolicy": "keep_indefinitely",
    "mounts": [
      {
        "resourceName": "test_1682437002_0000"
      }
    ],
    "spark": {
      "file": "test-spark-1682437002-0245.py",
      "driverMemory": "1g",
      "driverCores": 1,
      "executorMemory": "1g",
      "executorCores": 1
    },
    "schedule": {
      "enabled": false,
      "user": "csso_snemeth"
    }
  },
  {
    "name": "test-airflow-1682437002-0245",
    "type": "airflow",
    "created": "2023-04-25T15:40:18Z",
    "modified": "2023-04-25T15:40:18Z",
    "retentionPolicy": "keep_indefinitely",
    "mounts": [
      {
        "resourceName": "test_1682437002_0000"
      }
    ],
    "schedule": {
      "enabled": false,
      "user": "csso_snemeth"
    }
  }
  ]
"""

CORRECT_PASS = "pass"
print("cde job list --vcluster-endpoint https://d94tftqj.cde-64m2285t.dex-priv.xcu2-8y8x.dev.cldr.work/dex/api/v1")
print("WARN: Plaintext or insecure TLS connection requested, take care before continuing. Continue? yes/no [no]")
i = input()
if i != "yes":
    exit(1)

print("API User Password: ")
password = input()
if password != CORRECT_PASS:
    print("Password is incorrect. Exiting")
    exit(2)

print(TEST_OUTPUT)
exit(0)

