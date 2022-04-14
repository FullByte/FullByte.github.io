# Bash

Most commands listed here will work on any linux distributions but if in doubt it will most likely run on the latest Ubuntu.

Some great helpers:

- Understand commands: <https://explainshell.com/>
- ShellCheck gives warnings and suggestions for bash/sh shell scripts: <https://github.com/koalaman/shellcheck>

## Basics

Random basics

- Show all files: ```ls -halt```
- Check installed packges: ```sudo tasksel```
- Update and upgrade: ```sudo apt update && apt -y full-upgrade && apt -y autoremove```
- Upgrading to a newer release: ```do-release-upgrade```
- Check who is online: ```w```
- Show all system users: ```cut -d: -f1 /etc/passwd```
- Save to file: ```ls -halt > result.txt```
- Append to file: ```echo "add this" >> existing-file.txt```
- Pipe output e.g. to trash (to not see it): ```grep "stuff" 2> /dev/null```
- Change owner of file or dir: ```chown user:group blah```
- Change owner of file or dir recersive for all folders below: ```chown -R user:group blah```
- Change file / dir permissions: ```chmod 600 file```

Chain commands:

- Pipe the output of command1 to command2: ```<command1> | <command2>```
- Execute command2 after command1: ```<command1> ; <command2>```
- Execute command2 if command1 succeded: ```<command1> && <command2>```
- Redirect errors of command1 to file1: ```<command1> 2> <file1>```
- Redirect standard and error output of command1 to file1 ```<command1> &> <file1>```

Cursor

| Command | Description                         |
|---------|-------------------------------------|
| Ctrl+A  | Jump to beginning.                  |
| Ctrl+E  | Jump to end.                        |
| Ctrl+W  | Delete one word left of the cursor. |
| Ctrl+U  | Delete entire line.                 |
| Ctrl+Y  | Paste back what you just deleted.   |

## script snippets

Check if root

``` sh
if [ "$EUID" -ne 0 ]; then
    echo "You need to run this script as root"
    exit 1
fi
```

Check path

``` sh
if [ "$PWD" != "$HOME" ]; then
    echo "You need to run this script from your home directory $HOME"
    exit 1
fi
```

Check virtualization platform (openvz)

``` sh
if [ "$(systemd-detect-virt)" == "openvz" ]; then
    echo "OpenVZ is not supported"
    exit
fi
```

Check virtualization platform (lxc)

``` sh
if [ "$(systemd-detect-virt)" == "lxc" ]; then
    echo "LXC is not supported."
    exit
fi
```

Minimal safe Bash script template [based this blog](https://betterdev.blog/minimal-safe-bash-script-template/):

``` sh
#!/usr/bin/env bash

set -Eeuo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1

trap cleanup SIGINT SIGTERM ERR EXIT

usage() {
  cat <<EOF
Usage: $(basename "$0") [-h] [-v] [-f] -p param_value arg1 [arg2...]
Script description here.
Available options:
-h, --help      Print this help and exit
-v, --verbose   Print script debug info
-f, --flag      Some flag description
-p, --param     Some param description
EOF
  exit
}

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOCOLOR='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOCOLOR='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

msg() {
  echo >&2 -e "${1-}"
}

die() {
  local msg=$1
  local code=${2-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help)
      usage
      ;;
    -v | --verbose)
      set -x
      ;;
    --no-color)
      NO_COLOR=1
      ;;
    -f | --flag) # example flag
      flag=1
      ;;
    -p | --param) # example named parameter
      param="${2-}"
      shift
      ;;
    -?*)
      die "Unknown option: $1"
      ;;
    *)
      break
      ;;
    esac
    shift
  done

  args=("$@")

  # check required params and arguments
  [[ -z "${param-}" ]] && die "Missing required parameter: param"
  [[ ${#args[@]} -eq 0 ]] && die "Missing script arguments"

  return 0
}

parse_params "$@"
setup_colors

# script logic here

msg "${RED}Read parameters:${NOCOLOR}"
msg "- flag: ${flag}"
msg "- param: ${param}"
msg "- arguments: ${args[*]-}"
```

## bashrc

Paste these function in the ~/.bashrc file.

Make a new folder and cd into it

- Usage: mkcd name1
- Code: ```mkcd(){ NAME=$1; mkdir -p "$NAME"; cd "$NAME"; }```

Alias

- Count files in directory: ```alias fcount='ls -1 | wc -l'```
- Disable "Save workspace" promt when closing R: ```alias R='R --no-save'```
- Tweak df: ```alias df='df -h'```
- Tweak du: ```alias du='du -h'```
- Using Exa instead of ls

    ``` sh
    alias l='exa'
    alias la='exa -a'
    alias ll='exa -lah'
    alias ls='exa --color=auto'
    ```

More:

- Finding out which linux you are using: uname -m && cat /etc/*release
- Bulk renaming of files: rename 's/ch0/ch/gi' *.tiff

### last 10 commands that ran in the current directory

Add this function to your `.bashrc`

``` sh title=".bashrc"
function addhistory() {
    echo "${1%%$'\n'}|${PWD}   " >> ~/.history_ext
}
```

Create file e.g. `folderhistory` with the content below and add it to your `$PATH`

``` sh title="folderhistory"
grep -v "folderhistory" ~/.history_ext | grep -a --color=never "${PWD}   " | cut -f1 -d"|" | tail
```

Source: <https://github.com/natethinks/jog>

## System Information

Get system details

- Get all environment variables: ```printenv```
- Get all configuration variables: ```getconf -a```
- Show ports/connections open: ```lsof```
- Get ubuntu version: ```lsb_release -r```
- Free disk space: ```df -h```

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

History

Press `Ctrl+R` to search through your history using auto-complete. Press `Ctrl+R` again and it will cycle though the other auto-completion options. Press `Enter` and the command will execute. Press `←`,`→` to edit commands.

- Location of history file: ```echo $HISTFILE```
- Clear the history of current shell: ```history -c```
- Overwrite the history file with the current shell's history: ```history -c | history -w | exit```
- Delete first 15 entries: ```for i in {1..15}; do history -d 1; done```
- Clear history completly: ```ln -sf /dev/null ~/.bash_history && history -c && exit```
- Disable history: ```sudo echo "unset HISTFILE" >> /etc/profile```
- Disable history for user "0xfab1": ```echo "unset HISTFILE" >> /home/0xfab1/.bash_profile```
- Change number of lines stored in an ongoing history list session: ```echo "HISTFILESIZE=10 >> ~/.bashrc```
- Change amount of lines used for the history stack when it’s written to the history file: ```echo "HISTSIZE=0 >> ~/.bashrc```
- Top commands used: ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -nr```
- Commands only used once: ```history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -n | grep ' 1 '```

More...

- List open file descriptors (-i flag for network interfaces): ```lsof -i :8080```
- Stream current disk, network, CPU activity, etc: ```dstat -a```
- Trace system calls of a program: ```strace -f -e <syscall> <cmd>```
- Print currently active processes: ``` ps1 aux | head -n20```
- Visualize process forks: ``` ps1tree```
- Show size on disk for directories and their contents: ```du -ha```
- List currently open Internet/UNIX sockets and related information```netstat | head -n20```
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
- Kill Everything Running On A Certain Port```sudo kill "sudo lsof -t -i:3000"```
- See if the http status of the request changes: ```watch -d curl -LIs localhost:3000```
- Update access and modify time: ```touch README.md```
- Update access time: ```touch -a README.md```
- Update modify time: ```touch -m README.md```
- Show The Size Of Everything In A Directory```ls | xargs du -sh```
- Saying Yes: ```yes | rm -r ~/some/dir```
- Show Disk Usage For The Current Directory: ```du -h | sort -nr```

## VIM

To make a default Vim installation more useful, type the following 5 lines into its .vimrc file:

``` sh
set hls ic is nu noswf
```

## Screen

| Command               | Description                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------|
| screen                | Create a new session.                                                                     |
| Ctrl+A,D              | Detach from current screen session.                                                       |
| Ctrl+D                | End current session. Similart to `exit`.                                                  |
| screen -r             | Reattach to session.                                                                      |
| screen -ls            | List all sessions.                                                                        |
| screen -S `<name>` -L | Create a new screen session `<name>` with logging enabled.                                |
| screen -r `<name>`    | Reattach to session with `<name>` if there are multiple ones.                             |
| screen -rx `<name>`   | Attach to session that is already attached.                                               |
| Ctrl+A, Esc           | Enter scroll mode. Use ↑ and ↓ or Pg Up and Pg Dn to scroll. Hit Esc to exit scroll mode. |

## tmux

create a new tmux session

``` sh
tmux
```

or create a new session with a name e.g. "SessionName"

``` sh
tmux new-session -sSessionName
```

Use these commands to navigate between windows:

- Control + B + N next session
- Control + B + C new session

Join a tmux session (e.g. from a different device or user)

``` sh
tmux attach
```

or be specific:

``` sh
tmux attach-sesssion -t SessionName
```

Kill first window (0):

``` sh
tmux kill-window -t 0
```

Kill a session:

``` sh
tmux kill-session
```

## Work with a file

- Cat A File With Line Numbers: ```cat -n file```
- Line count in a file: ```wc -l <file>```
- Count unique words in a file: ```cat file.txt | xargs -n1 | sort | uniq -c```
- Display contents of a zipped text file: ```zcat <file.gz>```
- Copy a file from remote to local server, or vice versa: ```scp <user@remote_host> <local_path>```
- List Stats For A File: ```stat -x README.md```
- Securely Remove Files```srm -vz README.md``` or ``` shred -uvz -n 5 README.md```
- Securely Remove Files after rm was used: ```sfill -lvz /home```
- Copying File Contents To System Paste Buffer: ```cat some-file.txt | pbcopy```
- Exclude A Directory With Find: ```find . -type f -not -path './.git/*' -ctime -10```
- File Type Info With File: ```file data.txt```
- Find Newer Files than this file: ```find blog -name '*.md' -newer blog/first-post.md```
- Get The Unix Timestamp: ```date +%s```
- Hexdump A Compiled File: ```cat Hello.class | hexdump -C```
- Grep For Files Without A Match: ```grep -L "foobar" ./*```
- Grep For Files With Multiple Matches: ```grep -rl "match1" src/css | xargs grep -l "match2"```
- Add "new entry" in line 13 of file "file.txt": ```sed -n -i 'p;13a new entry' file.txt```
- Remove lines under n (e.g. 6) characters: ```sed -E '/^.{,6}$/d' /path/to/input/file > /path/to/output/file``` or ```gsed -E '/^.{,6}$/d' /path/to/input/file > /path/to/output/file```
- Sort Alphabetically and Remove Duplicates: ```sort -us -o /path/to/output/file /path/to/input/file``` or ```bash -c "LC_ALL='C' gsort -us -o /path/to/output/file /path/to/input/file"```

## Validate

- Valid IPv4 Address: ```grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"```
- Valid IPv4 CIDR Range: ```grep -E -o "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))"```
- Valid IPv6 Address: ```grep -E -o "^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*"```
- Valid IPv4 CIDR Range: ```grep -E -o "^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))"```
- Valid Hostname: ```grep -E -o "^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9-]*[A-Za-z0-9])"```
- Regex Escape String: ```sed -E 's/([\.\\\+\*\?\[\^\]\$\(\)\{\}\=\!\<\>\|\:\-\#])/\\1/'```

## Network Stuff

- Find Device in Monitoring Mode: ```iwconfig 2>/dev/null | grep "Mode\\:Monitor" | awk '{print $1}'```
- Find Access Point: ```iwconfig 2>&1 | sed -n -e 's/^.\*Access Point: //p'```
- Linux IPv6 search devices in local network: ```ping6 -c 2 -I en0 -w ff02::1```
- Show Linux network ports with process ID’s (PIDs): ```netstat -tulpn```
- Watch TCP, UDP open ports in real time with socket summary: ```watch ss -stplu```
- Show established connections: ```lsof -i```
- Change MAC address: ```macchanger -m MACADDR INTR```
- Change MAC address using ifconfig: ```ifconfig eth0 hw ether MACADDR```
- Get hostname for IP address```nbtstat -A x.x.x.x```
- Block access to e.g. "google.com" from the host machine```tcpkill -9 host google.com```
- Enable IP forwarding: ```echo "1" > /proc/sys/net/ipv4/ip_forward```
- Change DNS to 1.1.1.1: ```echo "1.1.1.1" > /etc/resolv.conf```
- Nmap scan every interface that is assigned an IP: ```ifconfig -a | grep -Po '\b(?!255)(?:\d{1,3}\.){3}(?!255)\d{1,3}\b' | xargs nmap -A -p0-```
- Extract your external IP address using dig: ```dig +short myip.opendns.com @resolver1.opendns.com```

### DNS

Simple DNS performance check:

``` sh
TIMEFORMAT=%R && (time dig @8.8.8.8 0xfab1.net) 2>&1 > /dev/null
```

Simple DNS performance check with loop through DNS list "dns.txt"

``` sh
for dns in `cat dns.txt`; do echo -n $dns: && TIMEFORMAT=%R && (time dig @$dns 0xfab1.net) 2>&1 > /dev/null; done
```

dns.txt could look like this:

``` txt title="dns.txt"
1.1.1.1
8.8.8.8
9.9.9.9
```

Loop through DNS list and check website 10x

``` sh
TIMEFORMAT=%R && for dns in `cat dns.txt`; do (for i in {1..10}; do (echo -n $dns: && (time dig @$dns 0xfab1.net) 2>&1 > /dev/null); done); done
```

## Fun Stuff

Entertaining nonsense:

- Loop Train: ```for i in {1..10}; do sl; done```

Alternatives for `tree` command:

-```ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//──/g' -e 's/─/├/' -e '$s/├/└/'```
-```find . -not -path '*/\.*' | python -c "import sys as s;s.a=[];[setattr(s,'a',list(filter(lambda p: c.startswith(p+'/'),s.a)))or (s.stdout.write('  '*len(s.a)+c[len(s.a[-1])+1 if s.a else 0:])or True) and s.a.append(c[:-1]) for c in s.stdin]"```

If you don't have `tree` maybe create an as such: `alias tree='command from above here'`

Display all terminal colors

``` sh
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

[Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) simulation

``` sh
echo -ne "\033#8";X=`tput cols`;Y=`tput lines`;((a=$X/2));((b=$Y/2));d=1;while case $d in 0)((a=a<2?X:a-1));;1)((b=b<2?Y:b-1));;2)((a=a==X?1:a+1));;3)((b=b==Y?1:b+1));; esac;do ((c=b+a*X));v=${k[c]:- };[ $v. = @. ]&&{((d=d>2?0:d+1));k[c]="";}||{(( d=d<1?3:d-1));k[c]=@;};echo -ne "\033[$b;${a}H$v";done
```

## Other

- Reboot: ```init 6```
- Compile C code: ```gcc -o output.c input.c```
- Compile 32 bit binary on 64 bit Linux: ```gcc -m32 -o output.c input.c```
- Disable bash history logging: ```unset HISTORYFILE```
- Connect to RDP server from Linux.```rdesktop X.X.X.X```
- Kill current session: ```kill -9 $$```
- Clear bash history: ```cat /dev/null > ~/.bash_history```
- one-time table: ```for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $iÃ—$j=$((i*j))\\t;done; echo;done```
