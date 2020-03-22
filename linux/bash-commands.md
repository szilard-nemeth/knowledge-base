1. Change login shell

`chsh -s /bin/bash`

More info: https://www.computerhope.com/unix/chsh.htm

2. Loop through string variable, separated by comma
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