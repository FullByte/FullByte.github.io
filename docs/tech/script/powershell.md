# Powershell

## Setup Powershell

### Windows

Admin Rights required

**1. Install [Powershell 7](https://github.com/PowerShell/powershell/releases)**

Run this command

```cmd
msiexec.exe /package PowerShell-7.1.2-win-x64.msi /quiet ADD_EXPLORER_CONTEXT_MENU_OPENPOWERSHELL=1 ENABLE_PSREMOTING=1 REGISTER_MANIFEST=1
```

- Latest Version: <https://aka.ms/powershell-release?tag=stable>
- Details: <https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7>

**2. Update [PowerShellGet](https://github.com/Azure/azure-powershell)**

```powershell
Install-PackageProvider -Name NuGet -Forces -scope AllUsers
Install-Module -Name PowerShellGet -Force -scope AllUsers
Update-Module -Name PowerShellGet -scope AllUsers
```

**3. Install [Module for Azure](https://docs.microsoft.com/en-us/powershell/azure)**

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

### Linux

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

## Powershell Tipps

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
New-SelfSignedCertificate -subject "SelfSignedCert" -Type CodeSigning  | Export-PfxCertificate -FilePath "D:\cert.pfx" -password $Password 
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

### Encrypt Files with Powershell and Cerficates

The following variables are required. Additionally you need a cert name and password but this will be queried in this example.

```powershell
$path = "D:\test.txt"
$pwcert = "password"
```

It is important do create/use a certificate with the properties or "KeyUsage" KeyEncipherment, DataEncipherment, KeyAgreement. In case you have created a certificate without specifically mentioning this feature it may not be available and file encryption/decryption will fail.

The following script will prepare a certificate or use a given one:

```powershell
$hascert=Read-Host -Prompt 'Do you have a certificate for file encryption? (Y/N)?'
If ($hascert -eq 'Y') {
    Write-Host 'Select Certificate.' 
    $mycert=Get-Childitem Cert:\CurrentUser\My
    $cert=$mycert | Where-Object hasprivatekey -eq 'true' | Select-Object -Property Issuer,Subject,HasPrivateKey | Out-GridView -Title 'Select Certificate' -PassThru
}
If ($hascert -eq 'N') {
    Write-Host 'This section creates a new self signed certificate. Provide certificate name.'
    $newcert=Read-Host 'Enter Certificate Name'
    New-SelfSignedCertificate -DnsName $newcert -CertStoreLocation "Cert:\CurrentUser\My" -KeyUsage KeyEncipherment,DataEncipherment,KeyAgreement -Type DocumentEncryptionCert
    $cert=Get-ChildItem -Path Cert:\CurrentUser\My\ | Where-Object subject -like "*$newcert*"
    $thumb=$cert.thumbprint
    Export-PfxCertificate -Cert Cert:\CurrentUser\My\$thumb -FilePath $home\"cert_"$env:username".pfx" -Password $pwcert 
}
```

Now that we have everything setup we can encrypt/decrypt a given file:

```powershell
$enc=Read-Host -Prompt 'Do you want to [e]ncrypt or [d]ecrypt the file? (E/D)?'
If ($enc -eq 'E') {
    Get-Content $path | Protect-CmsMessage -To $cert.Subject -OutFile $path
}
If ($enc -eq 'D') {
    $message = Unprotect-CmsMessage -Path $path -To $cert.Subject
    Set-Content -Path $path -Value $message
}
```

### Parallel tasks and throttle limit

Example running 10x 1sec sleep single thread, parallel, parallel optimized:

```powershell
#Requires -Version 7
Measure-Command -expression {1..10 | foreach-object {Start-Sleep -seconds 1}} # Serial Execution of 10 tasks of 1 seconds
Measure-Command -expression {1..10 | foreach-object -parallel {Start-Sleep -seconds 1}} # Parallel Execution of 10 tasks of 1 seconds
Measure-Command -expression {1..10 | foreach-object -parallel {Start-Sleep -seconds 1} -throttlelimit 10} #Setting Throttlelimit to 10 instead 5 (default value)
```

## Snippets

Some handy code snippets for powershell :)

### String manipulation

**Base64 Decode/Encode**

- Decode: ```[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("dGVzdA=="))```
- Encode: ```[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("test"))```

**Create files based on files**

Create md file for each file found in current folder and remove first and last chars:

```powershell
foreach ($file in (dir | select-object name)){New-Item ($file.name.Substring(3, $file.name.Length-7)+".md") -ItemType file}
```

**Create a password**

Option 1

```powershell
Function New-Password([int] $length, $pw = "")
{    
    $rng = New-Object System.Random
    for($i=0;$i -lt $length;$i++) { $pw = $pw +[char]$rng.next(33,126) }
    return $pw
}
New-Password 15
```

Option 2

```powershell
$pwlength = 20 # Something between 8 and 32

# Create a password
Function New-RandomPassword{
    Param([ValidateRange(8, 32)] [int] $Length = 16)
    $AsciiCharsList = @()

    foreach ($a in (33..126)){ $AsciiCharsList += , [char][byte]$a }

    do {
        $Password = ""
        $loops = 1..$Length
        Foreach ($loop in $loops) { $Password += $AsciiCharsList | Get-Random }
    }
    until ($Password -match "(?=^.{8,32}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9])(?=.*[a-z])|(?=.*[^A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9]))^.*")
    return $Password
}

# Looks cool and why use the first best choice? lol
for ($i = 0; $i -lt ($pwlength); $i++) {
    $line = ""
    for ($j = 0; $j -lt (5); $j++) { $line += "$(New-RandomPassword($pwlength)) " }
    Write-Host($line) -ForegroundColor Green
}

# Result
Write-Host("Password:") -ForegroundColor black -BackgroundColor yellow -NoNewline; Write-Host(" " + $(New-RandomPassword($pwlength))) -ForegroundColor Red
```

Option 3

```powershell
$buffer = New-Object byte[] 32;
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes(($buffer));
return [BitConverter]::ToString($buffer).Replace("-", [string]::Empty);
```


### System information

**Last boot time**

```powershell
Write-Host "System boot:" (Get-CimInstance -ClassName win32_operatingsystem | Select-Object -ExpandProperty LastBootUpTime)
```

**Get WinSAT information**

```powershell
# Run WinSAT (optional)
WinSAT formal

# Get WinSAT Data (XML)
$path = Get-ChildItem -Path 'C:\Windows\Performance\WinSAT\DataStore\*Formal.*.xml' | Sort-Object -Property CreationTime -Descending | Select-Object -First 1 -ExpandProperty FullName

# Parse as XML
$xml = [xml]::new()
$xml.Load($Path)

# Read XML
$node = $xml.WinSAT.Metrics.CPUMetrics.CompressionMetric
'CPU Compression Performance is {0} {1}' -f $node.'#text', $node.units
'CPU Manufacturer is {0} ' -f $xml.WinSAT.SystemConfig.Processor.Instance.Signature.Manufacturer.friendly
```

**Windows Defender Stats**

```powershell
$DefenderStatus = (Get-Service WinDefend -ErrorAction SilentlyContinue).Status
if ($DefenderStatus -ne "Running") {
    throw "The Windows Defender service is not currently running"
}
Get-MpComputerStatus
```

**Install apps**

Get install apps from app-store

```powershell
Get-AppxPackage | Select-Object -Property Name, Status, Version, InstallLocation | Format-Table
```

List all programs installed on Windows (and ignore the ones from Microsoft)

```powershell
Get-WMIObject -Query "SELECT * FROM Win32_Product Where Not Vendor Like '%Microsoft%'" | Format-Table
```

List files in programs folder:

```powershell
$Path = "$Env:ProgramData\Microsoft\Windows\Start Menu\Programs"
$StartMenu = Get-ChildItem $Path -Recurse -Include *.lnk

ForEach ($Item in $StartMenu) {
   $Shell = New-Object -ComObject WScript.Shell
   $Properties = @{
        ShortcutName = $Item.Name
        Target = $Shell.CreateShortcut($Item).targetpath
        }
    New-Object PSObject -Property $Properties
}

[Runtime.InteropServices.Marshal]::ReleaseComObject($Shell) | Out-Null
```

List installed Windows Store Apps (and ignore some):

```powershell
#Requires -RunAsAdministrator

Import-Module Appx
$Packages = Get-AppxPackage

## Ignore MS Stuff
$Whitelist = @(
    '*WindowsCalculator*',
    '*MSPaint*',
    '*Office.OneNote*',
    '*Microsoft.net*',
    '*MicrosoftEdge*',
    '*Microsoft*'
)

## Remove all things to ignore
ForEach($App in $Packages){
    $Matched = $false
    Foreach($Item in $Whitelist){
        If($App -like $Item){
            $Matched = $true
            break
        }
    }

    if($matched -eq $false){
        [PSCustomObject]@{
        Name = $App.Name
        Location = $App.InstallLocation
        }
    }
}
```

### System Config

Enable Remote Desktop

```powershell
(Get-WmiObject Win32_TerminalServiceSetting -Namespace root\cimv2\TerminalServices).SetAllowTsConnections(1,1) | Out-Null
(Get-WmiObject -Class "Win32_TSGeneralSetting" -Namespace root\cimv2\TerminalServices -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0) | Out-Null
Get-NetFirewallRule -DisplayName "Remote Desktop*" | Set-NetFirewallRule -enabled true
```

### Take a screenshot

Take a screenshot and save the image on your desktop:

```powershell
Add-Type -AssemblyName System.Windows.Forms
Add-type -AssemblyName System.Drawing
$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
$bitmap = New-Object System.Drawing.Bitmap $Screen.Width, $Screen.Height
$graphic = [System.Drawing.Graphics]::FromImage($bitmap)
$graphic.CopyFromScreen($Screen.Left, $Screen.Top, 0, 0, $bitmap.Size)
$bitmap.Save([Environment]::GetFolderPath("Desktop") + "\Screenshot.bmp")
```

### Sound

Tune the guitar

```powershell
82, 110, 146, 196, 246, 329 | Foreach-Object {[console]::beep($_,4000)} # E,A,D,G,B,E
```

### Speech

Make powershell read out some given text:

```powershell
[Reflection.Assembly]::LoadWithPartialName('System.Speech') | Out-Null
$tts = New-Object System.Speech.Synthesis.SpeechSynthesizer
$tts.Speak("OMG I can speak!")
```

It is possible to add [SSML](https://www.w3.org/TR/speech-synthesis) to set pitch and language:

```powershell
Add-Type -AssemblyName System.speech
$tts = New-Object System.Speech.Synthesis.SpeechSynthesizer

$Phrase = '
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" 
    xml:lang="en-US">
    <voice xml:lang="en-US">
    <prosody rate="1">
        <p>Normal pitch. </p>
        <p><prosody pitch="x-high"> High Pitch. </prosody></p>
    </prosody>
    </voice>
</speak>
'
$tts.SpeakSsml($Phrase)
```

### Email and Calendar

Sind Mail with depreacted Send-MailMessage command

```powershell
$From = "You@gmail.com"
$To = "sombody@somewhere.com"
$Attachment = "D:\test.txt"
$Subject = "Subject"
$Body = "Hi"
$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"
Send-MailMessage -From $From -to $To -Subject $Subject -Body $Body -SmtpServer $SMTPServer -port $SMTPPort -UseSsl -Credential (Get-Credential) -Attachments $Attachment
```

Get a list of meetings occurring today

```powershell
$ns = New-Object -ComObject Outlook.Application.GetNamespace('MAPI')
$Start = (Get-Date).ToShortDateString()
$End = (Get-Date).ToShortDateString()
$appointments = $ns.GetDefaultFolder(9).Items
$appointments.IncludeRecurrences = $true
$appointments.Restrict("[MessageClass]='IPM.Appointment' AND [Start] > '$Start' AND [End] < '$End'") |  
ForEach-Object {
    if (-Not $_.IsRecurring ) { $_;  } else {
        try { $_.GetRecurrencePattern().GetOccurrence((Get-Date).ToString("yyyy-MM-dd") + " " + $_.Start.ToString("HH:mm")) } 
        catch {  }
		}
	} | Sort-Object -property Start | ForEach-Object { 
    $arrr = ($_.RequiredAttendees.split(';') | ForEach-Object { $_.Trim() } | ForEach-Object { $_.split(' ')[1] + ' ' + $_.split(' ')[0] } )
    $attendees = ($arrr -join " ").Replace(", ",",").TrimEnd(',')
    "`n`t`t[ ] $($_.Start.ToString("HH:mm")) - $($_.Subject.ToUpper()) with: $attendees"
}
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
