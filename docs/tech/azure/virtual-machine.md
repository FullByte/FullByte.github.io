# Azure VM

## Custom Script Extension for Windows

You can only have one [Custom Script Extension](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-windows) attached to a VM at a time.

Local place the script is stored:

- Script: C:\Packages\Plugins\Microsoft.Compute.CustomScriptExtension\_%version%_\Downloads
- Actionlog: C:\WindowsAzure\Logs\Plugins\Microsoft.Compute.CustomScriptExtension\_%version%

You can overwrite the existing script and it will run :D

Example CSE for Windows to install IIS

```ps1
# this custom script extension installs IIS and downloads urlrewrite and install
$tmpDir = "c:\temp\" # this will be our temp folder for download / logging
if (!(Test-Path $tmpDir)) { mkdir $tmpDir -force } # create folder if it doesn't exist
Start-Transcript "$tmpDir\Install-IIS.log"

# install IIS features 
$features = @("Web-Server", "Web-WebServer", "Web-Common-Http", "Web-Default-Doc", "Web-Dir-Browsing", "Web-Http-Errors", "Web-Static-Content", "Web-Http-Redirect", "Web-Health", "Web-Http-Logging", "Web-Custom-Logging", "Web-Log-Libraries", "Web-Request-Monitor",  "Web-Http-Tracing", "Web-Performance", "Web-Stat-Compression", "Web-Dyn-Compression", "Web-Security", "Web-Filtering", "Web-Basic-Auth", "Web-IP-Security", "Web-Url-Auth", "Web-Windows-Auth", "Web-App-Dev", "Web-Net-Ext45", "Web-Asp-Net45", "Web-ISAPI-Ext", "Web-ISAPI-Filter", "Web-Mgmt-Tools", "Web-Mgmt-Console", "Web-Scripting-Tools", "NET-Framework-45-Features", "NET-Framework-45-Core", "NET-Framework-45-ASPNET", "NET-WCF-Services45", "NET-WCF-TCP-PortSharing45")
Install-WindowsFeature -Name $features -Verbose 

# download and install URL Rewrite Module for IIS
$URLRewrite2_1 = "http://download.microsoft.com/download/D/D/E/DDE57C26-C62C-4C59-A1BB-31D58B36ADA2/rewrite_amd64_en-US.msi"
$URLRewrite2_1Path = $tmpDir + "\$(Split-Path $URLRewrite2_1 -Leaf)"
if (!(Test-Path $URLRewrite2_1Path )) { start-bitstransfer "$URLRewrite2_1" "$URLRewrite2_1Path" -Priority High -RetryInterval 60 -Verbose -TransferType Download }
start-process -filepath msiexec -ArgumentList "/i ""$URLRewrite2_1Path"" /l*v ""$URLRewrite2_1Path.log""  /passive ACCEPTEULA=""YES""" -Wait #unattended install

Stop-Transcript
```
