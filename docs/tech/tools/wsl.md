# WSL

Some helpful [commands](https://docs.microsoft.com/en-us/windows/wsl/basic-commands):

- Check for updates: ```wsl --update```
- List all available WSL distributions: ```wsl --list --online```
- List locally installed distros: ```wsl --list --verbose```
- Install a distribution: ```wsl --install -d Ubuntu-22.10```
- Delete Distro: ```wsl --unregister Ubuntu-22.10```
- Set default distro: ```wsl --set-default Ubuntu-22.10```
- Open WSL in pwsh: ```wsl --distribution Ubuntu-22.10 --user fab1```
- Restart WSL: ```Get-Service LxssManager | Restart-Service``` or```wsl --shutdown```
- Change distro to version 2: ```wsl --set-version kali-linux 2```*

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

In this `wsl.conf` example, the distribution is `Ubuntu-22.10` and the file path is `\\wsl.localhost\Ubuntu-22.10\etc\wsl.conf`.

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
