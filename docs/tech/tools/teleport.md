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
sudo curl https://apt.releases.teleport.dev/gpg \
-o /usr/share/keyrings/teleport-archive-keyring.asc
source /etc/os-release
echo "deb [signed-by=/usr/share/keyrings/teleport-archive-keyring.asc] \
https://apt.releases.teleport.dev/${ID?} ${VERSION_CODENAME?} stable/v12" \
| sudo tee /etc/apt/sources.list.d/teleport.list > /dev/null

sudo apt-get update
sudo apt-get install teleport

teleport configure --acme --acme-email=<user>@<domain> --cluster-name=<FQDN> | \
sudo tee /etc/teleport.yaml > /dev/null
```

## Add a server

To add a device your get a new command each time that looks like this:

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
