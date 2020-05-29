1. Change login shell

`chsh -s /bin/bash`

More info: https://www.computerhope.com/unix/chsh.htm

# Tricks

## Append string to each element of an array
https://stackoverflow.com/a/6426901
```
array=(a b c d e)
array=( "${array[@]/%/_content}" )
printf '%s\n' "${array[@]}"
```

## Get domain name from URL
`echo http://example.com/index.php | awk -F[/:] '{print $4}'`