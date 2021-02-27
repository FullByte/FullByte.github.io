## Powershell

## Setup Powershell

Admin Rights required

**1. Install [Powershell 7](https://github.com/PowerShell/powershell/releases)**

A guide to follow is available here: https://docs.microsoft.com/de-de/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7

**2. Update [PowerShellGet](https://github.com/Azure/azure-powershell):**

```powershell
Install-PackageProvider -Name NuGet -Forces -scope AllUsers
Install-Module -Name PowerShellGet -Force -scope AllUsers
Update-Module -Name PowerShellGet -scope AllUsers
```

**3. Install Module for Azure**

Install the AZ Powershell Module, AzureAD and PSScriptAnalyzer with this command:

```powershell
Install-Module -Name Az -AllowClobber -Force -scope AllUsers
Install-Module -Name AzureAD -AllowClobber -Force -scope AllUsers
Install-Module -Name PSScriptAnalyzer -AllowClobber -Force -scope AllUsers
```

If you already have the modules installed consider updating them:

To update all modules run this command:

```powershell
Update-Module -scope AllUsers
```

## Powershell Basics

This chapter does not aim to teach powershell. Rather the scope is to teach proper scripting techniques, troubleshooting and collaboration when scripting.

### Verbose and Debug

PowerShell supports two optional parameters that can provide information about the execution of the cmdlet:

- "-Verbose" -> The -Verbose parameter displays any and all logging entries included by the cmdlet author, such as “Connecting to xyz”
- "-Debug"  -> The -Debug parameter displays any trace code implemented with a Write-Debug statement in the cmdlet, such as dumping the content of a variable.

### Required Tag

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

### Import Modules

Make sure to import all modules required.

Example:

```powershell
Import-Module -Name Az
```

### Privileges

Make sure you are admin if required

```powershell
#Requires -RunAsAdministrator
```

Run a process as non-admin from an elevated PowerShell console

```powershell
runas /trustlevel:0x20000 "powershell.exe -command 'whoami /groups |clip'"
```

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

### Code Documentation

Follow the Microsoft best-practice guidelines for code documentation in powershell scripts:
<https://docs.microsoft.com/de-de/powershell/scripting/gallery/concepts/publishing-guidelines?view=powershell-7.1>

## Troubleshooting

If you encounter an error, try running the same command in verbose mode.

Also helpful to get further information is running this command after the expected error:

```powershell
$Error[0].Exception | fl * -force
```

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
