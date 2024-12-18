# Advice

This section does not aim to teach powershell. Rather the scope is to teach proper scripting techniques, troubleshooting and collaboration when scripting.

## Languages

In case you run a command and want to query e.g. windows commands the result/keywords to look for may vary per language

Create a hash table with an expected search string entry per language:

``` ps1
$keyword = @{"de-DE" = 'Schlüsselinhalt'; "en-US" = 'Key Content'}
```

Then call the correct entry with```get-culture```:

``` ps1
echo something | Select-String ($keyword[(get-culture).Name])
```

## Variables

**Path variables**

Powershell defaults paths:

- Script location: ```$PSScriptRoot```
- Current location when the script is running: ```$PWD```
- User's home directory: ```$HOME```
- Script that invoked the current command (only populated if caller is a script): ```$PSCommandPath```

.NET Environment paths:

You can also use the [.NET Environment.SpecialFolder](https://docs.microsoft.com/en-us/dotnet/api/system.environment.specialfolder) Enum e.g.:

``` ps1
$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)
$DocumentsPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::CommonDocuments)
$ProgramFilesX86Path = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::ProgramFilesX86 )
$ProgramFilesPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::ProgramFiles)
$RecentFilesPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Recent)
$SendToPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::SendTo)
$UserProfilePath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::UserProfile)
$StartupPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Startup)
```

**Other variables:**

- First token in the last line received by the session: ```$^```
- Last token in the last line received by the session: ```$$```
- Execution status (true/false) on if the last command succeeded: ```$?```
- Current object in the pipeline object: ```$_``` or```$PSItem```
- Array of error objects: ```$Error``` e.g. first error entry =```$Error[0]```
- Check OS with: ```$IsLinux``` or```$IsMacOS``` or```$IsWindows```
- Use True/False with these : ```$true``` and```$false```
- Details on user who started the PSSession: ```$PSSenderInfo```
- Get version details of the run environment: ```$PSVersionTable``` e.g.```$PSVersionTable.PSVersion``` or```$PSVersionTable.OS```

## Script Description

### Privileges

Make sure you are admin if required

``` ps1
#Requires -RunAsAdministrator
```

Run a process as non-admin from an elevated PowerShell console

``` ps1
runas /trustlevel:0x20000 "powershell.exe -command 'whoami /groups |clip'"
```

Check the current privileges:

``` ps1
#Requires -RunAsAdministrator
[bool]([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
[bool](([System.Security.Principal.WindowsIdentity]::GetCurrent()).groups -match "S-1-5-32-544")
```

### Required Modules

**Add a required tag for every script you create.**

Some Examples:

``` ps1
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

``` ps1
Import-Module -Name Az
```

### Code Documentation

Follow the Microsoft best-practice guidelines for code documentation in powershell scripts:
<https://docs.microsoft.com/de-de/powershell/scripting/gallery/concepts/publishing-guidelines?view=powershell-7.1>

## Signing Script

Enabling to only run trusted, signed scripts is a good security measurement. This chapter will describe how to sign powershell scripts.

**Getting started**

- Current script execution policy: ```Get-ExecutionPolicy -List```
- Set execution policy for local user to signed only: ```Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser```
- Details on create certificate: ```certutil D:\cert.pfx```

**Create new self-signed cert.pfx**

``` ps1
$Password = ConvertTo-SecureString -String "password" -Force -AsPlainText 
New-SelfSignedCertificate -subject "SelfSignedCert" -Type CodeSigning  | Export-PfxCertificate -FilePath "D:\cert.pfx" -password $Password 
```

**Import cert.pfx to certificate store**

``` ps1
Import-PfxCertificate -FilePath "D:\cert.pfx" -CertStoreLocation "cert:\LocalMachine\My" -Password $Password
Import-PfxCertificate -FilePath "D:\cert.pfx" -CertStoreLocation "cert:\LocalMachine\Root" -Password $Password
Import-PfxCertificate -FilePath "D:\cert.pfx" -CertStoreLocation "cert:\LocalMachine\TrustedPublisher" -Password $Password
```

**Sign script.ps1 with cert.pfx**

``` ps1
$MyCert = Get-PfxCertificate -FilePath "D:\cert.pfx"
Set-AuthenticodeSignature "script.ps1" -Certificate $MyCert
```

- Option 1: Use a timestamp server```Set-AuthenticodeSignature "script.ps1" -Certificate $MyCert -IncludeChain "All" -TimestampServer "http://timestamp.verisign.com/scripts/timstamp.dll"```
- Option 2: Bulk sign scripts```get-childitem *.ps1 | Set-AuthenticodeSignature -Certificate $MyCert```

**Check the script signer details**

Status is "UnknownError" if not added to CertStore, else "valid"

``` ps1
Get-AuthenticodeSignature "script.ps1" | select-object *

$Thumbprint = Get-AuthenticodeSignature "script.ps1" | Select-Object -First 1 -ExpandProperty SignerCertificate | Select-Object -First 1 -ExpandProperty Thumbprint
Get-ChildItem Cert:\LocalMachine\TrustedPublisher\ | Where-object { $_.thumbprint -eq $Thumbprint}
```

## Encrypt Files with Powershell and Certificates

The following variables are required. Additionally you need a cert name and password but this will be queried in this example.

``` ps1
$path = "D:\test.txt"
$pwcert = "password"
```

It is important do create/use a certificate with the properties or "KeyUsage" KeyEncipherment, DataEncipherment, KeyAgreement. In case you have created a certificate without specifically mentioning this feature it may not be available and file encryption/decryption will fail.

The following script will prepare a certificate or use a given one:

``` ps1
$hascert=Read-Host -Prompt 'Do you have a certificate for file encryption? (Y/N)?'
If ($hascert -eq 'Y') {
    Write-Output 'Select Certificate.' 
    $mycert=Get-Childitem Cert:\CurrentUser\My
    $cert=$mycert | Where-Object hasprivatekey -eq 'true' | Select-Object -Property Issuer,Subject,HasPrivateKey | Out-GridView -Title 'Select Certificate' -PassThru
}
If ($hascert -eq 'N') {
    Write-Output 'This section creates a new self signed certificate. Provide certificate name.'
    $newcert=Read-Host 'Enter Certificate Name'
    New-SelfSignedCertificate -DnsName $newcert -CertStoreLocation "Cert:\CurrentUser\My" -KeyUsage KeyEncipherment,DataEncipherment,KeyAgreement -Type DocumentEncryptionCert
    $cert=Get-ChildItem -Path Cert:\CurrentUser\My\ | Where-Object subject -like "*$newcert*"
    $thumb=$cert.thumbprint
    Export-PfxCertificate -Cert Cert:\CurrentUser\My\$thumb -FilePath $home\"cert_"$env:username".pfx" -Password $pwcert 
}
```

Now that we have everything setup we can encrypt/decrypt a given file:

``` ps1
$enc=Read-Host -Prompt 'Do you want to [e]ncrypt or [d]ecrypt the file? (E/D)?'
If ($enc -eq 'E') {
    Get-Content $path | Protect-CmsMessage -To $cert.Subject -OutFile $path
}
If ($enc -eq 'D') {
    $message = Unprotect-CmsMessage -Path $path -To $cert.Subject
    Set-Content -Path $path -Value $message
}
```

## Parallel tasks and throttle limit

Example running 10x 1sec sleep single thread, parallel, parallel optimized:

``` ps1
#Requires -Version 7
Measure-Command -expression {1..10 | foreach-object {Start-Sleep -seconds 1}} # Serial Execution of 10 tasks of 1 seconds
Measure-Command -expression {1..10 | foreach-object -parallel {Start-Sleep -seconds 1}} # Parallel Execution of 10 tasks of 1 seconds
Measure-Command -expression {1..10 | foreach-object -parallel {Start-Sleep -seconds 1} -throttlelimit 10} #Setting Throttlelimit to 10 instead 5 (default value)
```

## Logging

Adding log (better: event-logs) helps understand what went wrong and why things are they way they currently are.

General logging:

``` ps1
Function writeEventLogEntry
{
    $message = "$args[0] Time: " + (get-date).ToString('yyyy-MM-dd HH:mm:ss') + " User: " + $env:userdomain + "\" + $env:username
    if ($args[1] -eq "Information") {
        write-eventlog -logname "Windows PowerShell" -source PowerShell -eventID 1999 -entrytype Information -message $message -category 1 -rawdata 10,20    }
    elseif ($args[1] -eq "Warning") {
        write-eventlog -logname "Windows PowerShell" -source PowerShell -eventID 1999 -entrytype Warning -message $message -category 1 -rawdata 10,20    }
    elseif ($args[1] -eq "Error") {
        write-eventlog -logname "Windows PowerShell" -source PowerShell -eventID 1999 -entrytype Error -message $message -category 1 -rawdata 10,20    }
}
```

## Verbose and Debug

PowerShell supports two optional parameters that can provide information about the execution of the cmdlet:

- "-Verbose" → The -Verbose parameter displays any and all logging entries included by the cmdlet author, such as "Connecting to xyz"
- "-Debug"  → The -Debug parameter displays any trace code implemented with a Write-Debug statement in the cmdlet, such as dumping the content of a variable.

**Option 1)** With a value of 1 you get each line of code as it executes, e.g.:

``` ps1
Set-PSDebug -Trace 1
Get-PSDepth
```

With a value of 2 you also get variable assignments and code paths:

``` ps1
Set-PSDebug -Trace 2
Get-PSDepth
```

**Option 2)** Use the below in your script.

``` ps1
$VerbosePreference="Continue"
```

Option 3) Some commands have an -verbose or -v parameter

Example missing

Also helpful to get further information is running this command after the expected error:

``` ps1
$Error[0].Exception | fl * -force
```

Start/Stop the debugger

``` ps1
Start Debugging
Set-PSDebug -step

Stop Debugging
Set-PSDebug -stop
```
