# Ubuntu

## Basics

Random basics

- Check installed packges ```sudo tasksel```
- Update and upgrade ```sudo apt update && sudo apt upgrade -y```
- Upgrading to a newer release ```do-release-upgrade```
- Check who is online ```w```
- Show all system users ```cut -d: -f1 /etc/passwd```
- Top commands used ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -nr```
- Commands only used once ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -n | grep ' 1 '```

Get system details

- Get all enviornment variables ```printenv```
- Get all configuration variables ```getconf -a```
- Show ports/connections open ```lsof```
- Get ubuntu version ```lsb_release -r```
- Free disk space ```df -h```

System Performance Check

- ```uptime```
- ```dmesg | tail```
- ```vmstat 1```
- ```mpstat -P ALL 1```
- ```pidstat 1```
- ```iostat -xz 1```
- ```free -m```
- ```sar -n DEV 1```
- ```sar -n TCP,ETCP 1```
- ```top```

## Create the boot script

Example script that install updates to ubuntu automatically

The script "bootupdate.sh":

```shell
#!/bin/bash
sudo apt update && sudo apt upgrade -y
exit 0
```

Move "bootupdate.sh" to init.d

```shell
mv bootupdate.sh /etc/init.d/bootupdate.sh
```

Add script to boot sequente

```shell
update-rc.d bootupdate.sh start 2
```

## Make Ubuntu Desktop nice

Get Video Codecs

```shell
sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons
```

Get Compiz and Docky

```shell
sudo apt-get install gnome-session-flashback compiz compiz-core compiz-plugins compiz-plugins-default compiz-plugins-extra compiz-plugins-main compiz-plugins-main-default compiz-plugins-main-dev compizconfig-settings-manager docky
```

Gnome Tweak

```shell
sudo apt-get install gnome-tweaks gnome-tweak-tool
```

## Network Tools

1. arpwatch – Ethernet Activity Monitor.
2. bmon – bandwidth monitor and rate estimator.
3. bwm-ng – live network bandwidth monitor.
4. curl – transferring data with URLs.
5. darkstat – captures network traffic, usage statistics.
6. dhclient – Dynamic Host Configuration Protocol Client
7. dig – query DNS servers for information.
8. dstat – replacement for vmstat, iostat, mpstat, netstat and ifstat.
9. ethtool – utility for controlling network drivers and hardware.
10. ftp – simplest file transfer protocol.
11. gated – gateway routing daemon.
12. host – DNS lookup utility.
13. hping – TCP/IP packet assembler/analyzer.
14. ibmonitor – shows bandwidth and total data transferred.
15. ifstat –  report network interfaces bandwidth.
16. iftop – display bandwidth usage.
17. ip (PDF file) – a command with more features that ifconfig (net-tools).
18. iperf3 – network bandwidth measurement tool. (above screenshot Stacklinux VPS)
19. iproute2 – collection of utilities for controlling TCP/IP.
20. IPTraf – An IP Network Monitor.
21. iputils – set of small useful utilities for Linux networking.
22. jwhois (whois) – client for the whois service.
23. mtr – network diagnostic tool.
24. net-tools – utilities include: arp, hostname, ifconfig, netstat, rarp, route, plipconfig, slattach, mii-tool, iptunnel and ipmaddr.
25. ncat – improved re-implementation of the venerable netcat.
26. netcat – networking utility for reading/writing network connections.
27. nethogs – a small ‘net top’ tool.
28. Netperf – Network bandwidth Testing.
29. netsniff-ng – Swiss army knife for daily Linux network plumbing.
30. netstat – Print network connections, routing tables, statistics, etc.
31. netwatch – monitoring Network Connections.
32. nload – display network usage.
33. nmap – network discovery and security auditing.
34. nslookup – query Internet name servers interactively.
35. ping – send icmp echo_request to network hosts.
36. route – show / manipulate the IP routing table.
37. slurm – network load monitor.
38. smokeping –  keeps track of your network latency.
39. speedometer – Measure and display the rate of data across a network.
40. speedtest-cli – test internet bandwidth using speedtest.net
41. ss – utility to investigate sockets.
42. ssh –  secure system administration and file transfers over insecure networks.
43. tcpdump – command-line packet analyzer.
44. tcptrack – Displays information about tcp connections on a network interface.
45. telnet – user interface to the TELNET protocol.
46. tracepath – very similar function to traceroute.
47. traceroute – print the route packets trace to network host.
48. vnStat – network traffic monitor.
49. wget –  retrieving files using HTTP, HTTPS, FTP and FTPS.
50. Wireless Tools for Linux – includes iwconfig, iwlist, iwspy, iwpriv and ifrename.
51. Wireshark – network protocol analyzer.
