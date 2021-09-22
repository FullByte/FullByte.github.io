# Linux Bash

Most commands listed here will work on any linux distributions but if in doubt it will most likely run on the latest Ubuntu.

Some great helpers:

- Understand commands: <https://explainshell.com/>
- ShellCheck gives warnings and suggestions for bash/sh shell scripts: <https://github.com/koalaman/shellcheck>

## Basics

Random basics

- Check installed packges ```sudo tasksel```
- Update and upgrade ```sudo apt update && apt -y full-upgrade && apt -y autoremove```
- Upgrading to a newer release ```do-release-upgrade```
- Check who is online ```w```
- Show all system users ```cut -d: -f1 /etc/passwd```
- Top commands used ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -nr```
- Commands only used once ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -n | grep ' 1 '```

## bashrc

Paste these function in the ~/.bashrc file.

Make a new folder and cd into it

- Usage: mkcd name1
- Code ```mkcd(){ NAME=$1; mkdir -p "$NAME"; cd "$NAME"; }```

## System Information

Get system details

- Get all environment variables ```printenv```
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

More...

- List open file descriptors (-i flag for network interfaces): ```lsof -i :8080```
- Stream current disk, network, CPU activity, etc: ```dstat -a```
- Trace system calls of a program: ```strace -f -e <syscall> <cmd>```
- Print currently active processes: ```ps aux | head -n20```
- Visualize process forks: ```pstree```
- Show size on disk for directories and their contents: ```du -ha```
- List currently open Internet/UNIX sockets and related information ```netstat | head -n20```
- Find hostname for a remote IP address: ```nslookup <IP address>```
- Current installed version: ```cat /etc/issue```
- Kernel information: ```uname -a```
- OS information: ```lsb_release -a```
- Device Information: ```lspci -v```
- Check the hostname of your machine: ```hostname```
- Shows last logged in users: ```last```
- Shows currently logged in user and groups for the user: ```id```
- List users on Linux: ```getent passwd```
- Show mounted drives: ```mount```
- Shows running kernel version: ```uname -ar```
- Show bash history, commands the user has entered previously: ```history```

## Disk Stuff

**DD:** low-level data dumping utility

- burning an ISO image to USB stick is just one command away: ```sudo dd if=ubuntu-18.04.1-desktop-amd64.iso of=/dev/sdb bs=1M```
- hard wipe a disk: ```sudo dd if=/dev/zero of=/dev/sda```

**DU:** Disk usage command is used for quickly estimating the drive space used in a folder or partition

- Show files and sort by size: ```/data/java$ du -sh * | sort -h```

**DF:** Used for estimating disk space but for the entire disk rather than a directory or folder.

- show which partition is how much full: ```df -h```

## MORE STUFF

- Execute a command and report statistics about how long it took: ```time <cmd>```
- Send a process in current tty into background and back to foreground: ```CTRL + z ; bg; jobs; fg```
- Change Default Shell For A User: ```chsh -s /usr/bin/zsh username```
- Make and Change To That New Directory: ```mkdir new_dir && cd $```
- Configure Your Server Timezone: ```dpkg-reconfigure tzdata```
- Kill Everything Running On A Certain Port ```sudo kill "sudo lsof -t -i:3000"```
- See if the http status of the request changes: ``` watch -d curl -LIs localhost:3000```
- Update access and modify time: ```touch README.md```
- Update access time: ```touch -a README.md```
- Update modify time: ```touch -m README.md```
- Show The Size Of Everything In A Directory ```ls | xargs du -sh```
- Saying Yes: ```yes | rm -r ~/some/dir```
- Show Disk Usage For The Current Directory: ```du -h | sort -nr```

## Display all terminal colors

```bash
for x in {0..8}; do 
    for i in {30..37}; do 
        for a in {40..47}; do 
            echo -ne "\e[$x;$i;$a""m\\\e[$x;$i;$a""m\e[0;37;40m "
        done
        echo
    done
done
echo ""
```

## String Manipulation

- Add "new entry" in line 13 of file "file.txt" ```sed -n -i 'p;13a new entry' file.txt```

## Work with a file

- Cat A File With Line Numbers: ```cat -n file```
- Line count in a file: ```wc -l <file>```
- Count unique words in a file: ```cat file.txt | xargs -n1 | sort | uniq -c```
- Display contents of a zipped text file: ```zcat <file.gz>```
- Copy a file from remote to local server, or vice versa: ```scp <user@remote_host> <local_path>```
- List Stats For A File: ```stat -x README.md```
- Securely Remove Files ```srm -vz README.md``` or ```shred -uvz -n 5 README.md```
- Securely Remove Files after rm was used: ```sfill -lvz /home```
- Copying File Contents To System Paste Buffer: ```cat some-file.txt | pbcopy```
- Exclude A Directory With Find: ```find . -type f -not -path './.git/*' -ctime -10```
- File Type Info With File: ```file data.txt```
- Find Newer Files than this file: ```find blog -name '*.md' -newer blog/first-post.md```
- Get The Unix Timestamp: ```date +%s```
- Hexdump A Compiled File  ```cat Hello.class | hexdump -C ```
- Grep For Files Without A Match: ```grep -L "foobar" ./*```
- Grep For Files With Multiple Matches ```grep -rl "match1" src/css | xargs grep -l "match2"```

## Network Stuff

- Find Device in Monitoring Mode: ```iwconfig 2>/dev/null | grep "Mode\\:Monitor" | awk '{print $1}'```
- Find Access Point: ```iwconfig 2>&1 | sed -n -e 's/^.\*Access Point: //p'```
- Linux IPv6 search devices in local network: ```ping6 -c 2 -I en0 -w ff02::1```
- Show Linux network ports with process ID’s (PIDs): ```netstat -tulpn```
- Watch TCP, UDP open ports in real time with socket summary: ```watch ss -stplu```
- Show established connections: ```lsof -i```
- Change MAC address: ```macchanger -m MACADDR INTR```
- Change MAC address using ifconfig: ```ifconfig eth0 hw ether MACADDR```
- Get hostname for IP address ```nbtstat -A x.x.x.x```
- Block access to e.g. "google.com" from the host machine ```tcpkill -9 host google.com```
- Enable IP forwarding: ```echo "1" > /proc/sys/net/ipv4/ip_forward```
- Change DNS to 1.1.1.1: ```echo "1.1.1.1" > /etc/resolv.conf```
- Nmap scan every interface that is assigned an IP: ```ifconfig -a | grep -Po '\b(?!255)(?:\d{1,3}\.){3}(?!255)\d{1,3}\b' | xargs nmap -A -p0-```
- Extract your external IP address using dig: ```dig +short myip.opendns.com @resolver1.opendns.com```

## Fun Stuff

Entertaining nonsense:

- Loop Train: ```for i in {1..10}; do sl; done```

Alternatives for `tree` command:

- ```ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//──/g' -e 's/─/├/' -e '$s/├/└/'```
- ```find . -not -path '*/\.*' | python -c "import sys as s;s.a=[];[setattr(s,'a',list(filter(lambda p: c.startswith(p+'/'),s.a)))or (s.stdout.write('  '*len(s.a)+c[len(s.a[-1])+1 if s.a else 0:])or True) and s.a.append(c[:-1]) for c in s.stdin]"```

If you don't have `tree` maybe create an as such: `alias tree='command from above here'`

### Screen

```shell
screen # attach
strg+a --> "d" # detach
screen -r # re-attach
```

## Other

- Reboot: ```init 6```
- Compile C code: ```gcc -o output.c input.c```
- Compile 32 bit binary on 64 bit Linux: ```gcc -m32 -o output.c input.c```
- Disable bash history logging: ```unset HISTORYFILE```
- Connect to RDP server from Linux. ```rdesktop X.X.X.X```
- Kill current session: ```kill -9 $$```
- Clear bash history: ```cat /dev/null > ~/.bash_history```

### Fun

[Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) simulation

```sh
echo -ne "\033#8";X=`tput cols`;Y=`tput lines`;((a=$X/2));((b=$Y/2));d=1;while case $d in 0)((a=a<2?X:a-1));;1)((b=b<2?Y:b-1));;2)((a=a==X?1:a+1));;3)((b=b==Y?1:b+1));; esac;do ((c=b+a*X));v=${k[c]:- };[ $v. = @. ]&&{((d=d>2?0:d+1));k[c]="";}||{(( d=d<1?3:d-1));k[c]=@;};echo -ne "\033[$b;${a}H$v";done
```
