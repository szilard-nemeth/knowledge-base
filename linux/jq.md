# jq


## Complex example
https://chatgpt.com/c/67f45d7a-26a8-8007-868c-aa8aed44f2f2

### Sample JSON
```json
{
    "id": "urn:uuid:41528a53-d4f7-408e-a70b-a40b2c148370",
    "attr": {
      "cdeVersion": "1.25.0",
      "datalakeVersion": "7.1.9.1015",
      "osName": "redhat",
      "osVersion": "8.8",
      "runtimeArch": [
        "amd64",
        "arm64"
      ],
      "sparkVersion": "3.3.2.1.24.7191000.0-10",
      "spark2Version": "",
      "software": {
        "Iceberg": "1.3.0",
        "Java": "1.8.0.442.b06-2.el8",
        "Python": "3.6.8-51.el8",
        "Python2": "2.7.18-17.module+el8.10.0+20822+a15ec22d",
        "Scala": "2.12.15"
      }
    },
    "defaultRuntime": true,
    "gpuSupport": true,
    "images": {
      "LivyServer": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-livy-server-2.4.8-7.1.9.1015",
        "tag": "1.25.0-b78",
        "digest": "sha256:ea612f865e535406b057d9770a0b807f51caa8c429801ccb9dbdf3137ddbadc2"
      },
      "PythonBuilder": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-runtime-python-builder-7.1.9.1015",
        "tag": "1.25.0-b78",
        "digest": "sha256:59cd966608fb116f140e64f13185cc90f9eeb8502aad42d0ac0ef2a44bbf33e7"
      },
      "Spark": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-spark-runtime-gpu-3.3.2-7.1.9.1015-compat",
        "tag": "1.25.0-b78",
        "digest": "sha256:65d2348e5063b8a54afc0c907b4865dd48c77003c445106898f22a02fc424444"
      },
      "SparkHistoryServer": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-spark-history-server-2.4.8-7.1.9.1015",
        "tag": "1.25.0-b78",
        "digest": "sha256:43d001e6c55d360c77ab80fd49bc33f81425a9b0a21e63a1086ed41fbf78436c"
      },
      "SparkSession": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-livy-runtime-gpu-3.3.2-7.1.9.1015-compat",
        "tag": "1.25.0-b78",
        "digest": "sha256:dd8a3880de95a3b63c0bc13163326981bb4f1a045592913dd46fdcd66e95cac0"
      }
    }
  }
```

### Examples

Example entry in input JSON file: 
```json
{
    "id": "urn:uuid:3896da9b-3e7c-4502-bca5-b50729fd9691",
    "attr": {
      "cdeVersion": "1.24.1",
      "datalakeVersion": "7.2.18.800",
      "dlMinVersion": "7.2.18",
      "dlMaxVersion": "7.3.1",
      "osName": "redhat",
      "osVersion": "8.10",
      "runtimeArch": [
        "amd64",
        "arm64"
      ],
      "sparkVersion": "3.5.1",
      "spark2Version": "",
      "software": {
        "Iceberg": "1.5.2",
        "Java": "11",
        "Python": "3.8",
        "Python2": "2.7.18-17.module+el8.10.0+20822+a15ec22d",
        "Scala": "2.12.18"
      },
      "platformPC": true,
      "platformPVC": false
    },
    "defaultRuntime": false,
    "gpuSupport": false,
    "images": {
      "LivyServer": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-livy-server-3.5.1-7.2.18.800",
        "tag": "1.24.1-b86",
        "digest": "sha256:60b88cf5c5ea7b2ed650ba822aef97fdc7b3ce5a3a861b7cb0b960dc0bd219bd"
      },
      "PythonBuilder": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-runtime-python-builder-7.2.18.800-compat",
        "tag": "1.24.1-b86",
        "digest": "sha256:5e4e46158ad7bf69fa6a517afe795b3f4fcf7e81ed1179df020ed7003f91682c"
      },
      "Spark": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-spark-runtime-3.5.1-7.2.18.800-compat",
        "tag": "1.24.1-b86",
        "digest": "sha256:c1e49746f36cda58af88b38c8792634e5a584f5dd5dbbffe47db7a2d5f53e3d5"
      },
      "SparkHistoryServer": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-spark-history-server-3.5.1-7.2.18.800",
        "tag": "1.24.1-b86",
        "digest": "sha256:8a87e5a78e496784362f41653360df4e877c8b4ae5b7adc48d2ac29b5e3bbf8c"
      },
      "SparkSession": {
        "repo": "docker-private.infra.cloudera.com/cloudera/dex/dex-livy-runtime-3.5.1-7.2.18.800-compat",
        "tag": "1.24.1-b86",
        "digest": "sha256:2104b386a8b340158b22d474ba8015d722c80d8fec53affba1a00a220824e4f9"
      }
    }
  },
```


1. Get cdeVersion: `jq '.attr.cdeVersion' file.json`

2. Get the osName and osVersion: `jq '.attr.osName, .attr.osVersion' file.json`

3. Get the list of runtimeArch: `jq '.attr.runtimeArch[]' file.json`

4. If you want to extract multiple values at once in one command: `jq '{cdeVersion: .attr.cdeVersion, os: .attr.osName, osVersion: .attr.osVersion, java: .attr.software.Java}' file.json`


5. To extract id, cdeVersion, and datalakeVersion only when defaultRuntime is true, you can use the following jq command: 
```
jq 'select(.defaultRuntime == true) | {id, cdeVersion: .attr.cdeVersion, datalakeVersion: .attr.datalakeVersion}' file.json
```

Or if the JSON is an array of objects: 
```
jq '.[] | select(.defaultRuntime == true) | {id, cdeVersion: .attr.cdeVersion, datalakeVersion: .attr.datalakeVersion}' file.json
```

6. Include defaultRuntime as well: `jq '.[] | select(.defaultRuntime == true) | {id, cdeVersion: .attr.cdeVersion, datalakeVersion: .attr.datalakeVersion, defaultRuntime}' file.json`

Example output: 
```json
{
  "id": "id",
  "cdeVersion": "1.20.3-h1",
  "datalakeVersion": "7.2.15.8",
  "defaultRuntime": true
}
```

7. Sort results: 
```
jq '[.[] | select(.defaultRuntime == true) | {id, cdeVersion: .attr.cdeVersion, datalakeVersion: .attr.datalakeVersion, defaultRuntime}] | sort_by(.cdeVersion)' file.json
```

8. Sort by multiple fields: 
```
jq '[.[] 
  | select(.defaultRuntime == true) 
  | {id, cdeVersion: .attr.cdeVersion, datalakeVersion: .attr.datalakeVersion, defaultRuntime}
] 
| sort_by(.cdeVersion, .datalakeVersion)' file.json
```

9. Select multiple fields
https://stackoverflow.com/a/46530324/1106893

```
jq '[.[] 
  | select(.attr.cdeVersion == "1.24.0" and .attr.sparkVersion == "3.5.1")
  |{  id, 
      cdeVersion: .attr.cdeVersion, 
      datalakeVersion: .attr.datalakeVersion, 
      sparkVersion: .attr.sparkVersion,
      osName: .attr.osName, 
      defaultRuntime
    }
] 
| sort_by(.cdeVersion, .datalakeVersion)' /Users/snemeth/development/cloudera/cde/dex/pkg/control-plane/service/catalog-entries.json
```

10. Extract by nested property
```
jq '[.[] 
  | select(.images.Spark.repo | contains("7.2.18.800"))
  |{  id, 
      cdeVersion: .attr.cdeVersion, 
      datalakeVersion: .attr.datalakeVersion, 
      sparkVersion: .attr.sparkVersion,
      osName: .attr.osName, 
      defaultRuntime,
      sparkrepo: .images.Spark.repo
    }
] 
| sort_by(.cdeVersion, .datalakeVersion)' /Users/snemeth/development/cloudera/cde/dex/pkg/control-plane/service/catalog-entries.json
```


## Extract data based on multiple properties on key
https://chatgpt.com/c/6827c793-ad2c-8007-b56c-784bf8d0aa4b

Expression:
```
jq 'to_entries
    | map(select(
        .key | test("-runtime") or test("^dex-runtime-python-builder")
      ))
    | map(.value.images.dev.image_url)'
```

Source:
```
{
"dex-spark-runtime-2.4.7-7.1.7.3016": {
    "aqua_api_url": "https://aquasec.infra.company.com/api/v2/images/Ad%20Hoc%20Scans/docker-private.infra.company.com%2Fcloudera/dex/dex-spark-runtime-2.4.7-7.1.7.3016/1.24.0-b686/vulnerabilities",
    "aqua_ui_url": "https://aquasec.infra.company.com/#/images/Ad%20Hoc%20Scans/docker-private.infra.company.com%2Fcloudera%2Fdex%2Fdex-spark-runtime-2.4.7-7.1.7.3016:1.24.0-b686?digest=sha256:62fbed7e3af8b34a3f535ef376ff9b60364223209857187784dc13ad69077558",
    "architcture": [
      "amd64"
    ],
    "base_image_url": null,
    "image_category": "application",
    "image_name": "dex/dex-spark-runtime-2.4.7-7.1.7.3016:1.24.0-b686",
    "image_sha": "sha256:62fbed7e3af8b34a3f535ef376ff9b60364223209857187784dc13ad69077558",
    "image_size": "2Gi",
    "images": {
      "dev": {
        "image_url": "docker-private.infra.company.com/cloudera/dex/dex-spark-runtime-2.4.7-7.1.7.3016:1.24.0-b686"
      },
      "ecr": {
        "image_url": "866858832276.dkr.ecr.us-west-2.amazonaws.com/cloudera/dex/dex-spark-runtime-2.4.7-7.1.7.3016:1.24.0-b686"
      }
    },
    "product": "DEX"
  },
}
```


## Get keys of JSON file
https://stackoverflow.com/a/23118607/1106893

`jq 'keys_unsorted' file.json`


`jq 'keys' file.json`

Complete example: 
```shell
$ cat file.json
{ "Created-By" : "Apache Maven", "Build-Number" : "", "Archiver-Version" : "Plexus Archiver", "Build-Id" : "",  "Build-Tag" : "", "Built-By" : "cporter"}

$ jq 'keys_unsorted' file.json                                         
[
  "Created-By",
  "Build-Number",
  "Archiver-Version",
  "Build-Id",
  "Build-Tag",
  "Built-By"
]

$ jq 'keys' file.json
[
  "Archiver-Version",
  "Build-Id",
  "Build-Number",
  "Build-Tag",
  "Built-By",
  "Created-By"
]
```

## Extract nested data, store in array
```json
{
  "example": {
    "sub-example": [
      {
        "name": "123-345",
        "tag" : 100
      },
      {
        "name": "234-456",
        "tag" : 100
      },
      {
        "name": "4a7-a07a5",
        "tag" : 100
      }
    ]
  }
}
```

https://stackoverflow.com/a/39228718/1106893
If you just want to extract the name fields, the command you're looking for is jq `'.example."sub-example" | .[] | .name'`. If you want to keep the names in an array, wrap the whole jq expression in square brackets.


## Select attribute beginning with a string
`jq -r '.[]|select(.hostname | startswith("abcd"))' jjjj`