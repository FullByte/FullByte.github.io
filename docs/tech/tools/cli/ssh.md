# SSH

| What    | Where                                                                                      |
|---------|--------------------------------------------------------------------------------------------|
| Docs    | <https://man.openbsd.org/ssh.1>                                                            |
| OpenSSH | <https://www.openssh.com>                                                                  |
| Windows | <https://learn.microsoft.com/de-de/windows-server/administration/openssh/openssh_overview> |

Some SSH Tools:

- <https://github.com/jtesta/ssh-audit>

## Install and Configure

Windows 10

### Install SSH

View Options: ```Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'```

Install SSH Client and or Server

``` ps1
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

### Configure SSH

``` ps1
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

### Firewall settings

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
ssh -i private.key user@server
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

Add Key to remote server

``` sh
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remote
```

## Security

### Server Hardening

Hardening for Ubuntu 22.04 LTS Server.
All commands need to be executed as root.

Re-generate the RSA and ED25519 keys

```sh
rm /etc/ssh/ssh_host_*
ssh-keygen -t rsa -b 4096 -f /etc/ssh/ssh_host_rsa_key -N ""
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N ""
```

Remove small Diffie-Hellman moduli

```sh
awk '$5 >= 3071' /etc/ssh/moduli > /etc/ssh/moduli.safe
mv /etc/ssh/moduli.safe /etc/ssh/moduli
```

Enable the RSA and ED25519 HostKey directives in the /etc/ssh/sshd_config file:

```sh
sed -i 's/^\#HostKey \/etc\/ssh\/ssh_host_\(rsa\|ed25519\)_key$/HostKey \/etc\/ssh\/ssh_host_\1_key/g' /etc/ssh/sshd_config
```

Restrict supported key exchange, cipher, and MAC algorithms

```sh
echo -e "\n# Restrict key exchange, cipher, and MAC algorithms, as per sshaudit.com\n# hardening guide.\nKexAlgorithms sntrup761x25519-sha512@openssh.com,curve25519-sha256,curve25519-sha256@libssh.org,gss-curve25519-sha256-,diffie-hellman-group16-sha512,gss-group16-sha512-,diffie-hellman-group18-sha512,diffie-hellman-group-exchange-sha256\nCiphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr\nMACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,umac-128-etm@openssh.com\nHostKeyAlgorithms ssh-ed25519,ssh-ed25519-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,rsa-sha2-512,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256,rsa-sha2-256-cert-v01@openssh.com" > /etc/ssh/sshd_config.d/ssh-audit_hardening.conf
```

Restart OpenSSH server

```sh
service ssh restart
```

### Client Config

When SSH tries to authenticate via public key, it sends the server all your public keys, one by one, until the server accepts one. One can take advantage of this to enumerate all the client's installed public keys.

If this behavior is problematic for you, you can tell SSH not to present your public keys to the server by default.

Add these lines at the end of your ```~/.ssh/config``` (after other "Host" directives)

```txt
Host *
    PubkeyAuthentication no
    IdentitiesOnly yes
```

Then specify what keys should be used for each host

```txt
Host github.com
    PubkeyAuthentication yes
    IdentityFile ~/.ssh/github_id_rsa
```

Some additional config settings from [mozilla](https://infosec.mozilla.org/guidelines/openssh):

```txt
# Ensure KnownHosts are unreadable if leaked - it is otherwise easier to know which hosts your keys have access to.
HashKnownHosts yes
# Host keys the client accepts - order here is honored by OpenSSH
HostKeyAlgorithms ssh-ed25519-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,ssh-ed25519,ssh-rsa,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256
KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
```

The algorithms supported by a particular OpenSSH version can be listed with the following commands:

```sh
ssh -Q cipher
ssh -Q cipher-auth
ssh -Q mac
ssh -Q kex
ssh -Q key
```

### Server Config

Some additional config settings from [mozilla](https://infosec.mozilla.org/guidelines/openssh):

```txt
# Supported HostKey algorithms by order of preference.
HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key

KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256

Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr

MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com

# Password based logins are disabled - only public key based logins are allowed.
AuthenticationMethods publickey

# LogLevel VERBOSE logs user's key fingerprint on login. Needed to have a clear audit track of which key was using to log in.
LogLevel VERBOSE

# Log sftp level file access (read/write/etc.) that would not be easily logged otherwise.
Subsystem sftp  /usr/lib/ssh/sftp-server -f AUTHPRIV -l INFO

# Root login is not allowed for auditing reasons. This is because it's difficult to track which process belongs to which root user:
#
# On Linux, user sessions are tracking using a kernel-side session id, however, this session id is not recorded by OpenSSH.
# Additionally, only tools such as systemd and auditd record the process session id.
# On other OSes, the user session id is not necessarily recorded at all kernel-side.
# Using regular users in combination with /bin/su or /usr/bin/sudo ensure a clear audit track.
PermitRootLogin No
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

### Creating an SSH key for Github

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

Get the public key of a github user:

```sh
curl -s https://github.com/fullbyte.keys > fullbyte-github.key
ssh-keygen -l -f fullbyte-github.key
256 SHA256:GsiF6Lligv7mFffk8WYLjhIpa4kgjxnfjHD4HXfgmi0 no comment (ED25519)
```

## Helpful commands

Add `-v`, `-vv` or `-vvv` for more output details.

- Change Password: ```ssh-keygen -p -f C:\Users\0xfab1\.ssh\id_ed25519```
- Forward Multiple Ports Over SSH: ```ssh dev@server.com -L 3000:localhost:3000 -L 9009:localhost:9009```
- Test SSH (e.g. to gitlab): ```ssh -vT git@gitlab.com```
- Close stuck SSH session: Press: ```Enter``` then ```~``` then ```.```
- Get SSH key fingerprint: ```ssh-keygen -l -E md5 -f ~/.ssh/my-ssh-key```
- Get Fingerprint of server: ```ssh-keyscan -H sshtest.0xfab1.net```
- Generate SSHFP DNS entries: ```ssh-keygen -g -r sshtest.0xfab1.net```
- Get SSHFP entries: ```ssh-keyscan -D sshtest.0xfab1.net```
- Get specific SSHFP entries: ```ssh-keyscan -t ecdsa,ed25519 -f sshtest.0xfab1.net```
- Read SSHFP DNS entries: ```dig @localhost sshtest.0xfab1.net sshfp +noall +answer +dnssec```
- Login and check SSHFP (requires DNSSEC): ```ssh -i sshtest_key.pem -o VerifyHostKeyDNS=yes fabian@sshtest.0xfab1.net```

## Restart SSHD

Different options to restart the SSH daemon for various OS:

| OS         | native/old                         | using service            | using systemd                       |
|------------|------------------------------------|--------------------------|-------------------------------------|
| CentOS     |                                    | service sshd restart     | sudo systemctl restart sshd         |
| RHEL       |                                    | service sshd restart     | sudo systemctl restart sshd         |
| Fedora     |                                    | service sshd restart     | sudo systemctl restart sshd         |
| Redhat     | /etc/init.d/sshd restart           | service sshd restart     | sudo systemctl restart sshd         |
| Alma       |                                    | service sshd restart     | sudo systemctl restart sshd         |
| Rocky      |                                    | service sshd restart     | sudo systemctl restart sshd         |
| Debian     | /etc/init.d/ssh restart            | sudo service ssh restart | sudo systemctl restart ssh          |
| Ubuntu     | /etc/init.d/ssh restart            | sudo service ssh restart | sudo systemctl restart ssh          |
| Mint       | /etc/init.d/ssh restart            | sudo service ssh restart |                                     |
| FreeBSD    | doas /etc/rc.d/sshd restart        |                          |                                     |
| UNIX       | kill -HUP $(cat /var/run/sshd.pid) |                          |                                     |
| OpenSUSE   |                                    |                          | sudo systemctl restart sshd         |
| SUSE       |                                    |                          | sudo systemctl restart sshd         |
| Arch Linux |                                    |                          | sudo systemctl restart sshd.service |
