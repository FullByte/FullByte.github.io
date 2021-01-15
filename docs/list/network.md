# Network

## DNS Server

A list of public DNS Servers

|Provider|Primary DNS Server|Secondary DNS Server|
|---|---|---|
|OpenDNS|208.67.222.222|208.67.220.220|
|Level3|209.244.0.3|209.244.0.4|
|Verisign|64.6.64.6|64.6.65.6|
|Google|8.8.8.8|8.8.4.4|
|Quad9|9.9.9.9|149.112.112.112|
|Comodo DNS|8.26.56.26|8.20.247.20|
|OpenDNS Home|208.67.222.222|208.67.220.220|
|Norton ConnectSafe|199.85.126.10|199.85.127.10|
|GreenTeamDNS|81.218.119.11|209.88.198.133|
|SafeDNS|195.46.39.39|195.46.39.40|
|OpenNIC|69.195.152.204|23.94.60.240|
|SmartViper|208.76.50.50|208.76.51.51|
|Dyn|216.146.35.35|216.146.36.36|
|FreeDNS|37.235.1.174|37.235.1.177|
|Alternate DNS|198.101.242.72|23.253.163.53|
|Yandex.DNS|77.88.8.8|77.88.8.1|
|UncensoredDNS|91.239.100.100|89.233.43.71|
|Hurricane Electric|74.82.42.42| ||
|puntCAT|109.69.8.51||
|CCC|213.73.91.35||
|anycast censurfridns|91.239.100.100|89.233.43.71|
|dns.watch|84.200.69.80|84.200.70.40|

## TTL as OS identifier

There is a chance to guess the OS based on its TTL.
Here is an overview:

|OS | Version | Protocol | TTL |
|------|---------|----|-----|
| *nix (Linux/Unix)| | | 64  |
|AIX | 3.2, 4.1 | ICMP | 255 |
|AIX | |  TCP | 60 |
|AIX | |  UDP | 30 |
|BSDI | BSD/OS 3.1 and 4.0 | ICMP | 255 |
|Cisco | | ICMP | 254 |
|Compa | Tru64 v5.0 | ICMP | 64 |
|DEC Pathworks | V5 | TCP and UDP | 30|
|Foundry | | ICMP | 64|
|FreeBSD | 5 | ICMP | 64|
|FreeBSD | 3.4, 4.0 | ICMP | 255|
|FreeBSD | 2.1R | TCP and UDP | 64|
|HP-UX | 9.0x | TCP and UDP | 30|
|HP-UX | 11 | ICMP | 255|
|HP-UX | 11 | TCP | 64|
|HP-UX | 10.2 | ICMP | 255|
|HP-UX | 10.01 | TCP and UDP | 64|
|Irix | 6.x | TCP and UDP | 60|
|Irix | 6.5.3, 6.5.8 | ICMP | 255|
|Irix | 5.3 | TCP and UDP | 60|
|Linux | Red Hat 9 | ICMP and TCP | 64|
|Linux | 2.4 kernel | ICMP | 255|
|Linux | 2.2.14 kernel | ICMP | 255|
|Linux | 2.0.x kernel | ICMP | 64|
|MPE/IX (HP) | | ICMP | 200|
|MacOS/MacTCP | X (10.5.6) | ICMP/TCP/UDP | 64|
|MacOS/MacTCP | 2.0.x | TCP and UDP | 60|
|NetBSD || ICMP | 255|
|Netgear FVG318 || ICMP and UDP | 64|
|OS/2 | |TCP/IP 3.0 | 64|
|OSF/1 | V3.2A | TCP | 60|
|OSF/1 | V3.2A | UDP | 30|
|OpenBSD | 2.6 & 2.7 | ICMP | 255|
|OpenVMS | 07.01.2002 | ICMP | 255|
|Solaris | 2.8 | TCP | 64|
|Solaris | 2.5.1, 2.6, 2.7, 2.8 | ICMP | 255|
|Solaris/AIX || | 254 |
|Stratus | TCP_OS (14.3+) | TCP and UDP | 64|
|Stratus | TCP_OS (14.2-) | TCP and UDP | 30|
|Stratus | TCP_OS | ICMP | 255|
|Stratus | STCP | ICMP/TCP/UDP | 60|
|SunOS | 5.7 | ICMP and TCP | 255|
|SunOS | 4.1.3/4.1.4 | TCP and UDP | 60|
|Ultrix | V4.2 – 4.5 | ICMP | 255|
|Ultrix | V4.1/V4.2A | TCP | 60|
|Ultrix | V4.1/V4.2A | UDP | 30|
|VMS/Multinet || TCP and UDP | 64|
|VMS/TCPware | |TCP | 60|
|VMS/TCPware | |UDP | 64|
|VMS/UCX | |TCP and UDP | 128|
|VMS/Wollongong | 1.1.1.1 | TCP | 128|
|VMS/Wollongong | 1.1.1.1 | UDP | 30|
|Windows | for Workgroups | TCP and UDP | 32|
|Windows | XP | ICMP/TCP/UDP | 128|
|Windows | Vista | ICMP/TCP/UDP | 128|
|Windows | Server 2008 | ICMP/TCP/UDP | 128|
|Windows | Server 2003 || 128|
|Windows | NT 4.0 SP6+ || 128|
|Windows | NT 4.0 SP5- | |32|
|Windows | NT 4.0 | TCP and UDP | 128|
|Windows | NT 4 WRKS SP 3, SP 6a | ICMP | 128|
|Windows | NT 4 Server SP4 | ICMP | 128|
|Windows | NT 3.51 | TCP and UDP | 32|
|Windows | ME | ICMP | 128|
|Windows | 98, 98 SE | ICMP | 128|
|Windows | 98 | ICMP | 32|
|Windows | 98 | TCP | 128|
|Windows | 95 | TCP and UDP | 32|
|Windows | 7 | ICMP/TCP/UDP | 128|
|Windows | 2000 pro | ICMP/TCP/UDP | 128|
|Windows | 2000 family | ICMP | 128|
|Windows | 10 | ICMP/TCP/UDP | 128|
| Windows |   |        | 128 |
|juniper || ICMP | 64|
