# SSH

## Open a SSH tunnel: https://plenz.com/tunnel-everything.php

```ssh -NL 2345:127.0.0.1:8000 <user>@<host>```


# SCP
## Scp a file from a remote host

```scp snemeth@<HOST>:642171.tar.gz /Users/szilardnemeth/Downloads/```


## scp or sftp copy multiple files with single command
https://stackoverflow.com/questions/16886179/scp-or-sftp-copy-multiple-files-with-single-command 

`$ scp your_username@remote.edu:/some/remote/directory/\{a,b,c\} ./`


https://serverfault.com/questions/1105798/using-scp-to-copy-multiple-local-directories-to-a-server
