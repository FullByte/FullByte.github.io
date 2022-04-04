# Windows Apps

See the tools section for useful windows applications. This is a list of microsoft native/own tools.

## WinGet

- Source: <https://github.com/microsoft/winget-cli>
- Store: <https://www.microsoft.com/en-us/p/app-installer/9nblggh4nns1>
- Docs: <https://docs.microsoft.com/en-us/windows/package-manager/>

Example:

``` ps1
winget install powertoys 
```

## File Recovery

Store: <https://www.microsoft.com/en-us/p/windows-file-recovery/9n26s50ln705?activetab=pivot:overviewtab>

Recover a specific file from your C: drive to the recovery folder on an E: drive.

``` ps1
winfr C: E: /n \Users\<username>\Documents\QuarterlyStatement.docx
```

Recover jpeg and png photos from your Pictures folder to the recovery folder on an E: drive.

``` ps1
winfr C: E: /n \Users\<username>\Pictures\*.JPEG /n \Users\<username>\Pictures\*.PNG
```

Recover your Documents folder from your C: drive to the recovery folder on an E: drive.

``` ps1
winfr C: E: /n \Users\<username>\Documents\ 
```

Recover PDF and Word files from your C: drive to the recovery folder on an E: drive.

``` ps1
winfr C: E: /r /n *.pdf /n *.docx
```

Recover any file with the string "invoice" in the filename by using wildcard characters.

``` ps1
winfr C: E: /r /n *invoice* 
```

## Sysinternals Suite

[Sysinternals Suite](https://www.microsoft.com/en-us/p/sysinternals-suite/9p7knl5rwt25#activetab=pivot:overviewtab) is a bundle of the Sysinternals utilities including Process Explorer, Process Monitor, Sysmon, Autoruns, ProcDump, all of the PsTools, and many more.

## Size Bench

SizeBench is a utility that analyzes PDB information to help you optimize and reduce the size of your binaries (DLLs, EXEs, and other PE files). You can break down a binary by sections of the PE file, COFF Groups, static libraries, OBJ file, even by source file - to see which parts of your code and data contribute meaningfully to on-disk and in-memory size. SizeBench can also run heuristic analyses to help you find likely sources of waste, including inefficient usage of virtual functions, duplicated data, and C++ templated code that is "almost foldable" to look for quick opportunities to reduce size.

- Store: <https://www.microsoft.com/en-us/p/sizebench/9ndf4n1wg7d6#activetab=pivot:overviewtab>
- Blog Post: <https://devblogs.microsoft.com/performance-diagnostics/sizebench-a-new-tool-for-analyzing-windows-binary-size/>

## Snip & Sketch (Screenshot)

[Download Snip & Sketch from the store](https://www.microsoft.com/en-us/p/snip-sketch/9mz95kl8mr0l?activetab=pivot:overviewtab)

Take screenshot: Windows + Shift + S

## Record Screen

- Start recording mode: Windows + G
- start recording: Window + Alt + R

## Windows Terminal

- Store: <https://www.microsoft.com/de-de/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab>
- Doc: <https://docs.microsoft.com/en-us/windows/terminal/>

Open a new Terminal Window with powershell 7, cmd and WSL (in my case ubuntu)

``` ps1
wt -p "PowerShell 7" `; split-pane -p "cmd" `; split-pane -H wsl.exe
```

### Customized command prompt

Install the required modules

``` ps1
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
```

Check available themes:

``` ps1
Get-PoshThemes
```

If this doesn't look good install a font that works e.g. [NerdFonts](https://www.nerdfonts.com/).

Now update $PROFILE to load modules with every start

``` ps1
echo "Import-Module posh-git") >> $PROFILE
echo "Import-Module oh-my-posh" >> $PROFILE
```

Add the Theme you like as well e.g. paradox:

``` ps1
echo "Set-PoshPrompt -Theme paradox" >> $PROFILE
```

### settings.json

Edit the "settings.json" and add under "profiles", "defaults" a line for a font you like e.g.:

```json
"fontFace": "MesloLGM NF"
```

## WSL

Some helpful [commands](https://docs.microsoft.com/en-us/windows/wsl/basic-commands):

- Check for updates: ```wsl --update```
- List all available WSL distributions: ```wsl --list --online```
- List locally installed distros: ```wsl --list --verbose```
- Install a distribution: ```wsl --install -d Ubuntu-20.04```
- Delete Distro: ```wsl --unregister Ubuntu-18.04```
- Set default distro: ```wsl --set-default Ubuntu-20.04```
- Open WSL in pwsh: ```wsl --distribution Ubuntu-20.04 --user fab1```
- Restart WSL: ```Get-Service LxssManager | Restart-Service``` or```wsl --shutdown```
- Change distro to version 2: ```wsl --set-version kali-linux 2```*

wsl --distribution Ubuntu-20.04 --user fab1

Note that the root password is set random and needs to be updated using ```sudo passwd```

*This may require installing the following

``` ps1
(New-Object System.Net.WebClient).DownloadFile("https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi", "wsl_update_x64.msi") 
Start-Process msiexec.exe -Wait -ArgumentList '/I wsl_update_x64.msi /quiet'
```

[Mount Linux File System](https://docs.microsoft.com/de-de/windows/wsl/wsl2-mount-disk)

List devices (choose the drive you want to mount) ```wmic diskdrive list brief```, then mount partition 1 of "PHYSICALDRIVE3" and open it:

``` ps1
wsl --mount \\.\PHYSICALDRIVE3 --partition 1
wsl
cd /mnt/wsl/PHYSICALDRIVE3p1/
```

To configure WSL there are [2 main config files](https://docs.microsoft.com/en-us/windows/wsl/wsl-config): `.wslconfig` and `wsl.conf`

- `.wslconfig` located in the Windows %UserProfile% directory to configure settings globally across all installed distributions.
- `wsl.conf` located in the /etc directory of the WSL distro to configure settings per-distribution.

In this `wsl.conf` example, the distribution is `Ubuntu-20.04` and the file path is `\\wsl.localhost\Ubuntu-20.04\etc\wsl.conf`.

``` ps1
# Automatically mount Windows drive when the distribution is launched
[automount]

# Set to true will automount fixed drives (C:/ or D:/) with DrvFs under the root directory set above. Set to false means drives won't be mounted automatically, but need to be mounted manually or with fstab.
enabled = true

# Sets the directory where fixed drives will be automatically mounted. This example changes the mount location, so your C-drive would be /c, rather than the default /mnt/c. 
root = /

# DrvFs-specific options can be specified.  
options = "metadata,uid=1003,gid=1003,umask=077,fmask=11,case=off"

# Sets the `/etc/fstab` file to be processed when a WSL distribution is launched.
mountFsTab = true

# Network host settings that enable the DNS server used by WSL 2. This example changes the hostname, sets generateHosts to false, preventing WSL from the default behavior of auto-generating /etc/hosts, and sets generateResolvConf to false, preventing WSL from auto-generating /etc/resolv.conf, so that you can create your own (ie. nameserver 1.1.1.1).
[network]
hostname = wslvm
generateHosts = false
generateResolvConf = false

# Set whether WSL supports interop process like launching Windows apps and adding path variables. Setting these to false will block the launch of Windows processes and block adding $PATH environment variables.
[interop]
enabled = false
appendWindowsPath = false

# Set the user when launching a distribution with WSL.
[user]
default = 0xfab1

# Set a command to run when a new WSL instance launches. This example starts the Docker container service.
[boot]
command = service docker start
```

By default `.wslconfig` is located here: `C:\Users\<UserName>\.wslconfig`.

``` ps1
# Settings apply across all Linux distros running on WSL 2
[wsl2]

# Limits VM memory to use no more than 4 GB, this can be set as whole numbers using GB or MB
memory=4GB 

# Sets the VM to use two virtual processors
processors=2

# Specify a custom Linux kernel to use with your installed distros. The default kernel used can be found at https://github.com/microsoft/WSL2-Linux-Kernel
kernel=C:\\temp\\myCustomKernel

# Sets additional kernel parameters, in this case enabling older Linux base images such as Centos 6
kernelCommandLine = vsyscall=emulate

# Sets amount of swap storage space to 8GB, default is 25% of available RAM
swap=8GB

# Sets swapfile path location, default is %USERPROFILE%\AppData\Local\Temp\swap.vhdx
swapfile=C:\\temp\\wsl-swap.vhdx

# Disable page reporting so WSL retains all allocated memory claimed from Windows and releases none back when free
pageReporting=false

# Turn off default connection to bind WSL 2 localhost to Windows localhost
localhostforwarding=true

# Disables nested virtualization
nestedVirtualization=false

# Turns on output console showing contents of dmesg when opening a WSL 2 distro for debugging
debugConsole=true
```
