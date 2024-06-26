File operations (find / ls)
===========================
1. Extract files from jar file to console, print with separator

```find . -iname "*<somename>.jar" -exec sh -c "echo file: {}; unzip -p {} META-INF/services/javax.ws.rs.ext.MessageBodyWriter; echo '$\n\n'" \;```

2. List recursive, show depth: 

```ls /export/apps -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'```


3. Remove multiple files: 

```find . -iname *versionsBackup -print0 | xargs -0 rm```

4. Find for specific file types, grep in them:

```find / -regex ".*\.\(xml\|txt\|ini\|cfg\)" 2>/dev/null | xargs grep <string>```

5. Find multiple files, with exclusion of filenames:

```find /opt/hadoop/share/hadoop/yarn/ -iname 'hadoop-yarn-server*nodemanager*' ! -iname "*test*.jar" ! -iname "*sources*jar" -printf "unzip -c %p | grep -q '' && echo %p\n" | sh```

6. Find and do something with results:
```
find . -type d -name venv -print0 | xargs -0 <command>
```

7. Cat a file, then invoke xargs per line:
Related SO answer: https://stackoverflow.com/a/65708689/1106893
```
cat ~/Downloads/tmp | xargs -n1 -I{} md5 {}
```

Example: 
```
find . -type d -name venv -print0 | xargs -0 -I % find % -type d | grep ".*pythoncommons\|python_commons.*"
```

7. Find + xargs, use special replacement character
```
find . -type d -name venv -print0 | xargs -0 -I % sh -c 'find % -type d'
```

Compression commands
===========================
1. Compress a folder with tar

```tar czf <dest>.tar.gz <file or dir>```

2. Untar

```tar xzvf example.tar.gz```


Jar commands
============

1. Extract specific file from jar file:

```jar xf <jarfile> META-INF/services/javax.ws.rs.ext.MessageBodyWriter```

2. List filenames of jar file: 

```unzip -Z1 <jarfile> | less | grep "about"```

3. List files in jar file: 

```jar tf <jarfile>```

4. unzip a file from jar file: 

```unzip -p <jarfile> org/apache/hadoop/yarn/api/protocolrecords/ResourceTypes.class```

5. List and grep for files in jars: 

Finding ObjectMapper.class in all jars found from service-dep.tar.gz
```for i in `find ~/Downloads/service-dep -iname "*jar"`; do [[ `unzip -Z1 $i | grep ObjectMapper\.class | wc -l` -gt 0 ]] && echo $i; done```

Networking commands 
===================

1. Restart network manager:

```sudo service network-manager restart``` OR

```sudo service networking restart``` OR

```sudo /etc/init.d/network restart```

2. Bring wlan interface down & up:

```
ifconfig wlan0 down
ifconfig wlan0 up
```

3. Ask for new IP (new DHCP lease): 

```sudo dhclient -v wlan0```


Linux version commands 
======================
Find out linux version (method 1):

```cat /etc/*-release```

Find out linux version (method 2):

```lsb_release -a```

Find out linux version (method 3):

```uname -a```

Find out linux version (method 4):

```cat /proc/version```



Rsync / SSH / scp commands
====================

1. Rsync whole folder to remote machine:

```rsync -a <dir> <user>@$<host>:```

2. Open a SSH tunnel: https://plenz.com/tunnel-everything.php

```ssh -NL 2345:127.0.0.1:8000 <user>@<host>```

3. Scp a file from a remote host

```scp snemeth@<HOST>:642171.tar.gz /Users/szilardnemeth/Downloads/```


Other tricks
============

1. Trick: Watch directory contents for changes (cgroup)

```while true; do date +'%H:%M:%S:%N' | tee -a /tmp/tmp2 && find /sys/fs/cgroup | grep hadoop 2>&1 | tee -a /tmp/tmp2; sleep 1; done```

2. Get OS version: 
- `lsb_release -ana`
- `uname -a`
- `cat /etc/os-release`


Disk management
============
1. Change the reserved blocks on a partition: 

> Specify the percentage of the filesystem blocks reserved for the super-user. This avoids fragmentation, and allows root-owned daemons, such as syslogd(8), to continue to function correctly after non-privi-leged processes are prevented from writing to the filesystem. The default percentage is 5%.

Links:

https://askubuntu.com/questions/100212/my-df-totals-dont-come-close-to-adding-up-why
https://ma.ttias.be/change-reserved-blocks-ext3-ext4-filesystem-linux/

Command to query reserved block count: 

```sudo /sbin/tune2fs -l /dev/md0  | grep "Reserved block count"```


Command to change reserved block count, -m0 means 0 percent:

```sudo /sbin/tune2fs -m0 /dev/md0```


Process commands
============
Kill process based on grep expression:
```kill $(ps aux | grep 'mapreduce-examples' | awk '{print $2}')```

Wait for process to complete by its pid:
```tail --pid=$pid -f /dev/null```
Details: https://unix.stackexchange.com/a/427133/189441


Print all process names that are connected to the internet: 
```sudo lsof -nPi | cut -f 1 -d " " | uniq | tail -n  +2```