# Linux Commands and Tools

Add <https://explainshell.com/> link to all cool commands :)

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

**Basic Tools**

```shell
sudo apt-get install htop screen nodejs npm python3-pip
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

## Process Information

**List open file descriptors (-i flag for network interfaces)**

```shell
lsof -i :8080
```

**Stream current disk, network, CPU activity & more**

```shell
dstat -a
```

**Trace system calls of a program (-e flag to filter for certain system calls)**

```shell
strace -f -e <syscall> <cmd>
```

**Print currently active processes**

```shell
ps aux | head -n20
```

**Visualize process forks**

```shell
pstree
```

**Show size on disk for directories and their contents**

```shell
du -ha
```

## Network Information

**List currently open Internet/UNIX sockets and related information**

```shell
netstat | head -n20
```

**Find hostname for a remote IP address**

```shell
nslookup <IP address>
```

## System Information

**Current installed version:**

```shell
cat /etc/issue
```

**Kernel information**

```shell
uname -a
```

**OS information**

```shell
lsb_release -a
```

**Device Information**

```shell
lspci -v
```

**Check the hostname of your machine (ie. the name so other computers can reach you)**

```shell
hostname
```

## Random stuff

### DD

low-level data dumping utility

**burning an ISO image to USB stick is just one command away:**

```shell
sudo dd if=ubuntu-18.04.1-desktop-amd64.iso of=/dev/sdb bs=1M
```

**hard wipe a disk**

```shell
sudo dd if=/dev/zero of=/dev/sda
```

### DU

Disk usage command is used for quickly estimating the drive space used in a folder or partition

**Show files and sort by size:**

```shell
/data/java$ du -sh * | sort -h
```

### DF

Used for estimating disk space but for the entire disk rather than a directory or folder.

**show which partition is how much full**

```shell
df -h
```

### MORE STUFF

**Execute a command and report statistics about how long it took**

```shell
time <cmd>
```

**Send a process in current tty into background and back to foreground**

```shell
CTRL + z ; bg; jobs; fg
```

**Count unique words in a file**

```shell
cat file.txt | xargs -n1 | sort | uniq -c
```

**Line count in a file**

```shell
wc -l <file>
```

**Display contents of a zipped text file**

```shell
zcat <file.gz>
```

**Copy a file from remote to local server, or vice versa**

```shell
scp <user@remote_host> <local_path>
```

## String Manipulation

### Add "new entry" in line 13 of file "file.txt"
```shell
sed -n -i 'p;13a new entry' file.txt
```

### TODO

**Find Device in Monitoring Mode**
iwconfig 2>/dev/null | grep "Mode\\:Monitor" | awk '{print $1}'

**Find Access Point**
iwconfig 2>&1 | sed -n -e 's/^.\*Access Point: //p'

\#######
    ls -lha
        list directory (verbose)
    pwd
        print the present working directory

    grep -inr {string}
        find a string in any files in this directory or child directories

    tree -LhaC 3
        show directory structure 3 levels down (with file sizes and including hidden directories)

    sed -i "s/{find}/{replace}/g" {file}
        replace a string in a file

    find . -type f -name '*.txt' -exec sed -i "s/{find}/{replace}/g" {} \;
        replace a string for each file in this and child folders with a name like *.txt

    tmux new -s session, tmux attach -t session
        create another terminal session without creating a new window [advanced]

    curl -X POST -d "{key: value}" http://www.google.com
        send an HTTP request to a web server

Linux IPv6 search devices in local network:
ping6 -c 2 -I en0 -w ff02::1


## Fun Stuff

Loop Train

```shell
for i in {1..10}; do sl; done
```


## COMMANDs

netstat -tulpn	Show Linux network ports with process ID’s (PIDs)
watch ss -stplu	Watch TCP, UDP open ports in real time with socket summary.
lsof -i	Show established connections.
macchanger -m MACADDR INTR	Change MAC address on KALI Linux.
ifconfig eth0 192.168.2.1/24	Set IP address in Linux.
ifconfig eth0:1 192.168.2.3/24	Add IP address to existing network interface in Linux.
ifconfig eth0 hw ether MACADDR	Change MAC address in Linux using ifconfig.
ifconfig eth0 mtu 1500	Change MTU size Linux using ifconfig, change 1500 to your desired MTU.
dig -x 192.168.1.1 	Dig reverse lookup on an IP address.
host 192.168.1.1 	Reverse lookup on an IP address, in case dig is not installed.
dig @192.168.2.2 domain.com -t AXFR	Perform a DNS zone transfer using dig.
host -l domain.com nameserver	Perform a DNS zone transfer using host.
nbtstat -A x.x.x.x	Get hostname for IP address.
ip addr add 192.168.2.22/24 dev eth0	Adds a hidden IP address to Linux, does not show up when performing an ifconfig.
tcpkill -9 host google.com	Blocks access to google.com from the host machine.
echo "1" > /proc/sys/net/ipv4/ip_forward	Enables IP forwarding, turns Linux box into a router – handy for routing traffic through a box.
echo "8.8.8.8" > /etc/resolv.conf	Use Google DNS.

### System Information Commands

Useful for local enumeration.

whoami	Shows currently logged in user on Linux.
id	Shows currently logged in user and groups for the user.
last	Shows last logged in users.
mount	Show mounted drives.
df -h	Shows disk usage in human readable output.
echo "user:passwd" | chpasswd	Reset password in one line.
getent passwd	List users on Linux.
strings /usr/local/bin/blah	Shows contents of none text files, e.g. whats in a binary.
uname -ar	Shows running kernel version.
PATH=$PATH:/my/new-path	Add a new PATH, handy for local FS manipulation.
history	Show bash history, commands the user has entered previously.
Redhat / CentOS / RPM Based Distros
COMMAND	DESCRIPTION
cat /etc/redhat-release	Shows Redhat / CentOS version number.
rpm -qa	List all installed RPM’s on an RPM based Linux distro.
rpm -q --changelog openvpn	Check installed RPM is patched against CVE, grep the output for CVE.


### Linux User Management

useradd new-user	Creates a new Linux user.
passwd username	Reset Linux user password, enter just passwd if you are root.
deluser username	Remove a Linux user.

### Linux Decompression Commands

How to extract various archives (tar, zip, gzip, bzip2 etc) on Linux and some other tricks for searching inside of archives etc.
unzip archive.zip	Extracts zip file on Linux.

zipgrep *.txt archive.zip	Search inside a .zip archive.
tar xf archive.tar	Extract tar file Linux.
tar xvzf archive.tar.gz	Extract a tar.gz file Linux.
tar xjf archive.tar.bz2	Extract a tar.bz2 file Linux.
tar ztvf file.tar.gz | grep blah	Search inside a tar.gz file.
gzip -d archive.gz	Extract a gzip file Linux.
zcat archive.gz	Read a gz file Linux without decompressing.
zless archive.gz	Same function as the less command for .gz archives.
zgrep 'blah' /var/log/maillog*.gz	Search inside .gz archives on Linux, search inside of compressed log files.
vim file.txt.gz	Use vim to read .txt.gz files (my personal favorite).
upx -9 -o output.exe input.exe	UPX compress .exe file Linux.

### Linux Compression Commands

zip -r file.zip /dir/*	Creates a .zip file on Linux.
tar cf archive.tar files	Creates a tar file on Linux.
tar czf archive.tar.gz files	Creates a tar.gz file on Linux.
tar cjf archive.tar.bz2 files	Creates a tar.bz2 file on Linux.
gzip file	Creates a file.gz file on Linux.

### Linux File Commands

df -h blah	Display size of file / dir Linux.
diff file1 file2	Compare / Show differences between two files on Linux.
md5sum file	Generate MD5SUM Linux.
md5sum -c blah.iso.md5	Check file against MD5SUM on Linux, assuming both file and .md5 are in the same dir.
file blah	Find out the type of file on Linux, also displays if file is 32 or 64 bit.
dos2unix	Convert Windows line endings to Unix / Linux.
base64 < input-file > output-file	Base64 encodes input file and outputs a Base64 encoded file called output-file.
base64 -d < input-file > output-file	Base64 decodes input file and outputs a Base64 decoded file called output-file.
touch -r ref-file new-file	Creates a new file using the timestamp data from the reference file, drop the -r to simply create a file.
rm -rf	Remove files and directories without prompting for confirmation.

### Samba Commands

Connect to a Samba share from Linux.

$ smbmount //server/share /mnt/win -o user=username,password=password1
$ smbclient -U user \\\\server\\share
$ mount -t cifs -o username=user,password=password //x.x.x.x/share /mnt/share
Breaking Out of Limited Shells
Credit to G0tmi1k for these (or wherever he stole them from!).
The Python trick:
python -c 'import pty;pty.spawn("/bin/bash")'
echo os.system('/bin/bash')
/bin/sh -i

### Misc Commands

init 6	Reboot Linux from the command line.
gcc -o output.c input.c	Compile C code.
gcc -m32 -o output.c input.c	Cross compile C code, compile 32 bit binary on 64 bit Linux.
unset HISTORYFILE	Disable bash history logging.
rdesktop X.X.X.X	Connect to RDP server from Linux.
kill -9 $$	Kill current session.
chown user:group blah	Change owner of file or dir.
chown -R user:group blah	Change owner of file or dir and all underlying files / dirs – recersive chown.
chmod 600 file	Change file / dir permissions
ssh user@X.X.X.X | cat /dev/null > ~/.bash_history   Clear bash history
    
### Linux File System Permissions

VALUE	MEANING
777	rwxrwxrwx No restriction, global WRX any user can do anything.
755	rwxr-xr-x Owner has full access, others can read and execute the file.
700	rwx------ Owner has full access, no one else has access.
666	rw-rw-rw- All users can read and write but not execute.
644	rw-r--r-- Owner can read and write, everyone else can read.
600	rw------- Owner can read and write, everyone else has no access.

### Linux File System

/	/ also know as “slash” or the root.
/bin	Common programs, shared by the system, the system administrator and the users.
/boot	Boot files, boot loader (grub), kernels, vmlinuz
/dev	Contains references to system devices, files with special properties.
/etc	Important system config files.
/home	Home directories for system users.
/lib	Library files, includes files for all kinds of programs needed by the system and the users.
/lost+found	Files that were saved during failures are here.
/mnt	Standard mount point for external file systems.
/media	Mount point for external file systems (on some distros).
/net	Standard mount point for entire remote file systems – nfs.
/opt	Typically contains extra and third party software.
/proc	A virtual file system containing information about system resources.
/root	root users home dir.
/sbin	Programs for use by the system and the system administrator.
/tmp	Temporary space for use by the system, cleaned upon reboot.
/usr	Programs, libraries, documentation etc. for all user-related programs.
/var	Storage for all variable files and temporary files created by users, such as log files, mail queue, print spooler. Web servers, Databases etc.

### Linux Interesting Files / Dir’s

Places that are worth a look if you are attempting to privilege escalate / perform post exploitation.
/etc/passwd	Contains local Linux users.
/etc/shadow	Contains local account password hashes.
/etc/group	Contains local account groups.
/etc/init.d/	Contains service init script – worth a look to see whats installed.
/etc/hostname	System hostname.
/etc/network/interfaces	Network interfaces.
/etc/resolv.conf	System DNS servers.
/etc/profile	System environment variables.
~/.ssh/	SSH keys.
~/.bash_history	Users bash history log.
/var/log/	Linux system log files are typically stored here.
/var/adm/	UNIX system log files are typically stored here.
/var/log/apache2/access.log
/var/log/httpd/access.log	Apache access log file typical path.
/etc/fstab	File system mounts.
