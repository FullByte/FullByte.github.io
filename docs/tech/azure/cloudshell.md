# Azure Cloud Shell

## Info

|What|Where|
|-|-|
|Official Page||
|Online|<https://shell.azure.com/>|

## Attach Storage

- Add FileShare to Cloud Shell: ```clouddrive mount -s <secret> -g <rg-name> -n <fileshare> -f <share>```
- Show Drives: ```Get-CloudDrive```

Link: <https://docs.microsoft.com/de-de/azure/cloud-shell/persisting-shell-storage>

## Connect to VM console

You can access an Azure VM within the Azure Cloud Shell.
<https://docs.microsoft.com/de-de/azure/cloud-shell/quickstart-powershell>

Enable remoting if not yet done:

```powershell
Enable-AzVMPSRemoting -Name MyVM1 -ResourceGroupname MyResourceGroup
```

Execute script on VM:

```powershell
Invoke-AzVMCommand -Name MyVM1 -ResourceGroupName MyResourceGroup -Scriptblock {Get-ComputerInfo} -Credential (Get-Credential)
```

Enter VMs commandline:

```powershell
Enter-AzVM -Name MyVM1 -ResourceGroupName MyResourceGroup -Credential (Get-Credential)
```

## Enhance CloudShell Bash

**Posh-Git** provides us with information at the command line about the state of the current repository we are in. It also provides tab completion for Git commands.
<https://github.com/dahlbyk/posh-git>

```powershell
install-module posh-git
import-module posh-git
```

**Oh-My-Posh** allows you to theme your prompt with various color schemes, Git status indicators, Admin status and many other things.
<https://github.com/JanDeDobbeleer/oh-my-posh>

```powershell
Install-Module oh-my-posh
Import-module oh-my-posh
```

**Get-ChildItemColor** is a simple tool which adds color coding to the get-childitem command. When you run this command, you get different colors used for folders vs. files and different file types.
<https://github.com/joonro/Get-ChildItemColor>

```powershell
Install-Module Get-ChildItemColor
Import-Module Get-ChildItemColor
```
