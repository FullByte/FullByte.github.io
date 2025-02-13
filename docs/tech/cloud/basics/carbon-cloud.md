# Cloud Carbon Footprint

## Prepare Azure

Create an App registration, add a new client secret and save the following information:

- Application (client) ID => AZURE_CLIENT_ID
- Directory (tenant) ID => AZURE_TENANT_ID
- client secret value (not Secret ID) => AZURE_CLIENT_SECRET

Give this app registration rights in the subscriptions you want to track and add the following roles:

- Reader
- Billing Reader
- Carbon Optimization Reader

Install a VM in Azure and SSH to the machine e.g. using a private key:

``` sh
chmod 400 ~/.ssh/ccfkey.pem
ssh -i ~/.ssh/ccfkey.pem carbonuser@1.1.1.1
```

## Install dependencies

``` sh
sudo apt install iptables-persistent nodejs
nvm install --lts
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")" 
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install --lts
corepack enable yarn
```

Check installed versions

``` sh
nvm --version
yarn --version
node --version
npm --version
```

## Install CCF

### Download

Download and unzip the latest release

``` sh
wget https://github.com/cloud-carbon-footprint/cloud-carbon-footprint/archive/refs/tags/latest.tar.gz
tar -xzvf latest.tar.gz
cd cloud-carbon-footprint-latest
```

### Config .env

Go to cloud-carbon-footprint folder and update the .env file

``` sh
sudo nano ~/cloud-carbon-footprint-latest/packages/api/.env
```

with the following content (e.g. for azure)

``` txt
# Azure
AZURE_USE_BILLING_DATA=true
AZURE_INCLUDE_ESTIMATES=true
AZURE_CLIENT_ID=<add here>
AZURE_CLIENT_SECRET=<add here>
AZURE_TENANT_ID=<add here>
AZURE_AUTH_MODE=default
AZURE_CONSUMPTION_CHUNKS_DAYS=0
AZURE_SUBSCRIPTION_CHUNKS=0
```

do the same for:

``` sh
sudo nano ~/cloud-carbon-footprint-latest/packages/cli/.env
```

Use the `.env.template` as orientation for required variables.

### Install and run

Install and run cloud carbon footprint

``` sh
cd ~/cloud-carbon-footprint-latest
yarn install
```

You need to terminals.

Run this in the first terminal:

``` sh
cd ~/cloud-carbon-footprint-latest
npm run start-api
```

and this in the second terminal:

``` sh
cd ~/cloud-carbon-footprint-latest
yarn start
```

The application should now run and be available on Port 3000. Open the URL (e.g. localhost:3000 or your-ip:3000) and check both terminals to see if there are any errors. The first run should take a while and required some refreshes on the web interface for me to start triggering the API to call and deliver data.

## Optimize

### Redirect to Port 80

Redirect port 3000 to standard http port 80.

``` sh
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 3000
sudo netfilter-persistent save
```

### Configure nginx

TODO

### Enable HTTPS

TODO

``` sh
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx
sudo certbot renew --dry-run
```

### Autostart

TODO

To automatically start cloud-carbon-footprint do the following:

``` sh
sudo nano /etc/systemd/system/cloud-carbon-footprint-api.service
```

And add this content

``` sh
#!/bin/bash
# Load nvm so that the proper Node version is available
export NVM_DIR="/home/youruser/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
cd cloud-carbon-footprint-latest
npm run start-api
```
