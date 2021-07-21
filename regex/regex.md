1. get lines starting with NOT http and any other characters follows http

`^[^http.*].*`  

2. Match URL:

`http[s]*://[a-z0-9./_%&?=#~:()@\-]*`

3. Facebook image name pattern

`.*_[no]\.jpg$`
`.*_[no]\.png$`

4. 
`Hadoop YARN log test pattern: Replace `
WHAT: `^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}(.*)`
TO: `\1`