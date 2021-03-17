# Linux / Ubuntu

Most commands listed here will work on any linux distributions but if in doubt it will most likely run on the latest Ubuntu.
Great tool to understand commands: <https://explainshell.com/>

## Basics

Random basics

- Check installed packges ```sudo tasksel```
- Update and upgrade ```sudo apt update && sudo apt upgrade -y```
- Upgrading to a newer release ```do-release-upgrade```
- Check who is online ```w```
- Show all system users ```cut -d: -f1 /etc/passwd```
- Top commands used ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -nr```
- Commands only used once ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -n | grep ' 1 '```

Get system details

- Get all enviornment variables ```printenv```
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

## Create the boot script

Example script that install updates to ubuntu automatically

The script "bootupdate.sh":

```shell
#!/bin/bash
sudo apt update && sudo apt upgrade -y
exit 0
```

Move "bootupdate.sh" to init.d

```shell
mv bootupdate.sh /etc/init.d/bootupdate.sh
```

Add script to boot sequente

```shell
update-rc.d bootupdate.sh start 2
```

## Make Ubuntu Desktop nice

```shell
# Get Video Codecs
sudo apt-get install ubuntu-restricted-extras ubuntu-restricted-addons

# Get Compiz and Docky
sudo apt-get install gnome-session-flashback compiz compiz-core compiz-plugins compiz-plugins-default compiz-plugins-extra compiz-plugins-main compiz-plugins-main-default compiz-plugins-main-dev compizconfig-settings-manager docky

#Gnome Tweak
sudo apt-get install gnome-tweaks gnome-tweak-tool
```

## Add/Remove User

```shell
adduser <user> # Add user
gpasswd -a <user> <group> # Add user to group
groups <user> # Show groups the user is added to
gpasswd -d <user> <group> # Remove user from group

passwd -l <user> # Lock the  User account
killall -9 -u <user> # Kill all running processes of the User
crontab -r -u <user> # Delete the user's cron jobs
lprm <user> # Delete printer jobs run
userdel -r <user> # Delete/ remove user account and files
```

## Install xrdp

```shell
sudo apt-get updates
sudo apt-get install tasksel
sudo apt-get install xrdp # start RDP
sudo systemctl status xrdp #verify
```

## Install TeamViewer

```shell
wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
sudo apt-get install ./teamviewer_amd64.deb
teamviewer
teamviewer --passwd password
teamviewer daemon restart
teamviewer -info
teamviewer license accept
```

## Install latest Node.js version

```shell
sudo apt update
sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt -y install nodejs
sudo apt -y  install gcc g++ make
node --version
npm --version
```

## Install and Update

**Keyboard layout**

```shell
dpkg-reconfigure keyboard-configuration
service keyboard-setup restart
```

**Define a new password**

```shell
passwd
```

**Configure WiFi**

```shell
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
    ssid="WiFi"
    psk="WiFiPassword"
}
sudo wpa_cli reconfigure
```

eventually reboot and/or try this:

```shell
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
sudo ifconfig wlan0 | grep inet
sudo service networking restart
```

Test Config:

```shell
wpa_supplicant -i wlan0 -D wext -c /etc/wpa_supplicant/wpa_supplicant.conf -d
```

## System Information

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

**Grep For Files With Multiple Matches**

Get a list of filenames that contain both a line with `@media only screen` and a line with `.class-name`.
If you need to, chain more `grep` commands on to narrow things down even farther.

```bash
$ grep -rl "@media only screen" src/css |
    xargs grep -l ".class-name"
```

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

## Fun Stuff

- Loop Train: ```for i in {1..10}; do sl; done```

## COMMANDs

### Misc Commands

init 6	Reboot Linux from the command line.
gcc -o output.c input.c	Compile C code.
gcc -m32 -o output.c input.c	Cross compile C code, compile 32 bit binary on 64 bit Linux.
unset HISTORYFILE	Disable bash history logging.
rdesktop X.X.X.X	Connect to RDP server from Linux.
kill -9 $$	Kill current session.

ssh user@X.X.X.X | cat /dev/null > ~/.bash_history   Clear bash history
    
### Linux File System Permissions

- Change owner of file or dir: ```chown user:group blah```
- Change owner of file or dir recersive for all folders below: ```chown -R user:group blah```
- Change file / dir permissions: ```chmod 600 file```

|VALUE|RWX|MEANING|
|---|--|--|
|777|rwxrwxrwx| No restriction, global WRX any user can do anything.|
|755|rwxr-xr-x| Owner has full access, others can read and execute the file.|
|700|rwx------| Owner has full access, no one else has access.|
|666|rw-rw-rw-| All users can read and write but not execute.|
|644|rw-r--r--| Owner can read and write, everyone else can read.|
|600|rw-------| Owner can read and write, everyone else has no access.|

### Linux File System

- **/bin** Common programs, shared by the system, the system administrator and the users.
- **/boot** Boot files, boot loader (grub), kernels, vmlinuz
- **/dev** Contains references to system devices, files with special properties.
- **/etc** Important system config files.
- **/home** Home directories for system users.
- **/lib** Library files, includes files for all kinds of programs needed by the system and the users.
- **/lost+found** Files that were saved during failures are here.
- **/mnt** Standard mount point for external file systems.
- **/media** Mount point for external file systems (on some distros).
- **/net** Standard mount point for entire remote file systems – nfs.
- **/opt** Typically contains extra and third party software.
- **/proc** A virtual file system containing information about system resources.
- **/root** root users home dir.
- **/sbin** Programs for use by the system and the system administrator.
- **/tmp** Temporary space for use by the system, cleaned upon reboot.
- **/usr** Programs, libraries, documentation etc. for all user-related programs.
- **/var** Storage for all variable files and temporary files created by users, such as log files, mail queue, print spooler. Web servers, Databases etc.

### Linux interesting files and directories

Places that are worth a look if you are attempting to privilege escalate / perform post exploitation.

- **/etc/passwd** Contains local Linux users.
- **/etc/shadow** Contains local account password hashes.
- **/etc/group** Contains local account groups.
- **/etc/init.d/** Contains service init script – worth a look to see whats installed.
- **/etc/hostname** System hostname.
- **/etc/network/interfaces** Network interfaces.
- **/etc/resolv.conf** System DNS servers.
- **/etc/profile** System environment variables.
- **~/.ssh/** SSH keys.
- **~/.bash_history** Users bash history log.
- **/var/log/** Linux system log files are typically stored here.
- **/var/adm/** UNIX system log files are typically stored here.
- **/var/log/httpd/access.log** Apache access log file typical path.
- **/etc/fstab** File system mounts.

## Cron Jobs

### Examples

```shell
Every Minute    * * * * *
Every Five Minutes    */5 * * * *
Every 10 Minutes    */10 * * * *
Every 15 Minutes    */15 * * * *
Every 30 Minutes    */30 * * * *
Every Hour    0 * * * *
Every Two Hours    0 */2 * * *
Every Six Hours    0 */6 * * *
Every 12 Hours    0 */12 * * *
During the Work Day    */5 9-17 * * *
Every day at Midnight    0 0 * * *
Every Two Weeks    0 0 * * Sun [ $(expr $(date +%W) % 2) -eq 1 ] && /path/to/command
At the Start of Every Month    0 0 1 * *
On January 1st at Midnight    0 0 1 1 *
```
