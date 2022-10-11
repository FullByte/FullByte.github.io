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
