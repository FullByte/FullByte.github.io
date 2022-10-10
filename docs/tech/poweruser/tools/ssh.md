# SSH

## Install and Configure

Windows 10

**Install SSH**

View Options: ```Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'```

Install SSH Client and or Server

``` ps1
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

**Configure SSH**

``` ps1
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

**Firewall settings**

There should be a firewall rule named "OpenSSH-Server-In-TCP", which should be enabled

``` ps1
Get-NetFirewallRule -Name *ssh*
```

If the firewall does not exist, create one

``` ps1
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH-Server-In-TCP' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

## Login

Login to azure server "azureserver" with user "user" and private ssh keyfile "private.key". The passphrase will be queried after executing the command.

``` sh
ssh -i private.key user@azureserver.westeurope.cloudapp.azure.com
```

When you SSH into another machine using public key authentication, the key pair from either `~/.ssh/id_dsa`, `~/.ssh/id_ecdsa`, or `~/.ssh/id_rsa` is used by default. The `-i` option can be used to specify a different key pair file.

Use the `-L` flag to forward a connection to a remote server

``` sh
ssh server -L3000:localhost:3000
```

## Configuration

Edit ~/.ssh/config for multiple SSH Hops

``` sh
Host bastion
Hostname bastion.domain.com
User bastion-user

Host server
Hostname server.local.lan
User server-user
ProxyCommand ssh bastion -W %h:%p
```

Edit ~/.ssh/authorized_keys to restrict SSH User Access

``` sh
from="10.20.30.0/24,44.55.66.77",no-agent-forwarding,no-port-forwarding,no-X11-forwarding,command="/usr/local/bin/whatever" ssh-rsa [...]
```

Create Secure SSH Key

``` sh
ssh-keygen -o -a 100 -t ed25519
```

Add Key to Remote Server

``` sh
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remote
```

## Security

When SSH tries to authenticate via public key, it sends the server all your public keys, one by one, until the server accepts one. One can take advantage of this to enumerate all the client's installed public keys.

If this behavior is problematic for you, you can tell SSH not to present your public keys to the server by default.

Add these lines at the end of your ```~/.ssh/config``` (after other "Host" directives)

``` config
Host *
    PubkeyAuthentication no
    IdentitiesOnly yes
```

Then specify what keys should be used for each host

``` config
Host github.com
    PubkeyAuthentication yes
    IdentityFile ~/.ssh/github_id_rsa
```

## SSH Escape Sequences

To see all escape sequences press `~?`.

``` txt
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

## Creating an SSH key

- Generate a key: ```ssh-keygen -t ed25519 -a 100 -q -N "" -f ~/.ssh/id_ed25519```
- Generate a key in the current directory: ```ssh-keygen -t ed25519 -a 100 -q -N "" -f "$PWD"/renameme```
- Generate a key with a given name: ```ssh-keygen -t ed25519 -a 100 -q -N "" -f "$PWD"/deploy_key_1 -C deploy_key_1```

Creating an SSH key for Github

``` sh
# Create
ssh-keygen -t rsa -b 4096 -N "" -C "" -f keyname
mv keyname* ~/.ssh
chmod 700 ~/.ssh && chmod 600 ~/.ssh/*
Host github
HostName github.com
User git
IdentityFile ~/.ssh/keyname

# Copy public key to server.
ssh-copy-id -i ~/.ssh/keyname user@remote_machine

# Checking the ssh procesd
ssh -T git@github.com
eval $(ssh-agent -s)
ssh-add ~/.ssh/keyname
ssh -T git@github.com
```

## Helpful commands

- Change Password: ```ssh-keygen -p -f C:\Users\0xfab1\.ssh\id_ed25519```
- Forward Multiple Ports Over SSH: ```ssh dev@server.com -L 3000:localhost:3000 -L 9009:localhost:9009```
- Test SSH (e.g. to gitlab): ```ssh -vT git@gitlab.com```
- Close stuck SSH session: Press: ```Enter``` then ```~``` then ```.```
- Get SSH key fingerprint: ```ssh-keygen -l -E md5 -f ~/.ssh/my-ssh-key```
