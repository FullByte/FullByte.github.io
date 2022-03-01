# Overview

## Copy Files

There are many ways to copy files. Currently the best way for me (depending on source and destiation) are the following (assuming source is my computer):

| Destination         | Tool                                                                                                | Comment                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Cloud               | [rclone](https://rclone.org/)                                                                       | Encryption possible, no client needed, many vendors supported                                      |
| Local USB-drive/NAS | [RoboCopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocop) | Already installed, has sync option, works.                                                         |
| FTP/WebDAV/etc.     | [WinSCP](https://winscp.net)                                                                        | Scripting possible using winscp.com                                                                |
| Remote PC/NAS       | [Syncthing](https://syncthing.net/)                                                                 | Use [SyncTrayzor](https://github.com/canton7/SyncTrayzor) for GUI and sync files via peer-to-peer. |
| Server Backup       | [Restic](https://restic.net/)                                                                       | Good for regular backups. Uses rclone in the backend.                                              |

## Convert Files

todo
