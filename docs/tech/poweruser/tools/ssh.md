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

When you SSH into another machine using public key authentication, the key pair from either `~/.ssh/id_dsa`, `~/.ssh/id_ecdsa`, or `~/.ssh/id_rsa` is used by default. The `-i` option can be used to specify a different key pair file.

Use the `-L` flag to forward a connection to a remote server

```
ssh server -L3000:localhost:3000
```

## SSH Escape Sequences

To see all escape sequences press `~?`.

```
 ~.   - terminate connection (and any multiplexed sessions)
 ~B   - send a BREAK to the remote system
 ~C   - open a command line
 ~R   - request rekey
 ~V/v - decrease/increase verbosity (LogLevel)
 ~^Z  - suspend ssh
 ~#   - list forwarded connections
 ~&   - background ssh (when waiting for connections to terminate)
 ~?   - this message
 ~~   - send the escape character by typing it twice
(Note that escapes are only recognized immediately after newline.)
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

## Helpful commands

Examples:

- Forward Multiple Ports Over SSH: ```ssh dev@server.com -L 3000:localhost:3000 -L 9009:localhost:9009```