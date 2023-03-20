# SCP

## File-Transfer with SCP

Copying file to host:

``` sh
scp SourceFile user@host:~/TargetFile
```

Copying file from host and copying folder from host (with -r switch):

``` sh
scp user@host:~/remotefolder .
scp -r user@host:~/remotefolder TargetFolder
```

Note that if the remote host uses a port other than the default of 22, it can be specified in the command. For example, copying a file from host:

``` sh
scp -P 666 user@host:directory/SourceFile TargetFile
```

## WinSCP

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

### Connect OneDrive over WebDAV

- After you log in to your OneDrive account, your URL should be like: <https://onedrive.live.com/?id=root&cid=ABCDEFGHIJKLMNOP>. The ABCDEFGHIJKLMNOP part is your "customer ID". Select it and copy it to the clipboard.
- Start WinSCP and create a new Login/New site node
- On the New site node, select WebDAV protocol and TLS/SSL Implicit encryption.
- Enter d.docs.live.net into the Host name box.
- Enter your Microsoft account credentials. If you have 2FA enabled, [create new app password](https://account.live.com/proofs/Manage/additional#AppPassword) and use this for the password box.
- Press the Advanced button to open Advanced site settings dialog and go to Environment > Directories page.
- Paste your "OneDrive customer ID" into the Remote directory box and add a slash in front of it, i.e. like /ABCDEFGHIJKLMNOP.

### Script

In a commmand prompt run `winscp.com` and login to a session. It is also possible to pass on all commands directly or attach a script with all commands.

#### Basic Examples

Save this [script](https://winscp.net/eng/docs/scripting) to a file (e.g. WinSCPWebDAVExample.txt)

``` txt
open https://username@webdav.domain.com/
put copythisfile.txt /path/destination/
exit
```

Run the scirpt with WinSCP like this:

``` sh
winscp.com /script=WinSCPWebDAVExample.txt
```

You can also run this example as a one-liner as follows:

``` sh
winscp.com /command "open https://username@webdav.domain.com/" "put copythisfile.txt /path/destination/" "exit"
```

#### My settings

I trigger winscp.com in a batch file as follows:

```bat
@echo off
winscp.com /rawconfig Interface\SynchronizeParams=4096 /ini=nul /script=myscript.txt
```

- `/rawconfig Interface\SynchronizeParams=4096` [enables mirror mode](https://winscp.net/eng/docs/rawconfig) when using [synchronize](https://winscp.net/eng/docs/scriptcommand_synchronize). It is possible to set `-mirror` but this didn't work for me.
- Force scripting mode to start with the [default configuration](https://winscp.net/eng/docs/config#no) with `/ini=nul`

My example script file to upload to a WebDAV server:

```scp
# Connect to WebDAV server using a password
open davs://user%40domain.com:password@myfiles.domain.com/

# Settings
option batch on
option confirm off

# Set local dir
lcd "L:\o\c\a\l"

# Set remote dir
cd "/www"

# Sync Files
synchronize remote -delete -mirror "L:\o\c\a\l" "/remote/"

# Exit WinSCP
exit
```
