# Power user

## Windows

### Download Files

| Destination | Tool                                             | Comment |
| ----------- | ------------------------------------------------ | ------- |
| Videos      | [yt-dlp](https://github.com/yt-dlp/yt-dlp)       |         |
| Torrents    | [qbittorrent](https://www.qbittorrent.org/)      |         |
| IRC XDCC    | [mirc](https://www.mirc.com/)                    |         |
| Gallery     | [gallery-dl](https://github.com/mikf/gallery-dl) |         |
| Files       | [wget](https://ftp.gnu.org/gnu/wget/)            |         |

### Copy Files

There are many ways to copy files. Currently the best way for me (depending on source and destiation) are the following (assuming source is my computer):

| Destination         | Tool                                                                                                 | Comment                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Cloud               | [rclone](https://rclone.org/)                                                                        | Encryption possible, no client needed, many vendors supported                                      |
| Local drive/NAS | [RoboCopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) | Already installed, has sync option, works.                                                         |
| SFTP/WebDAV     | [WinSCP](https://winscp.net)                                                                         | Scripting possible using winscp.com                                                                |
| Sync       | [Syncthing](https://syncthing.net/)                                                                  | Use [SyncTrayzor](https://github.com/canton7/SyncTrayzor) for GUI and sync files via peer-to-peer. |
| Backup       | [Restic](https://restic.net/)                                                                        | Good for regular backups. Uses rclone in the backend.                                              |

### Convert Files

| Destination | Tool                                   | Comment |
| ----------- | -------------------------------------- | ------- |
| Text        | [Pandoc](https://pandoc.org/)          |         |
| Video       | [FFmpeg](https://ffmpeg.org/)          |         |
| Audio       | [FFmpeg](https://ffmpeg.org/)          |         |
| Pictures    | [ImageMagick](https://imagemagick.org) |         |
| eBooks      | [Calibre](https://calibre-ebook.com/)  |         |
