# Code

## VScode

| What          | Where                                  |
|---------------|----------------------------------------|
| Official Page | <https://code.visualstudio.com/>       |
| Source        | <https://github.com/Microsoft/vscode>  |
| Download      | <https://aka.ms/win32-x64-user-stable> |
| Install       | choco install vscode                   |

### Shortcuts

- Menu: F1 or CTRL+SHift+P
- Insert cursor to select vertically: CTRL+ALT+up/down

### Extensions

Draw

- [tldraw](https://marketplace.visualstudio.com/items?itemName=tldraw-org.tldraw-vscode)
- [drawio](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)

### User Github or Microsoft Account to Sync settings

If you want to restore your settings or use VSCode on multiple machines consider syncing the VSCode settings such as extensions, settings, snippets, keyboard shortcuts and UI states.

## Git

## Tools

- Github quick stats: <https://github.com/arzzen/git-quick-stats>

### Setup

Set global user name and email:
(remove --global flag for specific repo only)

``` sh
git config --global user.name "0xfab1"
git config --global user.email "f@bi.an"
```

Setup SSH login

Create new key

``` sh
ssh-keygen -t ed25519
Check if service is running and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

Copy this to github: <https://github.com/settings/ssh/new>

``` sh
cat ~/.ssh/id_ed25519.pub
```

Test connection to github

``` sh
ssh -T git@github.com
```

Test to clone, commit and push on a repo

``` sh
git clone git@github.com:FullByte/git-test.git
cd git-test/
nano script.sh
chmod u+x script.sh
git add script.sh -f
git commit -m "adding script"
git push
```

### Commands

Get all authors:

``` sh
git log | Where { $_ -match "Author" } | Select-Object -unique
```

### Pretend to be busy

Do this on a clean machine

``` sh
git config --global user.email "busybee@fab1.internet"
git config --global user.name "Busy Bee"
```

Clone an empty new repostory e.g.:

``` sh
git clone https://github.com/FullByte/git-test
cd git-test
```

Run the script to create a commit for every day... e.g. since 1999.

``` sh
nano script.sh
chmod u+x script.sh
./script.sh
```

??? details "script.sh"
   ``` sh
    for Y in {2018..2020}
    do
    mkdir $Y
    cd $Y
    for M in {01..12}
    do
        mkdir $M
        cd $M
        for D in {01..28}
        do
            mkdir $D
            cd $D
            for i in {01..12}
            do
                echo "$i on $M/$D/$Y" > commit.md
                export GIT_COMMITTER_DATE="$Y-$M-$D 12:$i:00"
                export GIT_AUTHOR_DATE="$Y-$M-$D 12:$i:00"
                git add commit.md -f
                git commit --date="$Y-$M-$D 12:0$i:00" -m "$i on $M $D $Y"
            done
            cd ../
        done
        cd ../
    done
    cd ../
    done
    git push
    #optional: delete stuff
    #git rm -rf 20**
    #git rm -rf 19**
    #git commit -am "cleanup"
    #git push
   ```

## Github

Info

|What|Where|
|-|-|
|Official Page|<https://github.com>|
|Service Status|<https://www.githubstatus.com/>|
|Docs|<https://docs.github.com>|
|Download|<https://desktop.github.com/>|
|Install|choco install github-desktop|

### RSS Feed for Commits

Add ".atom" to a given commit link to get an RSS Reader update on a given file/folder or the entire project.

For example:

- Link: <https://github.com/FullByte/FullByte.github.io/commits/master>
- RSS Feed: <https://github.com/FullByte/FullByte.github.io/commits/master.atom>

Add the atom link to your rss feed reader to get notified on updates.

### VScode online

Press "." in any github repo to open the editor.

Add "1s" to "github" to get the VScode GUI of the github repo you selected

Example:

- Standard: <https://github.com/FullByte/FullByte.github.io/>
- VScode: <https://github1s.com/FullByte/FullByte.github.io/>

### Helper

- Smee receives payloads then sends them to your locally running application: <https://smee.io/>
- Probot automates and improves your github workflows with pre-built apps: <https://probot.github.io/>
- Search for code: <https://gowalker.org/>

### Execute Gist/Github Script

You can run remote scripts from e.g. Github (either gists or raw content):

From powershell with github raw file:

**Windows**

``` ps11
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/FullByte/project/master/file.file'))
```

From cmd with gist link:

```cmd
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/FullByte/000000000000000000000000000000000000/raw'))"
```

**Linux**

From bash

``` sh
bash <(curl -Ls https://raw.githubusercontent.com/FullByte/scripts/master/something)
```

### Github Pages

To honor [this post](https://rakhim.org/images/honestly-undefined/blogging.jpg) (and ensure the message remains true) I will use my own website as an example and show how I configured the static web app and make it to work the way it does.

I am using [Github Pages](https://pages.github.com/) to host the content, [Mkdocs](https://www.mkdocs.org/) to create the website from markdown files as input and have own [domain](https://0xfab1.net/) for a nicer URL.

#### Github Pages Repo

I created a repo named `FullByte.github.io` (Replace "FullByte" with your github username). Enable github pages for this repo in settings page of the repo. You will by default have a page available at [FullByte.github.io](https://FullByte.github.io).

#### Custom Domain

Here is a overview of the Github Pages settings I use:

![Github Pages](_github-pages.png)

[Mkdocs](https://www.mkdocs.org/) specifically uses the branch "gh-pages" by default to build the static website that will be served.

I added a [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) "0xfab1.net" and added a file in the main folder of my repo called [CNAME](https://github.com/FullByte/FullByte.github.io/blob/master/CNAME) with one line containing my domain "0xfab1.net".

I added the following IPv4 DNS records (`dig 0xfab1.net +noall +answer -t A`):

```dns
0xfab1.net.             0       IN      A       185.199.108.153
0xfab1.net.             0       IN      A       185.199.109.153
0xfab1.net.             0       IN      A       185.199.110.153
0xfab1.net.             0       IN      A       185.199.111.153
```

as well as these IPv6 DNS records (`dig 0xfab1.net +noall +answer -t AAAA`):

```dns
0xfab1.net.             0       IN      AAAA    2606:50c0:8000::153
0xfab1.net.             0       IN      AAAA    2606:50c0:8001::153
0xfab1.net.             0       IN      AAAA    2606:50c0:8002::153
0xfab1.net.             0       IN      AAAA    2606:50c0:8003::153
```

and a CNAME record for www.0xfab1.net (`dig www.0xfab1.net +noall +answer -t CNAME`):

```dns
www.0xfab1.net.         0       IN      CNAME   fullbyte.github.io.
```

#### Github Actions

Every time I commit to main I want the page to re-build so that the page is up-to-date. I currently don't use branches but this could be a good method to commit changes that should not yet be published. Once ready to publish, create a pull request of your branch and merge it to main.

My [github action to build the static webpage using mkdocs](https://github.com/FullByte/FullByte.github.io/blob/master/.github/workflows/main.yml) looks as follows and is based on [this documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/):

``` yaml
name: mkdocs gh-deploy

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build:
    name: Build and Deploy Documentation
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Master
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs-material
      - name: Deploy
        run: |
          git pull
          mkdocs gh-deploy
```

Additionally, I am running a [security scan](https://slscan.io/en/latest/integrations/code-scan) on every push and check the URLs I share regularly via cron job triggered github action.

There are many other nice things that could be done here. The main important part is to trigger the markdown to static website generator as github action on new commits so that the site is automatically built whenever you commit new content.

## OpenSSL

Examples using OpenSSL

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

### Create certificates and keys

Generate a new private key and Certificate Signing Request

``` sh
openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key
```

Generate a self-signed certificate (see How to Create and Install an Apache Self Signed Certificate for more info)

``` sh
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt
```

Generate a certificate signing request (CSR) for an existing private key

``` sh
openssl req -out CSR.csr -key privateKey.key -new
```

Generate a certificate signing request based on an existing certificate

``` sh
openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key
```

Remove a passphrase from a private key

``` sh
openssl rsa -in privateKey.pem -out newPrivateKey.pem
```

### Validate Certificates and Keys

Check an MD5 hash of the public key to ensure that it matches with what is in a CSR or private key

``` sh
openssl x509 -noout -modulus -in certificate.crt | openssl md5
openssl rsa -noout -modulus -in privateKey.key | openssl md5
openssl req -noout -modulus -in CSR.csr | openssl md5
```

Check an SSL connection: This displays all (including Intermediates) certificates of a given website.

``` sh
openssl s_client -connect www.google.com:443
```

Check Certificate

``` sh
openssl x509 -in certificate.crt -text -noout
```

Check CSR of Certificate

Decode your Certificate Signing Request (CSR) and and verify that it contains the correct information:

``` sh
openssl req -in mycsr.csr -noout -text
```

Check a private key

``` sh
openssl rsa -in private.key -check
```

Check a PKCS#12 file (.pfx or .p12)

``` sh
openssl pkcs12 -info -in keyStore.p12
```

### Converting Using OpenSSL

Convert certificates and keys to different formats to make them compatible with OS/software required.

Convert a DER file (.crt .cer .der) to PEM

``` sh
openssl x509 -inform der -in certificate.cer -out certificate.pem
```

Convert a PEM file to DER

``` sh
openssl x509 -outform der -in certificate.pem -out certificate.der
```

Convert a PKCS#12 file (.pfx .p12) containing a private key and certificates to PEM

You can add -nocerts to only output the private key or add -nokeys to only output the certificates.

``` sh
openssl pkcs12 -in keyStore.pfx -out keyStore.pem -nodes
```

Convert a PEM certificate file and a private key to PKCS#12 (.pfx .p12)

``` sh
openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt
```

### How to encrypt and decrypt files with OpenSSL

Install openssl and the associated development libraries'

Run **openssl version -a** to check if openssl is installed or just run this command to install all requirements for this demo:

``` sh
sudo apt install libssl-dev openssl
```

Create a test file named **"plain.txt"** which we shall encrypt & decrypt in the next step.

``` sh
echo "this is a test" > plain.txt
```

Encrypt and Decrypt example via Triple Data Encryption Standard

The following lines will create the encrypted file **"encrypted.txt"** and decrypted file **"decrypted.txt"**.

``` sh
openssl des3 -in plain.txt -out encrypted.txt -pass pass:password
openssl des3 -d -in encrypted.txt -out decrypted.txt -pass pass:password
```

The file **"decrypted.txt"** should match with our test file **"plain.txt"**.

``` sh
diff -s plain.txt decrypted.txt
```

Encrypt and Decrypt example via AES-256 with CBC

There are plenty of ciphers availble. Run **openssl help** to see the cipher commands available too you. Here is another example using AES-256 with CBC.

``` sh
openssl aes-256-cbc -a -salt -in plain.txt -out encrypted.txt -k password
openssl aes-256-cbc -d -a -in encrypted.txt -out decrypted.txt -k password
```

Encrypt images using a key and IV

``` sh
openssl aes-128-cbc -K "55555555555555555555555555555555" -iv "83deccd3f93b37c70d37297f319cf367" -in WRxFKdq.png -out OMG_SAME_IMAGE.png
```

Example screenshot:

![OpenSSL fle encyption and decryption demo](_openssl_file_encrpytion_decryption.png)

### HTTPS webserver

``` sh
openssl req -x509 -newkey rsa:4096 -keyout /tmp/key.pem -out /tmp/cert.pem -nodes && openssl s_server -WWW -port 8443 -cert /tmp/cert.pem -key /tmp/key.pem
```

``` sh
openssl req -newkey rsa:2048 -nodes -x509 -subj '/CN=name-you-want.example.com' -days 3650 -out server.cert -keyout server.key
```

``` sh
openssl s_server -accept 7781 -cert server.cert -key server.key -WWW
```

### Extract a certificate and private key from PFX file

``` sh
CertName='cert.pfx'
openssl pkcs12 -in $PfxCert -nocerts -out key.pem -nodes #Export the private key
openssl pkcs12 -in $PfxCert -nokeys -out $CertName.pem #Export the certificate
openssl rsa -in key.pem -out $CertName.key #Remove the passphrase from the private key
```

### Create a random password

``` sh
openssl rand -base64 32
```
