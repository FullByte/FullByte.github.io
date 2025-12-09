# Teleport

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |

## Install on Ubuntu

### Docker

``` sh
TELEPORT_DOCKER_IMAGE=public.ecr.aws/gravitational/teleport:12
mkdir -p ~/teleport/config ~/teleport/data
docker run --hostname localhost --rm \
  --entrypoint=/bin/sh \
  -v ~/teleport/config:/etc/teleport \
  ${TELEPORT_DOCKER_IMAGE} -c "teleport configure > /etc/teleport/teleport.yaml"
docker run --hostname localhost --name teleport \
  -v ~/teleport/config:/etc/teleport \
  -v ~/teleport/data:/var/lib/teleport \
  -p 3023:3023 -p 3025:3025 -p 3080:3080 \
  ${TELEPORT_DOCKER_IMAGE}
docker exec teleport tctl users add testuser --roles=editor,access --logins=root,ubuntu,ec2-user
```

### Local

``` sh
sudo apt update  
sudo apt install -y curl wget apt-transport-https gnupg2  

curl https://cdn.teleport.dev/install.sh | bash -s 18.5.0

sudo teleport configure -o file --acme --acme-email=mail@me.ok --cluster-name=ssh.domain.lol

sudo systemctl enable teleport
sudo systemctl start teleport
```

## Add a server

To add a device run this command:

``` sh
sudo bash -c "$(curl -fsSL https://<teleport-url>/scripts/<random-number>/install-node.sh)"
```

- View Teleport status ```sudo systemctl status teleport.service```
- View Teleport logs ```sudo journalctl -u teleport.service```
- Stop Teleport ```sudo systemctl stop teleport.service```
- Start Teleport ```sudo systemctl start teleport.service```

You can see this node connected in the Teleport web UI or 'tsh ls' with the name 'test'
Find more details on how to use Teleport here: <https://goteleport.com/docs/user-manual/>

## Add a Teleport user

``` sh
sudo tctl users add tele-admin --roles=editor,access --logins=fab1
```

## Remove all files

This may help when trying to de-install or re-install Teleport:

``` sh
pkill -f teleport
rm -rf /var/lib/teleport
rm -f /etc/teleport.yaml
rm -f /usr/local/bin/teleport /usr/local/bin/tctl /usr/local/bin/tsh
rm -rf /usr/local/bin/tctl
```

## Update Teleport

Run this to upgrade to the latest version:

``` sh
sudo apt-get update && sudo apt-get install teleport
```
