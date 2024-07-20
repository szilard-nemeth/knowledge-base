# Rsync commands

## Rsync manpage
https://www.manpagez.com/man/1/rsync/


## Rsync whole directory to remote machine:

```
rsync -a <dir> <user>@$<host>:
```


## Copying files using rsync from remote server to local machine
DETAILS: https://stackoverflow.com/questions/9090817/copying-files-using-rsync-from-remote-server-to-local-machine

From your local machine:
```
rsync -chavzP --stats user@remote.host:/path/to/copy /path/to/local/storage
```

From your local machine with a non standard ssh port:
```
rsync -chavzP -e "ssh -p $portNumber" user@remote.host:/path/to/copy /local/path
```

Or from the remote host, assuming you really want to work this way and your local machine is listening on SSH:
```
rsync -chavzP --stats /path/to/copy user@host.remoted.from:/path/to/local/storage
```