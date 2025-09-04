# mRemoteNG

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## OpenSSH

Use [OpenSSH](https://github.com/PowerShell/Win32-OpenSSH/releases) instead of [PuTTYNG](https://github.com/mRemoteNG/PuTTYNG) to SSH with mRemoteNG like a pro.

Create a new external program with the following parameters:

- Name: OpenSSH
- Path: c:\program files\PowerShell\7\pwsh.exe
- Parameter: -c "ssh %USERNAME%@%HOSTNAME%"
- Working directory: $env:USERPROFILE

Then select "external Program" for your connection and choose "OpenSSH".

![mRemoteNG](_mRemoteNG.png)
