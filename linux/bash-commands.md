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
