
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



SSH / scp commands
====================

## Open a SSH tunnel: https://plenz.com/tunnel-everything.php

```ssh -NL 2345:127.0.0.1:8000 <user>@<host>```

## Scp a file from a remote host

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
