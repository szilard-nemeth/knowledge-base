Various commands:

ifconfig

bond interface

iwconfig

tcpdump


1. Change MAC address of network inteface

`sudo ifconfig eth0 down; ifconfig eth0 hw ether 00:16:D4:B6:67:5B; ifconfig eth0 up;dhcp`

More info: https://blog.sleeplessbeastie.eu/2013/01/11/how-to-change-the-mac-address-of-an-ethernet-interface/