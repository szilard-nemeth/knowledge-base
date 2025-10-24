## Replace spaces with newlines (tr): 

```cat /proc/19368/environ | tr '\0' '\n'```

## Replace newline in variable
https://unix.stackexchange.com/questions/57124/remove-newline-from-unix-variable

`website=$(sed 's|/|\\/|g' <<< $website)`


Bash parameter expansion: https://unix.stackexchange.com/a/57128
```
dt=${dt//$'\n'/} # Remove all newlines.
dt=${dt%$'\n'}   # Remove a trailing newline.
```

## Replace text
https://stackoverflow.com/questions/6744006/can-i-use-sed-to-manipulate-a-variable-in-bash
Bash actually supports this sort of replacement natively:

```
${parameter/pattern/string} — replace the first match of pattern with string.
${parameter//pattern/string} — replace all matches of pattern with string.
```


## Grep for multiple patterns: 

```grep "<pattern1> \|<pattern2>" -A2 <inputfile>```

## Format timestamps (epoch): 

```for i in `ls -tr1 | sort | cut -d'.' -f1`; do echo $i.json `date -f "%s" -j $(($i / 1000 - 9*3600)) "+%Y%m%d-%H%M%S"`; done```


## Grep for something, in specific types of files
```grep -inR --include='*.yaml' "previousCDEVersion"```


## Grep in files with certain extensions
https://stackoverflow.com/questions/12516937/how-can-i-grep-recursively-but-only-in-files-with-certain-extensions

```
grep -inr --include \*.md --include \*.txt CP_Image /path/to/file
```



## Match and extract multiple parts of lines (e.g. two dates)
https://stackoverflow.com/questions/48458249/grep-show-two-parts-of-matching-line
Input: 
```
input=$(cat <<EOF 
2024-05-09T16:51:00.614251267Z Handling instance {"id":"dex-app-rcdg8cxr","clusterid":"cluster-2jz24l22","name":"qe-May08-r542","config":{"properties":{"dexapp.appTier":"tier-2","livy.ingress.enabled":"true","smtp.enabled":"false","spark.version":"3.3.0"},"chartValueOverrides":{"dex-app":{"safari.enabled":"false"}},"resources":{"cpu_requests":"20","mem_requests":"40Gi"},"accessControl":{"mechanism":"roles","roles":{"vc-full-access":{"users":["*"]}}},"defaults":{}},"appInfo":{"appInfoQuotaEnabled":true,"appInstanceUIStatus":{"Description":"Deleting","Status":"AppDeletionInitiated"},"cpuRequestActual":"27","createdVersion":"1.21.0-b422","creatorEmail":"dexssoadmin@cloudera.com","creatorID":"a57df75e-0485-4996-a3b1-1aee7e20efa8","creatorName":"dexssoadmin dexssoadmin","dedicatedFS":true,"dexApiUrl":"https://rcdg8cxr.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/dex/api/v1","dexUiUrl":"https://rcdg8cxr.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/dex/ui/","domain":"rcdg8cxr.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work","efsId":"fs-09b36becd5a1d5529","historyServerUrl":"https://rcdg8cxr.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/hs","livyServerUrl":"https://rcdg8cxr.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/livy","memRequestActual":"63Gi","roleProxyDefaultRole":"","roleProxyEnabled":false,"safariUrl":"https://rcdg8cxr.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/safari","sparkVersion":"3.3.0","version":"1.21.0-b422"},"status":"AppDeleted","created":"2024-05-08T16:27:57.172517Z","lastUpdated":"2024-05-08T16:50:49.878312Z","instanceLockStatus":"unlocked"}


2024-05-09T15:43:00.614360711Z Handling instance {"id":"dex-app-4rz6fhgs","clusterid":"cluster-2jz24l22","name":"qe-cross-vc-airflow-vc2","config":{"properties":{"dexapp.appTier":"tier-1","livy.ingress.enabled":"true","smtp.enabled":"false","spark.version":"3.3.0"},"chartValueOverrides":{"dex-app":{"safari.enabled":"false"}},"resources":{"cpu_requests":"20","mem_requests":"40Gi"},"accessControl":{"mechanism":"roles","roles":{"vc-full-access":{"users":["*"]}}},"defaults":{}},"appInfo":{"appInfoQuotaEnabled":true,"appInstanceUIStatus":{"Description":"Deleting","Status":"AppDeletionInitiated"},"cpuRequestActual":"27","createdVersion":"1.21.0-b422","creatorEmail":"dexssoadmin@cloudera.com","creatorID":"a57df75e-0485-4996-a3b1-1aee7e20efa8","creatorName":"dexssoadmin dexssoadmin","dedicatedFS":true,"dexApiUrl":"https://4rz6fhgs.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/dex/api/v1","dexUiUrl":"https://4rz6fhgs.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/dex/ui/","domain":"4rz6fhgs.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work","efsId":"fs-031704630ce79c224","historyServerUrl":"https://4rz6fhgs.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/hs","livyServerUrl":"https://4rz6fhgs.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/livy","memRequestActual":"63Gi","roleProxyDefaultRole":"","roleProxyEnabled":false,"safariUrl":"https://4rz6fhgs.cde-2jz24l22.dex-0th5.cyusea.b0.dev.cldr.work/safari","sparkVersion":"3.3.0","version":"1.21.0-b422"},"status":"AppDeleted","created":"2024-05-08T15:36:18.709377Z","lastUpdated":"2024-05-08T15:42:49.823022Z","instanceLockStatus":"unlocked"}
EOF
)
```

Extract dates from two parts of each line
```
echo $input | grep "Handling instance" | sed -E 's/(2024-05-09T[0-9:.Z]+).*(lastUpdated.*2024-05-.*Z",).*/\1 \2 /'
```


### Parse from alias
```
alias goto-dex-7712-clitesting | grep -o "=.*" | cut -d "'" -f2 | cut -d ' ' -f2
```

### Grep multiple exclude extensions
https://superuser.com/questions/509601/grep-multiple-exclude-extension

```
grep -r --exclude=\*.{html,htm,js} "li" *
```


### Grep multiple excludes
https://stackoverflow.com/questions/16212656/grep-exclude-multiple-strings
```
grep -Ev 'def|jkl' filename.txt
```


### Cut something by multiple whitespace

https://unix.stackexchange.com/questions/109835/how-do-i-use-cut-to-separate-by-multiple-whitespace
```
< file tr -s ' ' | cut -d ' ' -f 8
```


### Truncate long matching lines with grep
https://stackoverflow.com/questions/2034799/how-to-truncate-long-matching-lines-returned-by-grep-or-ack

```
grep -oE ".{0,10}mysearchstring.{0,10}" myfile.txt
```

Example full command: 
```
grep -oE ".{0,10}spark.driver.extraJavaOptions.{0,10}" ./DEX-7051/testing/20230612-system-testing/system-test-result-files-20230614/system-testing-log.txt\
```