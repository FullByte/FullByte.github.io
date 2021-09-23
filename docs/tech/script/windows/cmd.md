# CMD

More: <https://bytescout.com/blog/windows-command-prompt-commands.html>

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
ipconfig /all 2>&1 
net group "domain admins" /domain 2>&1 
net localgroup administrators 2>&1 
netstat -an 2>&1 & 
systeminfo 2>&1 & 
reg query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" 2>&1 
wmic os get Caption /value | more 2>&1 
schtasks /query /FO List /V | findstr /b /n /c:"Repeat: Every:" 2>&1
```

For are more detailed system info dump run [winPEAS](https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/winPEAS/winPEASbat/winPEAS.bat).

## Robocopy

- Exclude files: ```Robocopy /xd excludethis```
- Ignore hidden files ```Robocopy -s -h```

## Format and Image stuff

### Format FAT32 on >32GB

Use ```diskpart``` to clean the disk (requires Admin)

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

### Get MAC Address of remote PC

Option 1

```shell
net view machinename
nbtstat -a machinename
```

Option 2

```cmd
Ping <IP/machinename>
Arp –a
```

Option 3

```cmd
getmac
```

### Route network traffic

Requests to 10.11.12.13 will be routed via 8.8.8.8:

```cmd
route add 8.8.8.8 MASK 255.255.255.255 10.11.12.13
route print
```

### traceroute

[pathping](https://de.wikipedia.org/wiki/Pathping) (alternative to tracert)

Using ICMP: ```traceroute -I www.microsoft.com```
Using UDP: ```traceroute -U www.microsoft.com```
Using TCP Port 80 (usually allowed by firewalls): ```traceroute -T -p 80 www.microsoft.com```

### Send Message

```cmd
net send /users This is a test message
msg \* /SERVER:localhost /TIME:666 /W This is a test message
```

## More

- To hide something: ```copy /b secret.jpg + pic1.jpg newpic.jpg```
- To merge video files: ```copy /b video1.avi + video2.avi video.avi```
- Find hidden WiFi network: ```Netsh wlan show networks mode=bssid```
- Reply from IP: TTL expired in transit: ```ARP -p <IP> <MAC>```
- Benchmark Drive: ```Winsat disk –write –ran –ransize 262144 –drive f```
- Create Symbolic links: ```fsutil hardlink create <destination_path> <file_path>```
