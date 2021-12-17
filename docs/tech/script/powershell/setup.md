# Powershell Setup

## Windows

Admin Rights required

**1. Install [Powershell 7](https://github.com/PowerShell/powershell/releases)**

Run this command

```cmd
msiexec.exe /package PowerShell-7.1.2-win-x64.msi /quiet ADD_EXPLORER_CONTEXT_MENU_OPENPOWERSHELL=1 ENABLE_PSREMOTING=1 REGISTER_MANIFEST=1
```

- Latest Version: <https://aka.ms/powershell-release?tag=stable>
- Details: <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7>

**2. Update [PowerShellGet](https://github.com/Azure/azure-powershell)**

``` ps11
Register-PackageSource -Name MyNuGet -Location https://www.nuget.org/api/v2 -ProviderName NuGet
Install-PackageProvider -Name NuGet -Force
Install-Module -Name PowerShellGet -Force -AllowClobber
Update-Module -Name PowerShellGet
Get-PackageSource
```

**3. Install [Module for Azure](https://docs.microsoft.com/en-us/powershell/azure)**

Install the Powershell Modules you would like to use e.g.:

``` ps11
Install-Module -Name Az -AllowClobber -Force -scope AllUsers
Install-Module -Name AzureAD -AllowClobber -Force -scope AllUsers
Install-Module -Name PSScriptAnalyzer -AllowClobber -Force -scope AllUsers
```

Consider updating them from time to time with this command:

``` ps11
Update-Module -scope AllUsers -Force
```

## Linux

Install powershell on Ubuntu 20.04

``` sh
sudo apt update # Update the list of packages
sudo apt install -y wget apt-transport-https software-properties-common # Install pre-requisite packages.
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb # Download the Microsoft repository GPG keys
sudo dpkg -i packages-microsoft-prod.deb # Register the Microsoft repository GPG keys
sudo apt update # Update the list of products
sudo add-apt-repository universe # Enable the "universe" repositories
sudo apt install -y powershell # Install PowerShell
pwsh # Start PowerShell
```

Details: <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-7.1>

## Use the latest Modules

For example Az modules can be installed in various versions when updated.
Follow these three steps to update, find old modules and delete all but the latest:

**1. Update Az.Modules:**

``` ps11
Update-Module -Name Az
```

**2. Find out what versions you have installed**

``` ps11
Get-InstalledModule -Name Az -AllVersions | Select-Object -Property Name, Version
```

**3. Delete the older Module (or all and start over)**

Install the module "Az.Tools.Installer" to be able to delete an older Az Module version:

``` ps11
Install-Module -Name Az.Tools.Installer
Uninstall-AzModule -Name Az
```