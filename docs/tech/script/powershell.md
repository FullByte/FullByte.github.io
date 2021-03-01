# Powershell

## Setup Powershell Windows

Admin Rights required

**1. Install [Powershell 7](https://github.com/PowerShell/powershell/releases)**

Run this command

```cmd
msiexec.exe /package PowerShell-7.1.2-win-x64.msi /quiet ADD_EXPLORER_CONTEXT_MENU_OPENPOWERSHELL=1 ENABLE_PSREMOTING=1 REGISTER_MANIFEST=1
```

Latest Version: <https://aka.ms/powershell-release?tag=stable>
Details: <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7>

**2. Update [PowerShellGet](https://github.com/Azure/azure-powershell):**

```powershell
Install-PackageProvider -Name NuGet -Forces -scope AllUsers
Install-Module -Name PowerShellGet -Force -scope AllUsers
Update-Module -Name PowerShellGet -scope AllUsers
```

**3. Install Module for Azure**

Install the Powershell Modules you would like to use e.g.:

```powershell
Install-Module -Name Az -AllowClobber -Force -scope AllUsers
Install-Module -Name AzureAD -AllowClobber -Force -scope AllUsers
Install-Module -Name PSScriptAnalyzer -AllowClobber -Force -scope AllUsers
```

Consider updating them from time to time with this command:

```powershell
Update-Module -scope AllUsers -Force
```

## Setup Powershell Linux

Install powershell on Ubuntu 20.04

```bash
sudo apt-get update # Update the list of packages
sudo apt-get install -y wget apt-transport-https software-properties-common # Install pre-requisite packages.
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb # Download the Microsoft repository GPG keys
sudo dpkg -i packages-microsoft-prod.deb # Register the Microsoft repository GPG keys
sudo apt-get update # Update the list of products
sudo add-apt-repository universe # Enable the "universe" repositories
sudo apt-get install -y powershell # Install PowerShell
pwsh # Start PowerShell
```

Details: <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-7.1>

## Powershell Basics

This chapter does not aim to teach powershell. Rather the scope is to teach proper scripting techniques, troubleshooting and collaboration when scripting.

### Script Description

**Privileges**

Make sure you are admin if required

```powershell
#Requires -RunAsAdministrator
```

Run a process as non-admin from an elevated PowerShell console

```powershell
runas /trustlevel:0x20000 "powershell.exe -command 'whoami /groups |clip'"
```

**Required Tag**

Add a required tag for every script you create.
Some Examples:

```powershell
#Requires -Modules @{ ModuleName="Az"; ModuleVersion="5.0.0" }
```

It is usually best to use ModuleVersion to include new Versions. Here are the other options:

- ModuleVersion = equal or greater version
- RequiredVersion = equal to this version
- MaximumVersion = equal or lower version

Source: <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_requires?view=powershell-7>

**Import Modules**

Make sure to import all modules required.

Example:

```powershell
Import-Module -Name Az
```

**Code Documentation**

Follow the Microsoft best-practice guidelines for code documentation in powershell scripts:
<https://docs.microsoft.com/de-de/powershell/scripting/gallery/concepts/publishing-guidelines?view=powershell-7.1>

### Signing Script

Enabling to only run trusted, signed scripts is a good security measurement. This chapter will describe how to sign powershell scripts.

**Getting started**

- Current script execution policy: ```Get-ExecutionPolicy -List```
- Set execution policy for local user to signed only: ```Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser```
- Details on create certificate: ```certutil D:\cert.pfx```

**Create new self-signed cert.pfx**

```powershell
$Password = ConvertTo-SecureString -String "password" -Force -AsPlainText 
New-SelfSignedCertificate -subject "SelfSignedCert" -Type CodeSigning  | Export-PfxCertificate -FilePath "D:\cert2.pfx" -password $Password 
```

**Import cert.pfx to certificate store**

```powershell
Import-PfxCertificate -FilePath "D:\cert.pfx" -CertStoreLocation "cert:\LocalMachine\My" -Password $Password
Import-PfxCertificate -FilePath "D:\cert.pfx" -CertStoreLocation "cert:\LocalMachine\Root" -Password $Password
Import-PfxCertificate -FilePath "D:\cert.pfx" -CertStoreLocation "cert:\LocalMachine\TrustedPublisher" -Password $Password
```

**Sign script.ps1 with cert.pfx**

```powershell
$MyCert = Get-PfxCertificate -FilePath "D:\cert.pfx"
Set-AuthenticodeSignature "script.ps1" -Certificate $MyCert
```

- Option 1: Use a timestamp server ```Set-AuthenticodeSignature "script.ps1" -Certificate $MyCert -IncludeChain "All" -TimestampServer "http://timestamp.verisign.com/scripts/timstamp.dll"```
- Option 2: Bulk sign scripts ```get-childitem *.ps1 | Set-AuthenticodeSignature -Certificate $MyCert```

**Check the script signer details**

Status is "UnknownError" if not added to CertStore, else "valid"

```powershell
Get-AuthenticodeSignature "script.ps1" | select-object *

$Thumbprint = Get-AuthenticodeSignature "script.ps1" | Select-Object -First 1 -ExpandProperty SignerCertificate | Select-Object -First 1 -ExpandProperty Thumbprint
Get-ChildItem Cert:\LocalMachine\TrustedPublisher\ | Where-object { $_.thumbprint -eq $Thumbprint}
```

## Troubleshooting

If you encounter an error, try running the same command in verbose mode.

Also helpful to get further information is running this command after the expected error:

```powershell
$Error[0].Exception | fl * -force
```

### Verbose and Debug

PowerShell supports two optional parameters that can provide information about the execution of the cmdlet:

- "-Verbose" -> The -Verbose parameter displays any and all logging entries included by the cmdlet author, such as “Connecting to xyz”
- "-Debug"  -> The -Debug parameter displays any trace code implemented with a Write-Debug statement in the cmdlet, such as dumping the content of a variable.

### Use the latest Modules

For example Az modules can be installed in various versions when updated.
Follow these three steps to update, find old modules and delete all but the latest:

**1. Update Az.Modules:**

```powershell
Update-Module -Name Az
```

**2. Find out what versions you have installed**

```powershell
Get-InstalledModule -Name Az -AllVersions | Select-Object -Property Name, Version
```

**3. Delete the older Module (or all and start over)**

Install the module "Az.Tools.Installer" to be able to delete an older Az Module version:

```powershell
Install-Module -Name Az.Tools.Installer
Uninstall-AzModule -Name Az
```
