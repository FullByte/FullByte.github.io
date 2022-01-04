# Copy Files

There are many ways to copy files. Currently the best way for me (depending on source and destiation) are the following (assuming source is my computer):

| Destination         | Tool                                                                                                | Comment                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Cloud               | [rclone](https://rclone.org/)                                                                       | Encryption possible, no client needed, many vendors supported                                      |
| Local USB-drive/NAS | [RoboCopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocop) | Already installed, has sync option, works.                                                         |
| FTP/WebDAV/etc.     | [WinSCP](https://winscp.net)                                                                        | Scripting possible using winscp.com                                                                |
| Remote PC/NAS       | [Syncthing](https://syncthing.net/)                                                                 | Use [SyncTrayzor](https://github.com/canton7/SyncTrayzor) for GUI and sync files via peer-to-peer. |
| Server Backup       | [Restic](https://restic.net/)                                                                       | Good for regular backups. Uses rclone in the backend.                                              |

All mentioned tools are described in more detail below.

## curl

| What          | Where                                                                |
|---------------|----------------------------------------------------------------------|
| Official Page | <https://curl.se/>                                                   |
| Source        | <https://github.com/curl/curl>                                       |
| Download      | <https://github.com/curl/curl/releases>                              |
| Docs          | <https://everything.curl.dev> or <https://curl.se/docs/manpage.html> |
| Book          | <https://curl.se/docs/>                                              |
| Windows       |```scoop install curl```                                             |
| Ubuntu        |```apt install curl```                                               |

### Random Examples

Example to check /24 range in abuseipdb.com for the last 3 days

``` sh
curl -s -G https://api.abuseipdb.com/api/v2/check-block --data-urlencode "network=123.123.123.1/24" -d maxAgeInDays=$DAYS -H "Key: apikeyfromabuseipdb.com" -H "Accept: application/json" |jq '.data.reportedAddress'
```

If you want to inspect the headers of a response from some endpoint include the `-I` flag and `curl` will
return just the headers.

``` sh
curl -I localhost:3000/posts
```

Example of using curl with basic auth credentials

``` sh
curl -u username:password staging.example.com
```

Query a website e.g. request a json response from cloudflare-dns.com on TXT records of the domain 0xfab1.net

``` sh
curl -s -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=0xfab1.net&type=TXT'
```

### Send Mail

``` sh
curl --ssl-reqd --url 'smtps://smtp.gmail.com:465' --user 'username@gmail.com:password' --mail-from 'username@gmail.com' --mail-rcpt 'john@example.com' --upload-file mail.txt
```

mail.txt file contents:

``` txt
From: "User Name" <username@gmail.com>
To: "John Smith" <john@example.com>
Subject: This is a test

Hi John,
I’m sending this mail with curl thru my gmail account.
Bye!
```

Some more information:

- [gmail: turn on access for less secure apps](https://myaccount.google.com/lesssecureapps)
- Use [--netrc-file](https://everything.curl.dev/usingcurl/netrc) instead of credentials in curl command
- [Use curl with ssl](https://curl.se/docs/sslcerts.html)

### WebDAV

Create Folders

``` sh
curl -X MKCOL 'http://your.server/uploads/nested_folder1' --user 'name:pwd'
```

Copy Files

``` sh
curl -T <filename> -u <username>:<password> <url> -o /dev/stdout
```

Copy all files in a Folder (and subfolder). Folders must already exist.

``` sh
cd local_folder_to_upload && find . -exec curl -T {} 'http://your.server/uploads/{}' --user 'name:pwd' \;
```

## Wget

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

### Download all files from website

Generally, this can be blocked but works in most cases. To avoid a few things:

- Ignore **robots.txt** blocking the download by using```-e robots=off```
- Add **user-agent**; either one that guarantees a math e.g.```--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"``` or just the one you are using atm e.g.```Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0``` (Firefox: about:config --> devtools.responsive.userAgent)
- **Random service blocks**: Try removing some options as they may the reason access is blocked e.g.```-N``` blocked by AWS S3.
- Adding a **referrer** may help. Figure out what you need by checking why it works in the browser e.g.```wget --referer='http://example.net' http://example.com/```
- Checking the details of the **HTTP status code** you get as an error may help resolve the issue too: <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>
- A required **cookie** or missing **authorization** can be further reasons why the download doesn't work or run though fully.

Example:

``` sh
wget -e robots=off -r -np --page-requisites --convert-links --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" http://example.com/dir/
```

Alternative:

``` sh
wget -e robots=off --verbose --debug --adjust-extension --backup-converted --base=http://example.com/dir/ --no-http-keep-alive --no-parent --mirror http://example.com/dir/
```

### Download specific files types

``` sh
wget -e robots=off -r -A ogg,mp3 http://example.com/dir/ # Specific audio files
wget -e robots=off -r -A png,jpeg,jpg,gif http://example.com/dir/ # Specific Image Files
wget -e robots=off -r -l 3 -np -p  http://example.com/dir/ # All pictures
```

### Download features

In case you are downloading clear text files it may come in handy to preview the download:

``` sh
wget http://0xfab1.net/todo.txt --output-document - | head -n4
```

Continue a partially downloaded file where the download was interrupted with `-c` for continue:

``` sh
wget -c https://0xfab1.net/best-distro2.iso
```

You can copy an entire web page with `--mirror` which is the same as adding parameters `--recursive --level inf --timestamping --no-remove-listing`. When using mirror consider using `--no-cookies --page-requisites --convert-links` as additional parameters:

``` sh
wget --mirror --no-cookies --page-requisites --convert-links http://0xfab1.net
```

Use `--debug` to view HTTP header information of your download request.

``` sh
wget --debug https://0xfab1.net
```

If you want to deal with redirects as error set `--max-redirect 0`. This is also handy if you don't want to follow URL-shorter links:

``` sh
wget --max-redirect 0 "https://bit.ly/0xfab1"
```

## IPFS

Examples using IPFS

| What          | Where                                      |
|---------------|--------------------------------------------|
| Official Page | <https://ipfs.io/>                         |
| Documentation | <https://docs.ipfs.io/>                    |
| Source        | <https://github.com/ipfs>                  |
| Download      | <https://github.com/ipfs/go-ipfs/releases> |

### Find Peers

``` sh
ipfs dht findpeer QmYtQ3iJi5RAQYxWJLts7xN1dRNK2n258QEXk4N1eLMZFM
```

### Share encrypted files with IPFS

create key

``` sh
gpg --gen-key
gpg --export --armor -email > pubkey.asc
```

share and import key

``` sh
gpg --import pubkey.asc
gpg --list-keys
```

share enrypted files

``` sh
ipfs init
gpg --encrypt --recipient "Cory Heath" myriad.pdf
ipfs add myriad.pdf.gpg
```

get encrypted files

``` sh
ipfs get QmYqSCWuzG8cYo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL
gpg --decrypt QmYqSCWUZg8Cyo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL > myriad.pdf
```

### Hosting

For 0xfab1.net I am using [fleek](https://fleek.co/) to host the website on IPFS.

With Fleek you get a fleek adress, the IPDS address and I added a CNAME to make it easy to reach:

- Fleek IPFS: <https://ipfs.fleek.co/ipfs/QmXUY11j72BsYCqURakrfFyVCBjdnNiEcPT7csXN5LRFaJ/>
- IPFS <https://ipfs.io/ipfs/QmXUY11j72BsYCqURakrfFyVCBjdnNiEcPT7csXN5LRFaJ>
- CNAME: <https://ipfs.0xfab1.net/>

List of public gateways: <https://ipfs.github.io/public-gateway-checker/>

## SCP

### File-Transfer with SCP

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

### WinSCP

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

#### Connect OneDrive over WebDAV

- After you log in to your OneDrive accoutn, your URL should be like: https://onedrive.live.com/?id=root&cid=ABCDEFGHIJKLMNOP. The ABCDEFGHIJKLMNOP part is your “customer ID”. Select it and copy it to the clipboard.
- Start WinSCP and create a new Login/New site node
- On the New site node, select WebDAV protocol and TLS/SSL Implicit encryption.
- Enter d.docs.live.net into the Host name box.
- Enter your Microsoft account credentials. If you have 2FA enabled, [create new app password](https://account.live.com/proofs/Manage/additional#AppPassword) and use this for the password box.
- Press the Advanced button to open Advanced site settings dialog and go to Environment > Directories page.
- Paste your “OneDrive customer ID” into the Remote directory box and add a slash in front of it, i.e. like /ABCDEFGHIJKLMNOP.

#### Script

In a commmand prompt run `winscp.com` and login to a session. It is also possible to pass on all commands directly or attach a script with all commands.

**Basic Example:**

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

**My settings**

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

## rclone

rclone is a great tool to backup, copy, sync files to the cloud encrypted and without the client installed on the local machine.

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

### Restore rclone.conf

Run this command to find out where your `rclone.conf` file is.

``` sh
rclone config file
```

If you installed rclone and didn't configure anything yet you will get this information

``` txt
Configuration file doesn't exist, but rclone will use this path:
C:\Users\0xfab1\AppData\Roaming\rclone\rclone.conf
```

else, rclone will repond as follows:

``` txt
Configuration file is stored at:
C:\Users\0xfab1\AppData\Roaming\rclone\rclone.conf
```

Be sure to backup this file so you restore it (overwrite it or partcially update).

If you restore a file you may need to refresh the token(s) you are using.

Run the following command todo so e.g. for connection call "onedrive":

``` sh
rclone config reconnect onedrive:
```

The process will walk though parts of the steps you did whenever you set up this connection. ONce done the connection should work again.

## Restic

Restic is a great tool for backups and uses rclone for various tasks.

| What          | Where                                                           |
|---------------|-----------------------------------------------------------------|
| Official Page | <https://restic.net/>                                           |
| Source        | <https://github.com/restic/restic>                              |
| Install       | <https://restic.readthedocs.io/en/stable/020_installation.html> |

### Examples

TODO

## youtube-dl

Some examples on how to use youtube-dl or ytdlpl to download videos.

| What          | Where                                             |
|---------------|---------------------------------------------------|
| Official Page | <https://youtube-dl.org/>                         |
| Source        | <https://github.com/ytdl-org/youtube-dl>          |
| Download      | <https://github.com/ytdl-org/youtube-dl/releases> |
| Install       | choco install youtube-dl                          |

### Download Video

Download to a specific location in best quality:

``` sh
youtube-dl -f 22 -o 'path' '<youtube-link>'
```

Download with details:

``` sh
youtube-dl -f best --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '<youtube-link>'
```

### Audio only

``` sh
youtube-dl -i --extract-audio --audio-format mp3 --audio-quality 0 '<youtube-link>'
```

### YouTube Playlists

Download a playlist:

``` sh
youtube-dl -best 22 --yes-playlist '<playlist-link'
```

Download a playlist with audio only:

``` sh
youtube-dl -f 22 --yes-playlist '<playlist-link'
```

### Get Video Source Information

Get Source formats available:

``` sh
youtube-dl --list-formats '<youtube-link>'
```

### Script to download audio of playlist

Run ytdlpl (youtube downloader playlist) and add the playlist you want to download.
This script will download the latest youtube-dl version for windows to the current folder if not available.

``` ps1
Function ytdlpl
{
    Param ($playlist)

    # Check and get youtube-dl if required
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = ‘stop’
    try {if(Get-Command youtube-dl){Write-Host("Using youtube-dl version " + (Get-Command youtube-dl).Version + " from source: " + (Get-Command youtube-dl).Source)}}
    catch {Write-Host “youtube-dl not found, downloading to current folder... ”; Invoke-WebRequest -Uri "https://youtube-dl.org/downloads/latest/youtube-dl.exe" -OutFile ((Get-Location).Path + "\youtube-dl.exe")}
    $ErrorActionPreference=$oldPreference

    # Download and rename playlist
    youtube-dl.exe -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -i --extract-audio --audio-format mp3 --audio-quality 2 --yes-playlist "$playlist"
    Set-Location -Path ((Get-Location).Path + "\" + (Get-ChildItem | Sort-Object LastWriteTime | Select-Object -last 1).Name)
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '[^a-zA-Z]', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '\s+', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.Name -replace ' .mp3', '.mp3')}
}
```

Alternatively use this script

``` ps1
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/FullByte/scripts/main/tools/youtubedl/youtube-dl.ps1'))
```

### Extras

#### Alternative fork yt-dlp

Alternative <https://github.com/yt-dlp/yt-dlp>

You can swap yt-dlp with youtube-dl by renaming and not worry about commands fail. If the GUI parses the -F output to give format selection, it could cause a bit of a problem. To fix that, create yt-dlp.conf in the same dir as yt-dlp and put --list-formats-old in it.

#### GUI

[Youtube-dl-gui](https://github.com/oleksis/youtube-dl-gui) is a cross platform front-end GUI of the popular youtube-dl written in wxPython.
