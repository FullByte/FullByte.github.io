# Linux

## Application Shortcuts

- System: `/usr/share/applications/`
- System: `/usr/local/share/applications/`
- Flatpak: `/var/lib/flatpak/exports/share/applications/`
- Snap: `/var/lib/snapd/desktop/applications/`
- Local: `~/.local/share/applications/`

## Permissions

Type `chmod xxx <filename>` to change permissions where `xxx` is the numerical code from the table below.

``` txt
Explaination of the Codes: .      ...                 ...                 ...
                           (type) (user persmissions) (group permissions) (world permissions)
```

The first item can be `d` (a directory), `-` (a regular file) or `l` (a symbolic link).  
The following three triplets specify permissons for the `user`, `group` and `world` in that order.  
In each tripplet, permissions can be `r` (read), `w` (write), `x` (execute) or `-` (not assigned).  
Setting permissions can be done via numbers: `r=4`, `w=2`, `x=1` and `-=0`.  

| Setting      | Code | Use Case                                                                                                                                    |
|--------------|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `----------` | 000  | Locking even yourself out. Use `chmod` again, if this happens.                                                                              |
| `-r--------` | 400  | An auto-generated password file (e.g. `~/.google_authenticator`).                                                                           |
| `-rw-------` | 600  | Owner can read and write, everyone else has no access. `~/.history`, all the ssh keys in your `~/.ssh` folder.                              |
| `-rwx------` | 700  | Owner has full access, no one else has access. Your `~/.ssh` folder.                                                                        |
| `-r--r--r--` | 444  | A textfile, that others should see as well, but nobody should modify it.                                                                    |
| `-r-xr-xr-x` | 555  | A folder, that others should be able to `cd` into as well, but nobody should modify it.                                                     |
| `-rw-r--r--` | 644  | Owner can read and write, everyone else can read.                                                                                           |
| `-rw-rw-rw-` | 666  | All users can read and write but not execute.                                                                                               |
| `-rwxr-xr-x` | 755  | Owner has full access, others can read and execute the file. Files and folders you want other people to *see*.                              |
| `-rwxrwxrwx` | 777  | No restriction, global WRX any user can do anything. Files and folders you want other people to *see and modify*. The most open permission. |

Permissions on directory have the following meaning:  
The read bit allows to list the files within the directory.  
The write bit allows to create, rename, or delete files within the directory, and modify the directory's attributes.  
The execute bit allows to enter the directory, and access files and directories inside.  

To view permissions as numerical code: `stat -c %a <filename>`.

What does `s` mean? (click to expand)
"s", like "x", means something different for directories and regular files.

For files, "x" means "executable" of course. For directories, it means "searchable." Without "x" permission on a directory, you can't set it to be your current directory, or get any of the file information like size, permissions, or inode number, so that you effectively can't access any of the files. If a directory has no "r" permission, you can't get a listing, but if you know a file is there, you can still access the file.

Now "s", for files, means "setuid exec." If a file has s permission, then it's executable, and furthermore, the user id and/or group id of the process is set to the user or group id of the owner of the file, depending on whether it's the user or group "s" that's set. This is a way to give limited root powers to a user -- a program that runs as root when an ordinary user executes it. For example, the "passwd" program, which can change otherwise write-protected files on behalf of a user, works this way: it's owned by the "bin" group (generally) and has g+s so that it can write to /etc/passwd and/or /etc/opasswd which are also owned by group "bin."

For directories, "s" means "sticky". If a directory has "s", then the owner and/or group of any files put into the directory are set to the owner/group of the directory. This is often used on CVS repositories, so that the files in the repository end up all owned by the same person and/or group, even though they're put in by different people. I use g+s on all the CVS repositories I set up.

## File System

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

### Interesting files and directories

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

``` sh
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

## Linux Tools

### Pimp Linux

#### Themes/GUI

- gnome extension: <https://github.com/Schneegans/Burn-My-Windows> or <https://extensions.gnome.org/extension/4679/burn-my-windows/>
- NeXTSTEP-like desktop environment for Linux: <https://github.com/trunkmaster/nextspace>
- 1995 Microsoft OS GUI for Linux: <https://github.com/grassmunk/Chicago95>

#### Virtulize, Emnulate and Port

- DOS for Linux: <https://github.com/dosemu2/dosemu2>
- Wine for Windows applications on Linux: <https://www.winehq.org/>

### Alternatives

| original     | alternative                                                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ack          | [ag](https://github.com/ggreer/the_silver_searcher)                                                                                                                                                                                                                                                                                  |
| cat          | [bat](https://github.com/sharkdp/bat)                                                                                                                                                                                                                                                                                                |
| cd           | [zoxide](https://github.com/ajeetdsouza/zoxide)                                                                                                                                                                                                                                                                                      |
| curl         | [curlie](https://github.com/rs/curlie)                                                                                                                                                                                                                                                                                               |
| curl         | [curlx](https://github.com/shivkanthb/curlx)                                                                                                                                                                                                                                                                                         |
| cut          | [choose](https://github.com/theryangeary/choose)                                                                                                                                                                                                                                                                                     |
| diff         | git + [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy), [delta](https://github.com/dandavison/delta), [diffoscope](https://diffoscope.org/), [icdiff](https://github.com/jeffkaufman/icdiff)                                                                                                                               |
| dig          | [dog](https://github.com/ogham/dog)                                                                                                                                                                                                                                                                                                  |
| du           | [duf](https://github.com/muesli/duf), [dust](https://github.com/bootandy/dust), [space-hogs](https://www.npmjs.com/package/space-hogs)                                                                                                                                                                                               |
| find         | [fd](https://github.com/sharkdp/fd)                                                                                                                                                                                                                                                                                                  |
| grep         | [ripgrep](https://github.com/BurntSushi/ripgrep), [ugrep](https://github.com/Genivia/ugrep), [sift](https://github.com/svent/sift), [fselect](https://github.com/jhspetersson/fselect)                                                                                                                                               |
| history      | [mcfly](https://github.com/cantino/mcfly)                                                                                                                                                                                                                                                                                            |
| locate       | [plocate](https://git.sesse.net/?p=plocate)                                                                                                                                                                                                                                                                                          |
| ls           | [exa](https://github.com/ogham/exa), [lsd](https://github.com/Peltoche/lsd)                                                                                                                                                                                                                                                          |
| man          | [tldr](https://github.com/tldr-pages/tldr), [cheet](https://github.com/cheat/cheat)                                                                                                                                                                                                                                                  |
| ping         | [gping](https://github.com/orf/gping), [prettyping](https://github.com/denilsonsa/prettyping)                                                                                                                                                                                                                                        |
| ps           | [procs](https://github.com/dalance/procs)                                                                                                                                                                                                                                                                                            |
| sed          | [sd](https://github.com/chmln/sd)                                                                                                                                                                                                                                                                                                    |
| tar          | [asar](https://github.com/electron/asar)                                                                                                                                                                                                                                                                                             |
| top          | [btop](https://github.com/aristocratos/btop), [gtop](https://github.com/aksakalli/gtop), [htop](https://github.com/htop-dev/htop/), [tiptop](https://github.com/nschloe/tiptop), [bottom](https://github.com/ClementTsang/bottom), [glances](https://github.com/nicolargo/glances), [bpytop](https://github.com/aristocratos/bpytop) |
| tree         | [broot](https://github.com/Canop/broot)                                                                                                                                                                                                                                                                                              |
| sort \| uniq | [huniq](https://github.com/koraa/huniq)                                                                                                                                                                                                                                                                                              |

### JSON

- view json with [fx](https://github.com/antonmedv/fx)
- [jq](https://github.com/stedolan/jq) is a JSON processor

### Other

- [bandwhich](https://github.com/imsnif/bandwhich) is a terminal bandwidth utilization tool
- [bmon](https://github.com/tgraf/bmon) is a bandwidth monitor and rate estimator.
- [bv](http://www.ivarch.com/programs/pv.shtml) is a terminal-based tool for monitoring the progress of data through a pipeline.
- [colorls](https://github.com/athityakumar/colorls) beautifies the terminal's ls command, with color and font-awesome icons.
- [fuck](https://github.com/nvbn/thefuck) correct previously failed command inputs.
- [fzf](https://github.com/junegunn/fzf) is a command-line fuzzy finder.
- [hexyl](https://github.com/sharkdp/hexyl) is a hex viewer.
- [httpie](https://github.com/httpie/httpie) is a command-line HTTP client for the API era.
- [hyperfine](https://github.com/sharkdp/hyperfine) is a command-line benchmarking tool.
- [loop](https://github.com/Miserlou/Loop) is UNIX's missing `loop` command.
- [nnn](https://github.com/jarun/nnn) is a commandline file manager.
- [pathpicker](https://github.com/facebook/PathPicker) (fpp) accepts a wide range of input and presents you with a nice UI to select which files you're interested in.  
- [starship](https://github.com/starship/starship) creates a customizable prompt for any shell.
- [tokei](https://github.com/XAMPPRocky/tokei) counts your code quickly and presents stats.
- [viu](https://github.com/atanunq/viu) allows you to view images in the terminal.
- [watchexec](https://github.com/watchexec/watchexec) executes commands in response to file modifications.
- [xd](https://github.com/ducaale/xh) is a tool for sending HTTP requests.

### Apps

- Mail: <https://www.claws-mail.org>

## Bash

``` txt
             _._
         _.-'   '-._
     _.-'           '-._
 _.-'                   '-._
|                        _,-|
|                    _,-'+++|
|                _,-'+++++++|
|             ,-'+++++++++++|
|             |++++ ++++++++|
|             |+++   +++++++|
|             |++  +++++++++|
|             |++++  +++**++|
|             |++   ++**++++|
'-,_          |+++ ++++++_,-'
    '-,_      |++++++_,-'
        '-,_  |++_,-'
            '-|-'
```

Most commands listed here will work on any linux distributions but if in doubt it will most likely run on the latest Ubuntu.

Some great helpers:

- Understand commands: <https://explainshell.com/>
- ShellCheck gives warnings and suggestions for bash/sh shell scripts: <https://github.com/koalaman/shellcheck>
- Cheat sheets: <http://cht.sh/>

### Basics

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
- List all open ports: ```netstat -atun```

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

### Script Snippets

``` txt
              ___       ___        ___
             ####      ####       ####
            ####      ####       ####
      _____####______####___    ####
     #######################   ####
    #######################   ####
        ####      ####       ####
       ####      ####       ####
  ____####______####____   ####
 #######################  ####
#######################  ___
   ####      ####       ####
  ####      ####       ####
 ####      ####       ####
```

Encoding

- Base64: ```echo -n '12345678:abcdefg' | base64```

Gzip

- Backup: ```tar -cf archive-1.tar "dir-with-content"```
- Compress: ```gzip -9 -f -k archive-1.tar```
- Extract: ```gzip -d -f -k archive-1.tar.gz```

Replace string

``` sh
find . -type f -exec sed -i 's/STRING GOES HERE/REPLACEMENT HERE/g' {} +
find . -type f -exec sed -i 's|Click \[here\](/here/)!|Click HERE!|g' {} +
```

Infinite loop one-liner

``` sh
while true; do echo 'Inside the loop'; sleep 5; done
```

Repeat a key every second

``` sh
while true; do xdotool key F5; sleep 1; done
```

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

#### Bash profiling

Execute these lines in a shell, or put them at the top of your bash script:

``` sh
set -x
PS4='+ $EPOCHREALTIME ($LINENO) '
```

Now, every time you execute a command or script, you will see a timestamp, line number, and command/script executed.

``` sh
export A=1
# + 1608294433.986333 (3) export A=1
# + 1608294433.986378 (3) A=1

export B=2
# + 1608294439.100780 (4) export B=2
# + 1608294439.100807 (4) B=2

[ "$A" == "$B" ] && echo 'Equal' || echo 'Not Equal' && false
# + 1608294491.748071 (5) '[' 1 == 2 ']'
# + 1608294491.748115 (5) echo 'Not Equal'
# Not Equal
# + 1608294491.748200 (5) false
```

### bashrc

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

#### last 10 commands that ran in the current directory

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

### System Information

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

### Disk Stuff

**DD:** low-level data dumping utility

- burning an ISO image to USB stick is just one command away: ```sudo dd if=ubuntu-18.04.1-desktop-amd64.iso of=/dev/sdb bs=1M```
- hard wipe a disk: ```sudo dd if=/dev/zero of=/dev/sda```

**DU:** Disk usage command is used for quickly estimating the drive space used in a folder or partition

- Show files and sort by size: ```/data/java$ du -sh * | sort -h```

**DF:** Used for estimating disk space but for the entire disk rather than a directory or folder.

- show which partition is how much full: ```df -h```

### MORE STUFF

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

### VIM

To make a default Vim installation more useful, type the following 5 lines into its .vimrc file:

``` sh
set hls ic is nu noswf
```

### Screen

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

### tmux

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

### Work with a file

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

### Validate

- Valid IPv4 Address: ```grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"```
- Valid IPv4 CIDR Range: ```grep -E -o "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))"```
- Valid IPv6 Address: ```grep -E -o "^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*"```
- Valid IPv4 CIDR Range: ```grep -E -o "^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))"```
- Valid Hostname: ```grep -E -o "^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9-]*[A-Za-z0-9])"```
- Regex Escape String: ```sed -E 's/([\.\\\+\*\?\[\^\]\$\(\)\{\}\=\!\<\>\|\:\-\#])/\\1/'```
- Regex Base64: ```sed -E '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}\=|[A-Za-z0-9+/]{3}=)?$'```
- Credit Card Numbers: ```grep -E -o "(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)```
- Email Addresses: ```grep -E -o "(([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)(\s*;\s*|\s*$))*```
- Grab Everything Before the First Comma ```grep -E -o "^.[^,]*(?=(\,))```
- Filenames```grep -E -o "[^\\\/:*?"<>|\r\n]+$```
- Hash - MD5 ```grep -E -o "[a-fA-F0-9]{32}```
- Hash - SHA1 ```grep -E -o "[a-fA-F0-9]{40}```
- Hash - SHA256 ```grep -E -o "[a-fA-F0-9]{64}```
- Hash - SHA512 ```grep -E -o "[a-fA-F0-9]{128}```
- Hex ```grep -E -o "/^#?([a-f0-9]{6}|[a-f0-9]{3})$/```
- Phone Numbers ```grep -E -o "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$```
- MAC Address ```grep -E -o "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$```
- URLs ```grep -E -o "(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)```
- Valid URLs ```grep -E -o "\b((ht|f)tp(s)?:\/\/|www\.)+[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9]{2,}((\/)?([-a-zA-Z0-9@:%_\+.~#?&\/=]*)?)\b```
- US Social Security Numbers ```grep -E -o "^(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}$```

### Network Stuff

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

#### DNS

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

### Fun Stuff

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

### Other Stuff

- Reboot: ```init 6```
- Compile C code: ```gcc -o output.c input.c```
- Compile 32 bit binary on 64 bit Linux: ```gcc -m32 -o output.c input.c```
- Disable bash history logging: ```unset HISTORYFILE```
- Connect to RDP server from Linux.```rdesktop X.X.X.X```
- Kill current session: ```kill -9 $$```
- Clear bash history: ```cat /dev/null > ~/.bash_history```
- one-time table: ```for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $iÃ—$j=$((i*j))\\t;done; echo;done```
