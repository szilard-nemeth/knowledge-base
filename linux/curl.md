# curl commands


## Save file to specific folder with curl command
https://stackoverflow.com/questions/16362402/save-file-to-specific-folder-with-curl-command

```
cd target/path && { curl -O URL ; cd -; }
```

or with subshell
```
(cd target/path && curl -O URL)
```

If you need to set filename explicitly, you can use small -o option:
```
curl -o target/path/filename URL
```