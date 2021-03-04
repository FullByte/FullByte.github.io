# Powershell

## One-Liner to check for open ports of an application

You can check the open ports running via netstat.
To get a specific port pipe a find or select-string command with the process Id you are looking for:

```powershell
netstat -ano | Select-String "6048"
```

Some processes have many process ids. Example:

```powershell
Get-Process "svchost" | select -expand id
```

We would need to loop through all processes ids to be sure to see all communications currently open for this application.
Please note "svchost" is just an example application that should work for testing on your pc... choose whatever you like.

To avoid manually looping though all PIDs and having a oneliner with a readable output here is a powershell script that does just that.
Replace the "svchost" with the process name you are looking for.

```powershell
get-nettcpconnection | select local*,remote*,state,@{Name="Process";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | Where-Object {$_.Process -eq "svchost"} | Format-Table
```

## Basics

Check for Windows Updates Powershell Command:

```powershell
(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()
```

Export PowerShell command history to a file:

```powershell
Get-History | Export-CSV $env:USERPROFILE\Desktop\CommandHistory.CSV
```

Export all available powershell commands:

```powershell
Get-Command  | Export-CSV $env:USERPROFILE\Desktop\CommandsAvailable.CSV
```

## Servers

Access Server

```powershell
powershell.exe -nolog --command cmdkey /generic:TERMSRC/some_unc_path /user:username /pass:pa$$word; mstsc /v:some_unc_path
```

## Query System

Get Last 10 installations

```powershell
get-wmiobject Win32_ReliabilityRecords -computername 127.0.0.1 | select-object -first 10 Message | format-list *
```

## Verbose Mode

Option 1)

With a value of 1 you get each line of code as it executes, e.g.:

```powershell
Set-PSDebug -Trace 1
Get-PSDepth
```

With a value of 2 you also get variable assignments and code paths:

```powershell
Set-PSDebug -Trace 2
Get-PSDepth
```

Option 2)

You can always use the below in your script.

```powershell
$VerbosePreference="Continue"
```

Option 3)

```powershell
Some commands have an -verbose or -v parameter
```

## Privileges

**Check Admin Rights**

```powershell
#Requires -RunAsAdministrator
[bool]([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
[bool](([System.Security.Principal.WindowsIdentity]::GetCurrent()).groups -match "S-1-5-32-544")
```

## Find Commands

**Find commands valid in powershell for a specific typ/function e.g. “Service”**

```powershell
Get-Command –noun Service
```

**Sometimes the searched name is part of the noun e.g. typ/function “AD” will have no results when entering get-command –noun AD. But with the following command you get all AD related commands:**

```powershell
Get-Command -noun ad*
```

## IIS

```powershell
Set-ItemProperty 'IIS:\\Sites\\$Site' ApplicationPool $AppPoolName  
Set-ItemProperty IIS:\\Sites\\$Site -Name bindings -Value (@{protocol="https";bindingInformation="\*:$Port:$Site"})

Start-WebSite -Name $site
Stop-WebSite -Name $site

Clear-ItemProperty IIS:\\Sites\\$Site -Name bindings
```

Get Binding Info

```powershell
[string]$BindingInfo = $Binding.Collection
[string]$IP = $BindingInfo.SubString($BindingInfo.IndexOf(" "),$BindingInfo.IndexOf(":")-$BindingInfo.IndexOf(" "))			
[string]$Port = $BindingInfo.SubString($BindingInfo.IndexOf(":")+1,$BindingInfo.LastIndexOf(":")-$BindingInfo.IndexOf(":")-1)
```

## To Sort

### Debugging

```powershell
Start Debugging
Set-PSDebug -step

Stop Debugging
Set-PSDebug -stop
```

### Get Hostname

```powershell
get-content env:computername
```

### Set current Path

```powershell
[Environment]::CurrentDirectory=(Get-Location -PSProvider FileSystem).ProviderPath
$test=[Environment]::CurrentDirectory
$test
```

### Add all availbale snapins (good to check if somethings missing)

```powershell
get-pssnapin -registered | add-pssnapin -passthru
```

### Running services

````powershell
    Get-service | where-object {$_.status -eq "Running}
     ```

    ### review the IP addresses assigned to the server
    ```powershell
    Get-NetIPAddress | Format-table
````

Last 10 security log entries

```powershell
Get-EventLog Security -Newest 10
```

MyDocuments folder of current user:
[System.Environment]&#x3A;:GetFolderPath([System.Environment+SpecialFolder]&#x3A;:MyDocuments)

Get all help examples
Get-Command -CommandType cmdlet | % { (get-help $\_.name).examples }
\############################

## Server Information

Get Last Server Boot Time:

```powershell
([wmi]"").ConvertToDateTime((Get-WmiObject -Class Win32_OperatingSystem).LastBootuptime)
```

Search recursively for a certain string within files

```powershell
dir –r | select string "searchforthis"
```

five processes using the most memory

```powershell
ps | sort –property ws | select –last 5
```

Get Computer and BIOS information

```powershell
Get-WmiObject -Class Win32_BIOS
Get-WmiObject -Class Win32_ComputerSystem
```

All currently assigned IP addresses

```powershell
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Format-Table -Property IPAddress
```

All details on current IP addresses:

```powershell
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Select-Object -Property [a-z]_ -ExcludeProperty IPX_,WINS\*
```

Installed applications on the current computer

```powershell
Get-WmiObject -Class Win32_Product -ComputerName . | Format-Wide -Column 1
```

## Security

Get all thumbprint of a cert installed

```powershell
(Get-ChildItem -path cert:\\LocalMachine\\My | where { $\_.Subject -match '\*' }).thumbprint
```

## Storage

Add WebDAV to local path

```powershell
(Invoke-WebRequest https://webdav.domain.com/ -Method Options).Headers.DAV  
[String]$WebDAVShare = '\\webdav.domain.com@SSL/path/to/files'
New-PSDrive -Name S -PSProvider FileSystem -Root $WebDAVShare -Credential 'user@domain.tdl'
```

## Network

Test connection on specific port

```powershell
TNC <server> -Port 5986
```

Set network location to Private for all networks:

```powershell
$networkListManager = [Activator]&#x3A;:CreateInstance([Type]&#x3A;:GetTypeFromCLSID([Guid]"{DCB00C01-570F-4A9B-8D69-199FDBA5723B}")) 
$connections = $networkListManager.GetNetworkConnections() 
$connections | % {$\_.GetNetwork().SetCategory(1)}
```

Configure Ip address, DNS server for network cards:

```powershell
Set-DnsClientServerAddress –InterfaceAlias Ethernet\* -ServerAddresses “x.x.x.x”,”x.x.x.x”
```

Create NIC Teaming

```powershell
New-NetLBfoTeam –Name Guest –TeamMembers Guest-A,Guest-B -TeamingMode SwitchIndependent
```

## Files

Find something in (large) files

```powershell
Get-Content myTestLog.log -wait | where { $\_ -match “WARNING” }
```

Read Registry Key

```powershell
Get-ItemProperty -Path Registry::"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Install" | format-list
```

## Remoting

```powershell
Function runCodeOnRemoteNode
{

    # Run VBscript that starts Powershell script on source computer that does the following:
    $session = new-pssession -computername server -Credential dom\user

    # User $global:ScriptLink instead of hardcoded link
    Invoke-Command -session $session -filepath D:\Scripts\do.ps1 -ArgumentList "remote"

}

$Command = "Netsh int ip delete address ""$global:FrontendNICname"" addr=$global:OSSTIP"
    invoke-expression "$Command" #| out-null

```

## Most Used

ConvertTo-HTML

```powershell
Get-Service | ConvertTo-HTML -Property Name, Status > C:\\services.htm
```

Export-CSV

```powershell
Get-Service | Export-CSV c:\\service.csv
```

```powershell
Get-EventLog -Log "Application"
```

Report all of the USB devices installed
```powershell
gwmi Win32_USBControllerDevice -computername SERVER1 |fl Antecedent,Dependent
```

Use PSDrive to view more than just drives
The PSDrive command lets you view objects of the Windows environment beyond traditional network, local, or removable drives. One popular view is the HKLM PSDrive to view the HKEY_LOCAL_MACHINE top-level hive of the registry. To get into the registry, enter the following command:

```powershell
cd HKLM:
HKLM:/>
```

You are then transported into the registry hive and can view and even delete items, should you wish.

Export NTFS folder permissions — recursive or not
Managing NTFS permissions is a whole separate matter, but with PowerShell, you can export the permissions to audit access or take a quick look at access control lists (ACLs) for the security configuration. This can be a great accountability mechanism to run in a scripted format periodically — or you can run it on demand to diagnose a particular issue. For example, take the following iteration:

```powershell
Get-Acl N:Data
Get-ChildItem N:Data -recurse | Get-Acl
```
