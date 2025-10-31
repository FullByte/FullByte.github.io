# Windows

## Windows 11

Install without account:

On the first setup screen press Shift + F10 (CMD will open)

```cmd
net user yourusername/add
net localgroup administrators yourusername /add
net user yourusername/active:yes
net user yourusername/expires:never
net user administrator /active:no
net user defaultUser0 /delete
```

Next opens registry editor

```cmd
regedit
```

and navigate to

```reg
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\OOBE
```

an delete:

```txt
DefaultAccountAction
DefaultAccountSAMName
DefaultAccountSID
```

Right click on `LaunchUserOOBE` and rename it to `SkipMachineOOBE` and the value is set to 1.

Close registry editor and reboot computer:

```cmd
shutdown /r /t 0
```

Get old contect menu

```cmd
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

Get old explorer view

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Shell Extensions\Blocked]
"{e2bf9676-5f8f-435c-97eb-11607a5bedf7}"=""
```

## Features

### HyperV

```ps1
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
Get-WindowsOptionalFeature -Online | Findstr /i "Hyper-V"
```

### WSL

```ps1
wsl --install
wsl --set-default-version 2
wsl --list --online
wsl --install -d Debian
```

### RSAT

To see the RSAT tools available for installation:

```ps1
Get-WindowsCapability -Name RSAT* -Online | Select-Object -Property DisplayName, State
```

Install All RSAT Tools at Once:

```ps1
Get-WindowsCapability -Name RSAT* -Online | Add-WindowsCapability -Online
```

Install Specific RSAT Tools:

```ps1
Add-WindowsCapability -Online -Name RSAT.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0
```

## CMD

More: <https://bytescout.com/blog/windows-command-prompt-commands.html>

Basics

- System Information: ```systeminfo```
- NIC and DNS Info: ```ipconfig -all```
- Active Connections: ```netstat –a```
- Routing table: ```route print```
- Users logged in: ```(Get-CimInstance Win32_LoggedOnUser) | Select-Object -Unique```
- Services Running: ```Msconfig```
- Firewall settings: ```netsh advfirewall show currentprofile```
- Power Config: ```powercfg /l```
- Get tasks running: ```tasklist```
- Current user and groups + privileges: ```whoami /all```

### Systeminfo

Simple systeminfo.bat script

```bat
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

For a more detailed system info dump, run [winPEAS](https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/winPEAS/winPEASbat/winPEAS.bat).

### User Stuff

- Get last logon of user "john": ```net user john | findstr /B /C:"Last logon"```
- Change password: ```Set-ADAccountPassword -Identity "benutzername" -NewPassword (Read-Host -AsSecureString "New PW:") -Reset```
- Change password: ```net user YourUsername * /domain```

### Format and Image stuff

#### Format FAT32 on >32GB

Use ```diskpart``` to clean the disk (requires Admin)

```bat
diskpart
list disk
select disk 2
clean
create partition primary
assign
exit
```

use h2format to format the disk (64kb clusters) e.g. for drive x:

```bat
h2format x: 64
```

### Delete Stuff

Delete logs

```bat
del /f /q /s %windir%\prefetch\*
reg delete "HKCU\Software\Microsoft\Windows\ShellNoRoam\MUICache" /va /f
reg delete "HKLM\Software\Microsoft\Windows\ShellNoRoam\MUICache" /va /f
reg delete "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache" /va /f
reg delete "HKLM\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache" /va /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /va /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist" /va /f
wmic nteventlog where LogFileName=’File Replication Service’ Call ClearEventlog
wmic nteventlog where LogFileName=’Application’ Call ClearEventlog
wmic nteventlog where LogFileName=’System’ Call ClearEventlog
wmic nteventlog where LogFileName=’PowerShell’ Call ClearEventlog
ren %1 temp000 & copy /y %windir%\regedit.exe temp000 & del temp000
```

Delete Files

Drag and drop files/folders into this bat file:

```bat
DEL /F /A /Q \\?\%1
RD /S /Q \\?\%1
```

### Network

- DNS check: ```nslookup -all -debug -type=ANY -class=ANY 0xfab1.net 8.8.8.8```

#### Get MAC Address of remote PC

Option 1

``` bat
net view machinename
nbtstat -a machinename
```

Option 2

``` bat
Ping <IP/machinename>
Arp –a
```

Option 3

``` bat
getmac
```

#### Route network traffic

Requests to 10.11.12.13 will be routed via 8.8.8.8:

``` bat
route add 8.8.8.8 MASK 255.255.255.255 10.11.12.13
route print
```

### traceroute

[pathping](https://de.wikipedia.org/wiki/Pathping) (alternative to tracert)

Using ICMP: ```traceroute -I www.microsoft.com```
Using UDP: ```traceroute -U www.microsoft.com```
Using TCP Port 80 (usually allowed by firewalls): ```traceroute -T -p 80 www.microsoft.com```

#### Send Message

``` bat
net send /users This is a test message
msg \* /SERVER:localhost /TIME:666 /W This is a test message
```

### More

- To hide something: ```copy /b secret.jpg + pic1.jpg newpic.jpg```
- To merge video files: ```copy /b video1.avi + video2.avi video.avi```
- Find hidden WiFi network: ```Netsh wlan show networks mode=bssid```
- Reply from IP: TTL expired in transit: ```ARP -p <IP> <MAC>```
- Benchmark Drive: ```Winsat disk –write –ran –ransize 262144 –drive f```
- Create Symbolic links: ```fsutil hardlink create <destination_path> <file_path>```

### Clean up logs

``` bat
@echo off
del /f /q /s %windir%\prefetch\*
reg delete "HKCU\Software\Microsoft\Windows\ShellNoRoam\MUICache" /va /f
reg delete "HKLM\Software\Microsoft\Windows\ShellNoRoam\MUICache" /va /f
reg delete "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache" /va /f
reg delete "HKLM\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache" /va /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /va /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist" /va /f
wmic nteventlog where LogFileName=’File Replication Service’ Call ClearEventlog
wmic nteventlog where LogFileName=’Application’ Call ClearEventlog
wmic nteventlog where LogFileName=’System’ Call ClearEventlog
wmic nteventlog where LogFileName=’PowerShell’ Call ClearEventlog
ren %1 temp000 & copy /y %windir%\regedit.exe temp000 & del temp000
```

### Windows batch script snippets

Read argument input

``` bat
@echo off
ECHO The %~nx0 script args are...
for %%I IN (%*) DO ECHO %%I
```

## Tweaks

Releases and Editions

- [Windows 10 Enterprise LTSC](https://docs.microsoft.com/en-us/windows/whats-new/ltsc/) is a version with less updates and less noise.
- [Windows 10 Releases](https://docs.microsoft.com/en-us/windows/release-health/release-information)
- [Compare Windows 10 Editions](https://www.microsoft.com/en-us/WindowsForBusiness/Compare) and also check [wikipedia](https://en.wikipedia.org/wiki/Windows_10_editions)

Windows History: <https://winhistory.de>

### Windows Cleaner

Windows Base Install (depending on the release you are using) comes with more or less possibly undesired settings/applications. Here are some tools that take care of that:

- Sophia Script for Windows: <https://github.com/farag2/Sophia-Script-for-Windows>

Be careful with these tools and scripts; ideally copy those parts of the script you want and create your own.

Delete all App Packages on Windows 10 (add "-WhatIf" before running this to see if you really want to do this):

```ps1
Get-AppxPackage | Remove-AppxPackage
```

### Commands that help

- Export current drivers: ```pnputil /export-driver * e:\treiber```

### Pimp Desktop

Note really required and may just waste laptop battery life and/or desktop CPU but nice to look at/use:

- Animated Background and Screen Saver: <https://github.com/rocksdanister/lively>
- Microsoft PowerToys: <https://docs.microsoft.com/en-us/windows/powertoys/>
- Ear Trumpet: <https://github.com/File-New-Project/EarTrumpet>
- I like and recommend [dracula theme](https://draculatheme.com/) if available for applications.

### Useful shortcuts

#### App volume and device preferences

URI for "App volume and device preferences" is: ```ms-settings:apps-volume```

Create a file e.g. ```winaudio.url``` with the following content:

``` url
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,0
[InternetShortcut]
IDList=
URL=ms-settings:apps-volume
```

## Fix

Fixing Windows 10 issues

### Windows 10 boots in Recovery Mode

#### Recovery Deaktivieren

Problembehandlung → Eingabeaufforderung → command:

```cmd
bcdedit /set {current} recoveryenabled No
```

#### Fix MBR

Problembehandlung → Eingabeaufforderung → commands:

```cmd
bootrec.exe /fixmbr
bootrec.exe /fixboot
bootrec.exe /rebuildbcd
```

Sektor bzw. Festplatten reparieren
Problembehandlung → Eingabeaufforderung → command:

```cmd
chkdsk /f /r
```

#### Windows 10 abgesicherten Modus

Problembehandlung", dann „Erweiterte Optionen", dann „Starteinstellungen", dann „Neu starten"
Drücke auf „F5-Taste", um Abgesicherten Modus mit Netzwerktreibern zu aktivieren.

## Shortcuts

### Built in Tools

#### Snip & Sketch (Screenshot)

[Download Snip & Sketch from the store](https://www.microsoft.com/en-us/p/snip-sketch/9mz95kl8mr0l?activetab=pivot:overviewtab)

Take screenshot: Windows + Shift + S

#### Record Screen

- Start recording mode: Windows + G
- start recording: Window + Alt + R

### launch-settings URI

Source: <https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-settings-app>

#### Accounts

| Settings page         | URI                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------|
| Access work or school | ms-settings:workplace                                                                                   |
| Email & app accounts  | ms-settings:emailandaccounts                                                                            |
| Family & other people | ms-settings:otherusers                                                                                  |
| Set up a kiosk        | ms-settings:assignedaccess                                                                              |
| Sign-in options       | ms-settings:signinoptions<br>ms-settings:signinoptions-dynamiclock                                      |
| Sync your settings    | ms-settings:sync                                                                                        |
| Windows Hello setup   | ms-settings:signinoptions-launchfaceenrollment<br>ms-settings:signinoptions-launchfingerprintenrollment |
| Your info             | ms-settings:yourinfo                                                                                    |

#### Apps

| Settings page            | URI                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------|
| Apps & Features          | ms-settings:appsfeatures                                                                     |
| App features             | ms-settings:appsfeatures-app (Reset, manage add-on & downloadable content, etc. for the app) |
| Apps for websites        | ms-settings:appsforwebsites                                                                  |
| Default apps             | ms-settings:defaultapps                                                                      |
| Manage optional features | ms-settings:optionalfeatures                                                                 |
| Offline Maps             | ms-settings:maps<br/>ms-settings:maps-downloadmaps (Download maps)                           |
| Startup apps             | ms-settings:startupapps                                                                      |
| Video playback           | ms-settings:videoplayback                                                                    |

#### Cortana

| Settings page             | URI                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------|
| Cortana across my devices | ms-settings:cortana-notifications                                                          |
| More details              | ms-settings:cortana-moredetails                                                            |
| Permissions & History     | ms-settings:cortana-permissions                                                            |
| Searching Windows         | ms-settings:cortana-windowssearch                                                          |
| Talk to Cortana           | ms-settings:cortana-language<br/>ms-settings:cortana<br/>ms-settings:cortana-talktocortana |

#### Devices

| Settings page       | URI                                                                                          |
|---------------------|----------------------------------------------------------------------------------------------|
| AutoPlay            | ms-settings:autoplay                                                                         |
| Bluetooth           | ms-settings:bluetooth                                                                        |
| Connected Devices   | ms-settings:connecteddevices                                                                 |
| Default camera      | ms-settings:camera (**Deprecated in Windows 10, version 1809 and later**)                    |
| Mouse & touchpad    | ms-settings:mousetouchpad (touchpad settings only available on devices that have a touchpad) |
| Pen & Windows Ink   | ms-settings:pen                                                                              |
| Printers & scanners | ms-settings:printers                                                                         |
| Touchpad            | ms-settings:devices-touchpad (only available if touchpad hardware is present)                |
| Typing              | ms-settings:typing                                                                           |
| USB                 | ms-settings:usb                                                                              |
| Wheel               | ms-settings:wheel (only available if Dial is paired)                                         |
| Your phone          | ms-settings:mobile-devices                                                                   |

#### Ease of access

| Settings page         | URI                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------|
| Audio                 | ms-settings:easeofaccess-audio                                                               |
| Closed captions       | ms-settings:easeofaccess-closedcaptioning                                                    |
| Color filters         | ms-settings:easeofaccess-colorfilter                                                         |
| Cursor & pointer size | ms-settings:easeofaccess-cursorandpointersize                                                |
| Display               | ms-settings:easeofaccess-display                                                             |
| Eye control           | ms-settings:easeofaccess-eyecontrol                                                          |
| Fonts                 | ms-settings:fonts                                                                            |
| High contrast         | ms-settings:easeofaccess-highcontrast                                                        |
| Keyboard              | ms-settings:easeofaccess-keyboard                                                            |
| Magnifier             | ms-settings:easeofaccess-magnifier                                                           |
| Mouse                 | ms-settings:easeofaccess-mouse                                                               |
| Narrator              | ms-settings:easeofaccess-narrator                                                            |
| Other options         | ms-settings:easeofaccess-otheroptions (**Deprecated in Windows 10, version 1809 and later**) |
| Speech                | ms-settings:easeofaccess-speechrecognition                                                   |

#### Extras

| Settings page      | URI                                                                                               |
|--------------------|---------------------------------------------------------------------------------------------------|
| Extras             | ms-settings:extras (only available if "settings apps" are installed, for example, by a 3rd party) |
| Settings home page | ms-settings:                                                                                      |

#### Gaming

| Settings page              | URI                                                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Broadcasting               | ms-settings:gaming-broadcasting                                                                                            |
| Game bar                   | ms-settings:gaming-gamebar                                                                                                 |
| Game DVR                   | ms-settings:gaming-gamedvr                                                                                                 |
| Game Mode                  | ms-settings:gaming-gamemode                                                                                                |
| Playing a game full screen | ms-settings:quietmomentsgame                                                                                               |
| TruePlay                   | ms-settings:gaming-trueplay (**As of Windows 10, version 1809 (10.0; Build 17763), this feature is removed from Windows**) |
| Xbox Networking            | ms-settings:gaming-xboxnetworking                                                                                          |

#### Mixed reality

| Settings page    | URI                                         |
|------------------|---------------------------------------------|
| Audio and speech | ms-settings:holographic-audio               |
| Environment      | ms-settings:privacy-holographic-environment |
| Headset display  | ms-settings:holographic-headset             |
| Uninstall        | ms-settings:holographic-management          |

#### Network and internet

| Settings page         | URI                                                                          |
|-----------------------|------------------------------------------------------------------------------|
| Airplane mode         | ms-settings:network-airplanemode<br/>ms-settings:proximity                   |
| Cellular & SIM        | ms-settings:network-cellular                                                 |
| Data usage            | ms-settings:datausage                                                        |
| Dial-up               | ms-settings:network-dialup                                                   |
| DirectAccess          | ms-settings:network-directaccess (only available if DirectAccess is enabled) |
| Ethernet              | ms-settings:network-ethernet                                                 |
| Manage known networks | ms-settings:network-wifisettings                                             |
| Mobile hotspot        | ms-settings:network-mobilehotspot                                            |
| NFC                   | ms-settings:nfctransactions                                                  |
| Proxy                 | ms-settings:network-proxy                                                    |
| Status                | ms-settings:network-status<br/>ms-settings:network                           |
| VPN                   | ms-settings:network-vpn                                                      |
| Wi-Fi                 | ms-settings:network-wifi (only available if the device has a wifi adapter)   |
| Wi-Fi Calling         | ms-settings:network-wificalling (only available if Wi-Fi calling is enabled) |

#### Personalization

| Settings page                        | URI                                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------------------|
| Background                           | ms-settings:personalization-background                                                    |
| Choose which folders appear on Start | ms-settings:personalization-start-places                                                  |
| Colors                               | ms-settings:personalization-colors<br/>ms-settings:colors                                 |
| Glance                               | ms-settings:personalization-glance (**Deprecated in Windows 10, version 1809 and later**) |
| Lock screen                          | ms-settings:lockscreen                                                                    |
| Navigation bar                       | ms-settings:personalization-navbar (**Deprecated in Windows 10, version 1809 and later**) |
| Personalization (category)           | ms-settings:personalization                                                               |
| Start                                | ms-settings:personalization-start                                                         |
| Taskbar                              | ms-settings:taskbar                                                                       |
| Themes                               | ms-settings:themes                                                                        |

#### Phone

| Settings page | URI                                                                                                                                          |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Your phone    | ms-settings:mobile-devices<br/>ms-settings:mobile-devices-addphone<br/>ms-settings:mobile-devices-addphone-direct (Opens **Your Phone** app) |

#### Privacy

| Settings page            | URI                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------|
| Accessory apps           | ms-settings:privacy-accessoryapps (**Deprecated in Windows 10, version 1809 and later**) |
| Account info             | ms-settings:privacy-accountinfo                                                          |
| Activity history         | ms-settings:privacy-activityhistory                                                      |
| Advertising ID           | ms-settings:privacy-advertisingid (**Deprecated in Windows 10, version 1809 and later**) |
| App diagnostics          | ms-settings:privacy-appdiagnostics                                                       |
| Automatic file downloads | ms-settings:privacy-automaticfiledownloads                                               |
| Background Apps          | ms-settings:privacy-backgroundapps                                                       |
| Calendar                 | ms-settings:privacy-calendar                                                             |
| Call history             | ms-settings:privacy-callhistory                                                          |
| Camera                   | ms-settings:privacy-webcam                                                               |
| Contacts                 | ms-settings:privacy-contacts                                                             |
| Documents                | ms-settings:privacy-documents                                                            |
| Email                    | ms-settings:privacy-email                                                                |
| Eye tracker              | ms-settings:privacy-eyetracker (requires eyetracker hardware)                            |
| Feedback & diagnostics   | ms-settings:privacy-feedback                                                             |
| File system              | ms-settings:privacy-broadfilesystemaccess                                                |
| General                  | ms-settings:privacy or ms-settings:privacy-general                                       |
| Inking & typing          | ms-settings:privacy-speechtyping                                                         |
| Location                 | ms-settings:privacy-location                                                             |
| Messaging                | ms-settings:privacy-messaging                                                            |
| Microphone               | ms-settings:privacy-microphone                                                           |
| Motion                   | ms-settings:privacy-motion                                                               |
| Notifications            | ms-settings:privacy-notifications                                                        |
| Other devices            | ms-settings:privacy-customdevices                                                        |
| Phone calls              | ms-settings:privacy-phonecalls                                                           |
| Pictures                 | ms-settings:privacy-pictures                                                             |
| Radios                   | ms-settings:privacy-radios                                                               |
| Speech                   | ms-settings:privacy-speech                                                               |
| Tasks                    | ms-settings:privacy-tasks                                                                |
| Videos                   | ms-settings:privacy-videos                                                               |
| Voice activation         | ms-settings:privacy-voiceactivation                                                      |

#### Surface Hub

| Settings page          | URI                                     |
|------------------------|-----------------------------------------|
| Accounts               | ms-settings:surfacehub-accounts         |
| Session cleanup        | ms-settings:surfacehub-sessioncleanup   |
| Team Conferencing      | ms-settings:surfacehub-calling          |
| Team device management | ms-settings:surfacehub-devicemanagenent |
| Welcome screen         | ms-settings:surfacehub-welcome          |

#### System

| Settings page                     | URI                                                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------------------------------|
| About                             | ms-settings:about                                                                                       |
| Advanced display settings         | ms-settings:display-advanced (only available on devices that support advanced display options)          |
| App volume and device preferences | ms-settings:apps-volume (**Added in Windows 10, version 1903**)                                         |
| Battery Saver                     | ms-settings:batterysaver (only available on devices that have a battery, such as a tablet)              |
| Battery Saver settings            | ms-settings:batterysaver-settings (only available on devices that have a battery, such as a tablet)     |
| Battery use                       | ms-settings:batterysaver-usagedetails (only available on devices that have a battery, such as a tablet) |
| Clipboard                         | ms-settings:clipboard                                                                                   |
| Display                           | ms-settings:display                                                                                     |
| Default Save Locations            | ms-settings:savelocations                                                                               |
| Display                           | ms-settings:screenrotation                                                                              |
| Duplicating my display            | ms-settings:quietmomentspresentation                                                                    |
| During these hours                | ms-settings:quietmomentsscheduled                                                                       |
| Encryption                        | ms-settings:deviceencryption                                                                            |
| Focus assist                      | ms-settings:quiethours <br> ms-settings:quietmomentshome                                                |
| Graphics Settings                 | ms-settings:display-advancedgraphics (only available on devices that support advanced graphics options) |
| Messaging                         | ms-settings:messaging                                                                                   |
| Multitasking                      | ms-settings:multitasking                                                                                |
| Night light settings              | ms-settings:nightlight                                                                                  |
| Phone                             | ms-settings:phone-defaultapps                                                                           |
| Projecting to this PC             | ms-settings:project                                                                                     |
| Shared experiences                | ms-settings:crossdevice                                                                                 |
| Tablet mode                       | ms-settings:tabletmode                                                                                  |
| Taskbar                           | ms-settings:taskbar                                                                                     |
| Notifications & actions           | ms-settings:notifications                                                                               |
| Remote Desktop                    | ms-settings:remotedesktop                                                                               |
| Phone                             | ms-settings:phone (**Deprecated in Windows 10, version 1809 and later**)                                |
| Power & sleep                     | ms-settings:powersleep                                                                                  |
| Sound                             | ms-settings:sound                                                                                       |
| Storage                           | ms-settings:storagesense                                                                                |
| Storage Sense                     | ms-settings:storagepolicies                                                                             |

#### Time and language

| Settings page       | URI                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Date & time         | ms-settings:dateandtime                                                                                                                                                                                                                                                                                                                                                                        |
| Japan IME settings  | ms-settings:regionlanguage-jpnime (available if the Microsoft Japan input method editor is installed)                                                                                                                                                                                                                                                                                          |
| Region              | ms-settings:regionformatting                                                                                                                                                                                                                                                                                                                                                                   |
| Language            | ms-settings:keyboard<br/>ms-settings:regionlanguage<br/>ms-settings:regionlanguage-bpmfime<br/>ms-settings:regionlanguage-cangjieime<br/>ms-settings:regionlanguage-chsime-pinyin-domainlexicon<br/>ms-settings:regionlanguage-chsime-pinyin-keyconfig<br/>ms-settings:regionlanguage-chsime-pinyin-udp<br/>ms-settings:regionlanguage-chsime-wubi-udp<br/>ms-settings:regionlanguage-quickime |
| Pinyin IME settings | ms-settings:regionlanguage-chsime-pinyin (available if the Microsoft Pinyin input method editor is installed)                                                                                                                                                                                                                                                                                  |
| Speech              | ms-settings:speech                                                                                                                                                                                                                                                                                                                                                                             |
| Wubi IME settings   | ms-settings:regionlanguage-chsime-wubi (available if the Microsoft Wubi input method editor is installed)                                                                                                                                                                                                                                                                                      |

#### Update and security

| Settings page                      | URI                                                                                                       |
|------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Activation                         | ms-settings:activation                                                                                    |
| Backup                             | ms-settings:backup                                                                                        |
| Delivery Optimization              | ms-settings:delivery-optimization                                                                         |
| Find My Device                     | ms-settings:findmydevice                                                                                  |
| For developers                     | ms-settings:developers                                                                                    |
| Recovery                           | ms-settings:recovery                                                                                      |
| Troubleshoot                       | ms-settings:troubleshoot                                                                                  |
| Windows Security                   | ms-settings:windowsdefender                                                                               |
| Windows Insider Program            | ms-settings:windowsinsider (only present if user is enrolled in WIP)<br/>ms-settings:windowsinsider-optin |
| Windows Update                     | ms-settings:windowsupdate<br>ms-settings:windowsupdate-action                                             |
| Windows Update-Advanced options    | ms-settings:windowsupdate-options                                                                         |
| Windows Update-Restart options     | ms-settings:windowsupdate-restartoptions                                                                  |
| Windows Update-View update history | ms-settings:windowsupdate-history                                                                         |

#### User accounts

| Settings page    | URI                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------|
| Provisioning     | ms-settings:workplace-provisioning (only available if enterprise has deployed a provisioning package)         |
| Provisioning     | ms-settings:provisioning (only available on mobile and if the enterprise has deployed a provisioning package) |
| Windows Anywhere | ms-settings:windowsanywhere (device must be Windows Anywhere-capable)                                         |

### CLSID Key (GUID) Shortcuts List

Source: <https://docs.microsoft.com/de-de/windows/win32/com/clsid-key-hklm>

Run this as follows:

```cmd
# Template
explorer shell:::{CLSID key}
explorer /e,::{CLSID key}

# Example
explorer shell:::{ED7BA470-8E54-465E-825C-99712043E01C}
```

| Opens                                                               | CLSID key (GUID) shortcut                                                       |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 3D Objects (folder)                                                 | {0DB7E03F-FC29-4DC6-9020-FF41B59E513A}                                          |
| Add Network Location                                                | {D4480A50-BA28-11d1-8E75-00C04FA31A86}                                          |
| Administrative Tools                                                | {D20EA4E1-3957-11d2-A40B-0C5020524153}                                          |
| Applications                                                        | {4234d49b-0245-4df3-b780-3893943456e1}                                          |
| AutoPlay                                                            | {9C60DE1E-E5FC-40f4-A487-460851A8D915}                                          |
| Backup and Restore (Windows 7)                                      | {B98A2BEA-7D42-4558-8BD1-832F41BAC6FD}                                          |
| BitLocker Drive Encryption                                          | {D9EF8727-CAC2-4e60-809E-86F80A666C91}                                          |
| Bluetooth Devices                                                   | {28803F59-3A75-4058-995F-4EE5503B023C}                                          |
| Color Management                                                    | {B2C761C6-29BC-4f19-9251-E6195265BAF1}                                          |
| Command Folder                                                      | {437ff9c0-a07f-4fa0-af80-84b6c6440a16}                                          |
| Common Places FS Folder                                             | {d34a6ca6-62c2-4c34-8a7c-14709c1ad938}                                          |
| Control Panel                                                       | {5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}                                          |
| Control Panel (All Tasks)                                           | {ED7BA470-8E54-465E-825C-99712043E01C}                                          |
| Control Panel (always Category view)                                | {26EE0668-A00A-44D7-9371-BEB064C98683}                                          |
| Appearance and Personalization                                      | {26EE0668-A00A-44D7-9371-BEB064C98683}\1                                        |
| Clock and Region                                                    | {26EE0668-A00A-44D7-9371-BEB064C98683}\6                                        |
| Ease of Access                                                      | {26EE0668-A00A-44D7-9371-BEB064C98683}\7                                        |
| Hardware and Sound                                                  | {26EE0668-A00A-44D7-9371-BEB064C98683}\2                                        |
| Network and Internet                                                | {26EE0668-A00A-44D7-9371-BEB064C98683}\3                                        |
| Programs                                                            | {26EE0668-A00A-44D7-9371-BEB064C98683}\8                                        |
| System and Security                                                 | {26EE0668-A00A-44D7-9371-BEB064C98683}\5                                        |
|                                                                     | OR                                                                              |
|                                                                     | {26EE0668-A00A-44D7-9371-BEB064C98683}\10                                       |
| User Accounts                                                       | {26EE0668-A00A-44D7-9371-BEB064C98683}\9                                        |
| Control Panel (always Icons view)                                   | {21EC2020-3AEA-1069-A2DD-08002B30309D}                                          |
| Credential Manager                                                  | {1206F5F1-0569-412C-8FEC-3204630DFB70}                                          |
| Date and Time                                                       | {E2E7934B-DCE5-43C4-9576-7FE4F75E7480}                                          |
| Default Programs                                                    | {17cd9488-1228-4b2f-88ce-4298e93e0966}                                          |
| Default Apps page in Settings                                       | {17cd9488-1228-4b2f-88ce-4298e93e0966}\pageDefaultProgram                       |
| Default Apps page in Settings                                       | {17cd9488-1228-4b2f-88ce-4298e93e0966}\pageFileAssoc                            |
| delegate folder that appears in Computer                            | {b155bdf8-02f0-451e-9a26-ae317cfd7779}                                          |
| Desktop (folder)                                                    | {B4BFCC3A-DB2C-424C-B029-7FE99A87C641}                                          |
| Device Manager                                                      | {74246bfc-4c96-11d0-abef-0020af6b0b7a}                                          |
| Devices and Printers                                                | {A8A91A66-3A7D-4424-8D24-04E180695C7A}                                          |
| Documents (folder)                                                  | {A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {d3162b92-9365-467a-956b-92703aca08af}                                          |
| Downloads (folder)                                                  | {088e3905-0323-4b02-9826-5d99428e115f}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {374DE290-123F-4565-9164-39C4925E467B}                                          |
| Ease of Access Center                                               | {D555645E-D4F8-4c29-A827-D93C859C4F2A}                                          |
| Use the computer without a display                                  | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageNoVisual                             |
| Make the computer easier to see                                     | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageEasierToSee                          |
| Use the computer without a mouse or keyboard                        | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageNoMouseOrKeyboard                    |
| Make the mouse easier to use                                        | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageEasierToClick                        |
| Set up Mouse Keys                                                   | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageMouseKeysSettings                    |
| Make the keyboard easier to use                                     | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageKeyboardEasierToUse                  |
| Use text or visual alternatives for sounds                          | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageEasierWithSounds                     |
| Make it easier to focus on tasks                                    | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageEasierToReadAndWrite                 |
| Set up Filter Keys                                                  | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageFilterKeysSettings                   |
| Set up Sticky Keys                                                  | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageStickyKeysSettings                   |
| Get recommendations to make your computer easier to use (cognitive) | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageQuestionsCognitive                   |
| Get recommendations to make your computer easier to use (eyesight)  | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageQuestionsEyesight                    |
| Set up Repeat and Slow Keys                                         | {D555645E-D4F8-4c29-A827-D93C859C4F2A}\pageRepeatRateSlowKeysSettings           |
| E-mail (default e-mail program)                                     | {2559a1f5-21d7-11d4-bdaf-00c04f60b9f0}                                          |
| Favorites                                                           | {323CA680-C24D-4099-B94D-446DD2D7249E}                                          |
| File Explorer Options                                               | {6DFD7C5C-2451-11d3-A299-00C04F8EF6AF}                                          |
| File History                                                        | {F6B6E965-E9B2-444B-9286-10C9152EDBC5}                                          |
| Folder Options                                                      | {6DFD7C5C-2451-11d3-A299-00C04F8EF6AF}                                          |
| Font Settings                                                       | {93412589-74D4-4E4E-AD0E-E0CB621440FD}                                          |
| Fonts (folder)                                                      | {BD84B380-8CA2-1069-AB1D-08000948F534}                                          |
| Frequent folders                                                    | {3936E9E4-D92C-4EEE-A85A-BC16D5EA0819}                                          |
| Games Explorer                                                      | {ED228FDF-9EA8-4870-83b1-96b02CFE0D52}                                          |
| Get Programs                                                        | {15eae92e-f17a-4431-9f28-805e482dafd4}                                          |
| Help and Support                                                    | {2559a1f1-21d7-11d4-bdaf-00c04f60b9f0}                                          |
| Hyper-V Remote File Browsing                                        | {0907616E-F5E6-48D8-9D61-A91C3D28106D}                                          |
| Indexing Options                                                    | {87D66A43-7B11-4A28-9811-C86EE395ACF7}                                          |
| Infared (if installed)                                              | {A0275511-0E86-4ECA-97C2-ECD8F1221D08}                                          |
| Installed Updates                                                   | {d450a8a1-9568-45c7-9c0e-b4f9fb4537bd}                                          |
| Intel Rapid Storage Technology (if installed)                       | {E342F0FE-FF1C-4c41-BE37-A0271FC90396}                                          |
| Internet Options (Internet Explorer)                                | {A3DD4F92-658A-410F-84FD-6FBBBEF2FFFE}                                          |
| Keyboard Properties                                                 | {725BE8F7-668E-4C7B-8F90-46BDB0936430}                                          |
| Libraries                                                           | {031E4825-7B94-4dc3-B131-E946B44C8DD5}                                          |
| Location Information (Phone and Modem Control Panel)                | {40419485-C444-4567-851A-2DD7BFA1684D}                                          |
| Location Settings                                                   | {E9950154-C418-419e-A90A-20C5287AE24B}                                          |
| Media Servers                                                       | {289AF617-1CC3-42A6-926C-E6A863F0E3BA}                                          |
| Mouse Properties                                                    | {6C8EEC18-8D75-41B2-A177-8831D59D2D50}                                          |
| Music (folder)                                                      | {1CF1260C-4DD0-4ebb-811F-33C572699FDE}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}                                          |
| My Documents                                                        | {450D8FBA-AD25-11D0-98A8-0800361B1103}                                          |
| netplwiz                                                            | {7A9D77BD-5403-11d2-8785-2E0420524153}                                          |
| Network                                                             | {F02C1A0D-BE21-4350-88B0-7367FC96EF3C}                                          |
| Network and Sharing Center                                          | {8E908FC9-BECC-40f6-915B-F4CA0E70D03D}                                          |
| Advanced sharing settings                                           | {8E908FC9-BECC-40f6-915B-F4CA0E70D03D}\Advanced                                 |
| Media streaming options                                             | {8E908FC9-BECC-40f6-915B-F4CA0E70D03D}\ShareMedia                               |
| Network Connections                                                 | {7007ACC7-3202-11D1-AAD2-00805FC1270E}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {992CFFA0-F557-101A-88EC-00DD010CCC48}                                          |
| Network (WorkGroup)                                                 | {208D2C60-3AEA-1069-A2D7-08002B30309D}                                          |
| Notification Area Icons                                             | {05d7b0f4-2121-4eff-bf6b-ed3f69b894d9}                                          |
| NVIDIA Control Panel (if installed)                                 | {0bbca823-e77d-419e-9a44-5adec2c8eeb0}                                          |
| Offline Files Folder                                                | {AFDB1F70-2A4C-11d2-9039-00C04F8EEB3E}                                          |
| OneDrive                                                            | {018D5C66-4533-4307-9B53-224DE2ED1FE6}                                          |
| Pen and Touch                                                       | {F82DF8F7-8B9F-442E-A48C-818EA735FF9B}                                          |
| Personalization                                                     | {ED834ED6-4B5A-4bfe-8F11-A626DCB6A921}                                          |
| Color and Appearance                                                | {ED834ED6-4B5A-4bfe-8F11-A626DCB6A921}\pageColorization                         |
| Desktop Background                                                  | {ED834ED6-4B5A-4bfe-8F11-A626DCB6A921}\pageWallpaper                            |
| Pictures (folder)                                                   | {24ad3ad4-a569-4530-98e1-ab02f9417aa8}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}                                          |
| Portable Devices                                                    | {35786D3C-B075-49b9-88DD-029876E11C01}                                          |
| Power Options                                                       | {025A5937-A6BE-4686-A844-36FE4BEC8B6D}                                          |
| Create a power plan                                                 | {025A5937-A6BE-4686-A844-36FE4BEC8B6D}\pageCreateNewPlan                        |
| Edit Plan Settings                                                  | {025A5937-A6BE-4686-A844-36FE4BEC8B6D}\pagePlanSettings                         |
| System Settings                                                     | {025A5937-A6BE-4686-A844-36FE4BEC8B6D}\pageGlobalSettings                       |
| Previous Versions Results Folder                                    | {f8c2ab3b-17bc-41da-9758-339d7dbf2d88}                                          |
| printhood delegate folder                                           | {ed50fc29-b964-48a9-afb3-15ebb9b97f36}                                          |
| Printers                                                            | {2227A280-3AEA-1069-A2DE-08002B30309D}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {863aa9fd-42df-457b-8e4d-0de1b8015c60}                                          |
| Problem Reporting Settings                                          | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageSettings                             |
| Programs and Features                                               | {7b81be6a-ce2b-4676-a29e-eb907a5126c5}                                          |
| Public (folder)                                                     | {4336a54d-038b-4685-ab02-99bb52d3fb8b}                                          |
| Quick access                                                        | {679f85cb-0220-4080-b29b-5540cc05aab6}                                          |
| Recent folders                                                      | {22877a6d-37a1-461a-91b0-dbda5aaebc99}                                          |
| Recent Items Instance Folder                                        | {4564b25e-30cd-4787-82ba-39e73a750b14}                                          |
| Recovery                                                            | {9FE63AFD-59CF-4419-9775-ABCC3849F861}                                          |
| Recycle Bin                                                         | {645FF040-5081-101B-9F08-00AA002F954E}                                          |
| Region                                                              | {62D8ED13-C9D0-4CE8-A914-47DD628FB1B0}                                          |
| Reliability Monitor                                                 | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageReliabilityView                      |
| Remote Assistance                                                   | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\raPage                                   |
| RemoteApp and Desktop Connections                                   | {241D7C96-F8BF-4F85-B01F-E2B043341A4B}                                          |
| Connection Properties                                               | {241D7C96-F8BF-4F85-B01F-E2B043341A4B}\PropertiesPage                           |
| Remote Printers                                                     | {863aa9fd-42df-457b-8e4d-0de1b8015c60}                                          |
| Removable Drives                                                    | {F5FB2C77-0E2F-4A16-A381-3E560C68BC83}                                          |
| Removable Storage Devices                                           | {a6482830-08eb-41e2-84c1-73920c2badb9}                                          |
| Results Folder                                                      | {2965e715-eb66-4719-b53f-1672673bbefa}                                          |
| Run                                                                 | {2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}                                          |
| Search (File Explorer)                                              | {9343812e-1c37-4a49-a12e-4b2d810d956b}                                          |
| Search (Windows)                                                    | {2559a1f8-21d7-11d4-bdaf-00c04f60b9f0}                                          |
| Security and Maintenance                                            | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}                                          |
| Advanced Problem Reporting Settings                                 | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageAdvSettings                          |
| Change Security and Maintenance settings                            | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\Settings                                 |
| Problem Details                                                     | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageReportDetails                        |
| Problem Reporting Settings                                          | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageSettings                             |
| Problem Reports                                                     | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageProblems                             |
| Reliability Monitor                                                 | {BB64F8A7-BEE7-4E1A-AB8D-7D8273F7FDB6}\pageReliabilityView                      |
| Set Program Access and Computer Defaults                            | {2559a1f7-21d7-11d4-bdaf-00c04f60b9f0}                                          |
| Show Desktop                                                        | {3080F90D-D7AD-11D9-BD98-0000947B0257}                                          |
| Sound                                                               | {F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}                                          |
| Speech Recognition                                                  | {58E3C745-D971-4081-9034-86E34B30836A}                                          |
| Storage Spaces                                                      | {F942C606-0914-47AB-BE56-1321B8035096}                                          |
| Sync Center                                                         | {9C73F5E5-7AE7-4E32-A8E8-8D23B85255BF}                                          |
| Sync Setup                                                          | {9C73F5E5-7AE7-4E32-A8E8-8D23B85255BF}\::{F1390A9A-A3F4-4E5D-9C5F-98F3BD8D935C} |
| Sync Setup Folder                                                   | {2E9E59C0-B437-4981-A647-9C34B9B90891}                                          |
| System                                                              | {BB06C0E4-D293-4f75-8A90-CB05B6477EEE}                                          |
| System Icons                                                        | {05d7b0f4-2121-4eff-bf6b-ed3f69b894d9}\SystemIcons                              |
| System Restore                                                      | {3f6bc534-dfa1-4ab4-ae54-ef25a74e0107}                                          |
| Tablet PC Settings                                                  | {80F3F1D5-FECA-45F3-BC32-752C152E456E}                                          |
| Task View                                                           | {3080F90E-D7AD-11D9-BD98-0000947B0257}                                          |
| Taskbar and Navigation properties                                   | {0DF44EAA-FF21-4412-828E-260A8728E7F1}                                          |
| Taskbar page in Settings                                            | {0DF44EAA-FF21-4412-828E-260A8728E7F1}                                          |
| Text to Speech                                                      | {D17D1D6D-CC3F-4815-8FE3-607E7D5D10B3}                                          |
| This Device                                                         | {5b934b42-522b-4c34-bbfe-37a3ef7b9c90}                                          |
| This PC                                                             | {20D04FE0-3AEA-1069-A2D8-08002B30309D}                                          |
| Troubleshooting                                                     | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}                                          |
| Additional Information                                              | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\resultPage                               |
| All Categories                                                      | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\listAllPage                              |
| Change Settings                                                     | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\settingPage                              |
| History                                                             | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\historyPage                              |
| Search Troubleshooting                                              | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\searchPage                               |
| Troubleshoot problems - Hardware and Sound                          | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\devices                                  |
| Troubleshoot problems - Network and Internet                        | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\network                                  |
| Troubleshoot problems - Programs                                    | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\applications                             |
| Troubleshoot problems - System and Security                         | {C58C4893-3BE0-4B45-ABB5-A63E4B8C8651}\system                                   |
| User Accounts                                                       | {60632754-c523-4b62-b45c-4172da012619}                                          |
| Change Your Name                                                    | {60632754-c523-4b62-b45c-4172da012619}\pageRenameMyAccount                      |
| Manage Accounts                                                     | {60632754-c523-4b62-b45c-4172da012619}\pageAdminTasks                           |
| User Accounts (netplwiz)                                            | {7A9D77BD-5403-11d2-8785-2E0420524153}                                          |
| User Pinned                                                         | {1f3427c8-5c10-4210-aa03-2ee45287d668}                                          |
| %UserProfile%                                                       | {59031a47-3f72-44a7-89c5-5595fe6b30ee}                                          |
| Videos (folder)                                                     | {A0953C92-50DC-43bf-BE83-3742FED03C9C}                                          |
|                                                                     | OR                                                                              |
|                                                                     | {f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}                                          |
| Web browser (default)                                               | {871C5380-42A0-1069-A2EA-08002B30309D}                                          |
| Windows Defender Firewall                                           | {4026492F-2F69-46B8-B9BF-5654FC07E423}                                          |
| Allowed apps                                                        | {4026492F-2F69-46B8-B9BF-5654FC07E423}\pageConfigureApps                        |
| Customize Settings                                                  | {4026492F-2F69-46B8-B9BF-5654FC07E423}\PageConfigureSettings                    |
| Restore defaults                                                    | {4026492F-2F69-46B8-B9BF-5654FC07E423}\PageRestoreDefaults                      |
| Windows Mobility Center                                             | {5ea4f148-308c-46d7-98a9-49041b1dd468}                                          |
| Windows Features                                                    | {67718415-c450-4f3c-bf8a-b487642dc39b}                                          |
| Windows To Go                                                       | {8E0C279D-0BD1-43C3-9EBD-31C3DC5B8A77}                                          |
| Work Folders                                                        | {ECDB0924-4208-451E-8EE0-373C0956DE16}                                          |

### Systemverwaltung

- appwiz.cpl	Startet "Add or Remove Programs"
- certmgr.msc	Zertifikat - Manager (Certificate Store)
- ciadv.msc	Indexdienst
- cleanmgr.exe	Datenträgerbereinigung
- Clipbrd	Zwischenablage
- cmd.exe	Eingabeaufforderung
- comexp.msc	Komponentendienste
- compmgmt.msc	Computerverwaltung
- control userpasswords2	Benutzerkonten
- devmgmt.msc	Geräte-Manager 
- dfrg.msc	Defragmentierung
- diskmgmt.msc	Datenträgerverwaltung
- Driverquery	Lister aller aktiven Treiber
- drwtsn32.exe	Dr. Watson
- eventvwr.msc	Ereignisanzeige
- fsmgmt.msc	Freigegebene Ordner
- gpedit.msc	Gruppenrichtlinien - Editor
- ias.msc	Internetauthentifizierungsdienst
- lusrmgr.msc	Benutzer und Gruppen
- msconfig.exe	Systemkonfigurationsprogramm
- mstsc.exe	Remotedesktopverbindung
- narrator.exe	Sprachausgabe
- ntbackup.exe	Sicherungs - Wiederherstellungs - Assistent
- ntmsmgr.msc	Wechselmedienverwaltung
- ntmsoprq.msc	Übersicht über Wechselmedien
- odbcad32.exe	ODBC-Datenquellen-Administrator
- Osk	Bildschirmtastatur
- perfmon.msc	Systemmonitor
- regedit.exe	Registrierungs - Editor  
- secpol.msc	Sicherheitseinstellungen
- services.msc	Diensteverwaltung
- shrpubw.exe	Freigabe erstellen
- sigverif.exe	Dateisignaturverifizierung
- Sysedit	Systemkonfigurationseditor
- syskey.exe	Sichern der XP Kontodatenbank
- taskmgr.exe	Task - Manager
- winchat.exe	Windows Chat
- Windbver.exe	SQL-Server
- wmimgmt.msc	WMI-Steuerung
- adsiedit.msc	Microsoft Management Console (MMC)-SnapIn
- dfsgui.msc	DFS (verteiltes Dateisystem)
- dhcpmgmt.msc	DHCP Admin
- dnsmgmt.msc	DNS Manager
- dsa.msc	Active Directory  
- iis.msc bzw. inetmgr	IIS Verwaltung nur bei installiertem IIS
- Mmc	leere Management-Konsole
- mscorfcg.msc	mmc snapin
- rrasmgmt.msc	Routing und RAS
- winsmgmt.msc	WINS

### Windows Shortcuts

- [Windows-Taste] – Zwischen Metro-Programm und dem Metro-Startmenü wechseln
- [Windows-Taste]+[Leertaste] -  Eingabesprache und Tastaturlayout ändern
- [Windows-Taste]+[Y] – Windows-Desktop kurzzeitig anzeigen
- [Windows-Taste]+[D] - Desktop anzeigen
- [Windows-Taste]+[O] – Bildschirmorientierung/-ausrichtung arretieren (Kippsensor deaktivieren)
- [Windows-Taste]+[V] – Vorwärts durch Toasts blättern
- [Windows-Taste]+[Shift/Umschalten]+[V] – Rückwärts durch Toasts blättern
- [Windows-Taste]+[Return/Enter] - Narrator starten
- [Windows-Taste]+[Bild rauf] – Kachel nach links schieben
- [Windows-Taste]+[Bild runter] – Kachel nach rechts schieben
- [Windows-Taste]+[Shift/Umschalten]+[.] – Aufteilung nach links schieben
- [Windows-Taste]+[.] – Aufteilung nach rechts schieben
- [Windows-Taste]+[L] - Windows 8 sperren
- [Windows-Taste]+[F] – Suchen-App starten
- [Windows-Taste]+[C] – Charms Bar (Metro-Startmenü) öffnen
- [Windows-Taste]+[I] – Charm Bar (Metro-Sidebar) öffnen, um Windows 8 zum Beispiel herunterzufahren (Befehl "Power | Shut down")
- [Windows-Taste]+[K] – Connect Charm öffnen
- [Windows-Taste]+[H] – Apps-Suche unter dem Metro-Startmenü öffnen
- [Windows-Taste]+[Q]  - Apps-Übersicht einblenden
- [Windows-Taste]+[W] – Einstellungen für Such-App öffnen
- [Windows-Taste]+[Z] - App Bar öffnen

Kombination aus Maus- und Tastaturtaste für Desktopobjekte

- UMSCHALT+RECHTE MAUSTASTE: Kontextmenü anzeigen, das alternative Befehle enthält
- UMSCHALT+DOPPELKLICK: Alternativen Standardbefehl (zweites Element im Menü) ausführen
- ALT+DOPPELKLICK: Eigenschaften anzeigen
- UMSCHALT+ENTF: Objekt sofort löschen, ohne es im Papierkorb abzulegen

Tastenkombinationen für Desktop, Arbeitsplatz und Windows Explorer

Bei einem ausgewählten Objekt:

- F2: Objekt umbenennen
- F3: Alle Dateien suchen
- UMSCHALT+ENTF: Markiertes Element sofort löschen, ohne es im Papierkorb abzulegen
- ALT+EINGABE: Eigenschaftenfenster für das markierte Objekt öffnen

Allgemeine Tastaturbefehle

- F1: Windows-Hilfe anzeigen
- F10: Optionen der Menüleiste aktivieren
- UMSCHALT+F10: Kontextmenü für das ausgewählte Objekt öffnen (entspricht dem Klicken mit der rechten Maustaste auf ein Objekt)
- STRG+ESC: Das Menü Start öffnen (wählen Sie über die Pfeiltasten ein Objekt aus)
- STRG+ESC oder ESC: Wählt die Schaltfläche Start aus (Die TAB-Taste drücken, um die Taskleiste auszuwählen, oder UMSCHALT+F10 drücken, um ein Kontextmenü zu öffnen)
- STRG+UMSCHALT+ESC: Windows Task-Manager öffnen
- ALT+NACH-UNTEN-PFEIL: Dropdown-Listenfeld öffnen
- ALT+TAB: Zu einer anderen laufenden Anwendung wechseln (zum Anzeigen des Programmwechselfensters die ALT-Taste gedrückt halten und anschließend die TAB-Taste drücken)
- UMSCHALTTASTE: Die UMSCHALTTASTE beim Einlegen einer CD-ROM gedrückt halten, um die automatische Wiedergabe zu umgehen
- ALT+LEERTASTE: Systemmenü des Hauptfensters anzeigen (im Systemmenü können Sie das Fenster wiederherstellen, verschieben, die Größe ändern, minimieren, maximieren oder schließen)
- ALT+- (ALT+Bindestrich): Systemmenü des untergeordneten MDI-Fensters (Multiple Document Interface) anzeigen (im Systemmenü des untergeordneten MDI-Fensters können Sie das untergeordnete Fenster wiederherstellen, verschieben, die Größe ändern, minimieren, maximieren oder schließen)
- STRG+TAB: Zum nächsten untergeordneten Fenster einer MDI-Anwendung (Multiple Document Interface) wechseln
- ALT+unterstrichener Buchstabe im Menü: Entsprechendes Menü öffnen
- ALT+F4: Aktuelles Fenster schließen
- STRG+F4: Aktuelles MDI-Fenster (Multiple Document Interface) schließen
- ALT+F6: Zwischen mehreren Fenstern in der gleichen Anwendung wechseln (wird beispielsweise im Editor das Dialogfeld Suchen angezeigt, können Sie mit ALT+F6 zwischen dem Dialogfeld Suchen und dem Hauptfenster des Editors wechseln)

Tastenkombinationen für Eingabehilfen

- UMSCHALTTASTE fünfmal drücken: Einrastfunktion ein- und ausschalten
- Rechte UMSCHALTTASTE 8 Sekunden lang gedrückt halten: Anschlagverzögerung ein- und ausschalten
- NUM-Taste 5 Sekunden lang gedrückt halten: Statusanzeige ein- und ausschalten
- Linke ALT-Taste und linke UMSCHALTTASTE+NUM-Taste: Tastaturmaus ein- und ausschalten

Linke ALT-Taste und linke UMSCHALTTASTE+DRUCK-Taste: Kontrast ein- und ausschalten

### Environment Variables

- %ALLUSERSPROFILE% (%PROGRAMDATA%) → C:\\ProgramData
- %APPDATA% → C:\\Users{username}\\AppData\\Roaming
- %COMPUTERNAME% → hostname
- %COMMONPROGRAMFILES% → C:\\Program Files\\Common Files
- %COMMONPROGRAMFILES(x86)% → C:\\Program Files (x86)\\Common Files
- %COMSPEC% → Pfad zum Kommandozeilen-Interpreter
- %HOMEDRIVE%  → C:\\
- %HOMEPATH%  → \\Users{username}
- %LOCALAPPDATA%  → C:\\Users{username}\\AppData\\Local
- %PROGRAMFILES%  → C:\\Program Files
- %PROGRAMFILES(X86)%  → C:\\Program Files (x86)
- %USERPROFILE%  → C:\\Users{username}
- %WINDIR%  → C:\\Windows
- %PUBLIC%  → C:\\Users\\Public
- %PSModulePath%  → %SystemRoot%\\system32\\WindowsPowerShell\\v1.0\\Modules\\
