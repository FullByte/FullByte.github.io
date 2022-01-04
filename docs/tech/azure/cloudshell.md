# Azure Cloud Shell

| What              | Where                                                                                                                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Official Page     | <https://azure.microsoft.com/en-us/features/cloud-shell/>                                                                        |
| Docs              | <https://docs.microsoft.com/en-us/azure/cloud-shell/overview>                                                                    |
| Online            | <https://shell.azure.com/> </br> <https://portal.azure.com/#cloudshell/>                                                         |
| Cloud Shell Tools | <https://docs.microsoft.com/en-us/azure/cloud-shell/features> </br> <https://build5nines.com/azure-cloud-shell-tips-and-tricks/> |

Further Links

- persisting-shell-storage <https://docs.microsoft.com/en-us/azure/cloud-shell/persisting-shell-storage>

## Cloud Shell options

There are three options to use the cloud shell: Docker, Windows Terminal and the Azure Web Interface:

### Docker

You get a [CloudShell](https://github.com/Azure/CloudShell) container as follows:

``` ps1
docker run -it mcr.microsoft.com/azure-cloudshell /bin/bash # for bash
docker run -it mcr.microsoft.com/azure-cloudshell /usr/bin/pwsh # for powershell
```

### Windows Terminal

The [Windows terminal](https://docs.microsoft.com/de-de/windows/terminal/) has the cloud shell integrated. Aside from other features this is a good way to interact with azure on command line.

Install the windows terminal with```choco install microsoft-windows-terminal```.
You need to login to azure first to use the terminal.

### Azure Portal

Go to <https://shell.azure.com> and you are logged in with your current user.

To get a GUI editor in the web run```code .```.

## Attach Storage

- Add FileShare to Cloud Shell:```clouddrive mount -s <secret> -g <rg-name> -n <fileshare> -f <share>```
- Show Drives:```Get-CloudDrive```
- Remove or re-configure your cloud drive:```dismount-clouddrive```

Sources:

- <https://docs.microsoft.com/de-de/azure/cloud-shell/persisting-shell-storage>

## Connect to VM console

You can access an Azure VM within the Azure Cloud Shell.
<https://docs.microsoft.com/de-de/azure/cloud-shell/quickstart-powershell>

Enable remoting if not yet done:

``` ps1
Enable-AzVMPSRemoting -Name MyVM1 -ResourceGroupname MyResourceGroup
```

Execute script on VM:

``` ps1
Invoke-AzVMCommand -Name MyVM1 -ResourceGroupName MyResourceGroup -Scriptblock {Get-ComputerInfo} -Credential (Get-Credential)
```

Enter VMs commandline:

``` ps1
Enter-AzVM -Name MyVM1 -ResourceGroupName MyResourceGroup -Credential (Get-Credential)
```

## Enhance CloudShell Bash

**Posh-Git** provides us with information at the command line about the state of the current repository we are in. It also provides tab completion for Git commands.
<https://github.com/dahlbyk/posh-git>

``` ps1
install-module posh-git
import-module posh-git
```

**Oh-My-Posh** allows you to theme your prompt with various color schemes, Git status indicators, Admin status and many other things.
<https://github.com/JanDeDobbeleer/oh-my-posh>

``` ps1
Install-Module oh-my-posh
Import-module oh-my-posh
```

**Get-ChildItemColor** is a simple tool which adds color coding to the get-childitem command. When you run this command, you get different colors used for folders vs. files and different file types.
<https://github.com/joonro/Get-ChildItemColor>

``` ps1
Install-Module Get-ChildItemColor
Import-Module Get-ChildItemColor
```
