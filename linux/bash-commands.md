## Bash commands

Change login shell

`chsh -s /bin/bash`

More info: https://www.computerhope.com/unix/chsh.htm

Loop through string variable, separated by comma
```
variable=abc,def,ghij
for i in ${variable//,/ }
do
    # call your procedure/other scripts here below
    echo "$i"
done
```

More info: https://stackoverflow.com/a/35894538/1106893
http://www.tldp.org/LDP/abs/html/string-manipulation.html


## Bash functions

Function to check status of command: 
```
function check_status_of_cmd {
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo "error with $1" >&2
    fi
    return $status
}
```

## Bash tricks

### Append string to each element of an array
https://stackoverflow.com/a/6426901
```
array=(a b c d e)
array=( "${array[@]/%/_content}" )
printf '%s\n' "${array[@]}"
```

### Get domain name from URL
`echo http://example.com/index.php | awk -F[/:] '{print $4}'`


### Get path and last dir of full path
https://superuser.com/a/443862
```
local lastdir=${file##*/}
local parentpath=${file%/*}
```

### Replace spaces with space + escape in paths
Example: `/Users/szilardnemeth/Library/Application Support/Google/Chrome//Profile 1/History`
``` 
echo $file | sed 's/ /\\ /g'
```
Reverse operation:
```
local profile=$(basename "${parentpath}" | tr -d "\\" | tr -d " ") 
```

### Parse comma-separated string into an array
```
string="some,comma,separated,text"
IFS=', ' read -r -a array <<< "$string"

echo ${array[0]}
echo ${array[1]}
echo ${array[@]}
```



### Argument parsing example
```
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
  -v|--version)
  DEX_IMAGE_TAG="$2"
  shift # past argument
  shift # past value
  ;;

  -h|--help)
  shift # past argument
  help
  exit 0
  ;;

  -f|--fullstack)
  FULLSTACK=true
  shift # past argument
  ;;

  -cl|--custom-liftie)
  CUSTOM_LIFTIE=true
  shift # past argument
  ;;

  -t|--tag)
  WORKLOAD_IMAGE_TAG="$2"
  shift
  shift
  ;;

  --ttl)
  TTL="$2"
  shift
  shift
  ;;

  -sb|--skip-build)
  SKIP_BUILD=true
  shift
  ;;


  *)
  invalid_arg $1
  exit 1
  ;;
esac
done
```


### Run a particular function from a shell script
https://stackoverflow.com/questions/8818119/how-can-i-run-a-function-from-a-script-in-command-line


Answer: https://stackoverflow.com/a/16159057/1106893
```
# Check if the function exists (bash specific)
if declare -f "$1" > /dev/null
then
  # call arguments verbatim
  "$@"
else
  # Show a helpful error
  echo "'$1' is not a known function name" >&2
  exit 1
fi
```
