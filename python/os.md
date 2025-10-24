# Python OS operations

## How do I list all files of a directory?
https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
This answer: https://stackoverflow.com/a/3207973

Only list files from directory: 
```
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
```


## Watch files for changes
https://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes

--> http://packages.python.org/watchdog/