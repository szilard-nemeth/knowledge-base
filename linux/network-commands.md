Various commands:

ifconfig

bond interface

iwconfig

tcpdump


1. Change MAC address of network inteface

`sudo ifconfig eth0 down; ifconfig eth0 hw ether 00:16:D4:B6:67:5B; ifconfig eth0 up;dhcp`

More info: https://blog.sleeplessbeastie.eu/2013/01/11/how-to-change-the-mac-address-of-an-ethernet-interface/


2. Check if port is open

https://superuser.com/questions/621870/test-if-a-port-on-a-remote-system-is-reachable-without-telnet
```
cat < /dev/tcp/127.0.0.1/22
```

AND 

Single port: `nc -zv 127.0.0.1 80`

Multiple ports: `nc -zv 127.0.0.1 22 80 8080`

Range of ports: `nc -zv 127.0.0.1 20-30`

Mac OS: https://superuser.com/questions/115553/netcat-on-mac-os-x 


How can I list my open network ports with netstat? https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat

`sudo lsof -PiTCP -sTCP:LISTEN` and `netstat -anvp tcp | awk 'NR<3 || /LISTEN/'`