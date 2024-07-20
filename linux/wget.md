# WGET

Flags: 
```
-h: help of commands
-S: writes HTTP header out to the screen
-i: read URLs from file
-T: network timeout
--limit-rate=amount: Limits the download speed to amount bytes/second
  example: 
  --limit-rate=20k-->Limit set to 20 KB/s
  --limit-rate=10M-->limit set to 10MB/s
--spider: Spider mode: 
  Checks whether the resources are available or not
  Example: 
    Checking of bookmarks: wget --spider --force-html -i bookmarks.html
--force-directories; -x: Create the directory structure while retrieving content. 
--no-host-directories; -nH: Disable generation of host prefixed directories.
--directory-prefix=prefix;-P prefix: The target save directory.
--recursive;-r : The links to files that have been downloaded by Wget will be changed to refer to the file they point to as a relative link.Recursive retrieving
--level depth;-l depth : Specify recursion depth level.
--convert-links;-k : Convert links contained by downloaded files to provide offline viewing,
--page-requisites;-p : This option causes Wget to download all the files related to a page to display it correctly
-----------------------------
-A,  --accept=LIST               comma-separated list of accepted extensions.
-t,  --tries=NUMBER            set number of retries to NUMBER (0 unlimits).
       --retry-connrefused       retry even if connection is refused.  
–proxy=on: Turn on proxy.
[PREREQUISITE STEP: set environment proxy variable: export http_proxy="http://proxy.example.com:8080"]
```


## Download to different directory
DETAILS: https://unix.stackexchange.com/questions/23501/download-using-wget-to-a-different-directory-than-current-directory

```
wget -P /var/cache/foobar/ [...]
wget --directory-prefix=/var/cache/foobar/ [...]
```

## Examples

### Download webpage fully, convert links to relative links with proxy turned on
```
wget --proxy=on --mirror -p --html-extension --convert-links -P ~/_USEFUL_SAVED_WEBPAGES_FULL http://www.linuxcommand.org/index.php
```