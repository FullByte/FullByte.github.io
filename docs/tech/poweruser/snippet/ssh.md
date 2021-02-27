# SSH

## Install and Configure

Windows 10

**Install SSH**

View Options

```powershell
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
```

Install SSH Client and or Server

```powershell
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

**Configure SSH**

```powershell
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

**Firewall settings**

There should be a firewall rule named "OpenSSH-Server-In-TCP", which should be enabled

```powershell
Get-NetFirewallRule -Name *ssh*
```

If the firewall does not exist, create one

```powershell
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH-Server-In-TCP' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

## Login

Login to azure server "azureserver" with user "user" and private ssh keyfile "private.key". The passphrase will be queried after executing the command.

```shell
ssh -i private.key user@azureserver.westeurope.cloudapp.azure.com
```

## File Transfert with SCP

Copying file to host:

```shell
scp SourceFile user@host:~/TargetFile
```

Copying file from host and copying folder from host (with -r switch):

```shell
scp user@host:~/remotefolder .
scp -r user@host:~/remotefolder TargetFolder
```

Note that if the remote host uses a port other than the default of 22, it can be specified in the command. For example, copying a file from host:

```shell
scp -P 666 user@host:directory/SourceFile TargetFile
```
