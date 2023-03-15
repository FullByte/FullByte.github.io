# GPG

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Using a symmetric cypher (AES 256)

Encrypt with symmetric cypher

``` sh
gpg --symmetric --cipher-algo aes256 -o test.txt.gpg test.txt
```

Decrypt with symmetric cypher

``` sh
gpg -d -o test.txt test.txt.gpg
```

## Email setup

Generate Key

``` sh
gpg --full-generate-key
```

Export Key

``` sh
gpg --list-keys
gpg --output mygpgkey_pub.gpg --armor --export ABCDFE01
gpg --output mygpgkey_sec.gpg --armor --export-secret-key ABCDFE01
```

Alternativly output to console: ``` gpg --armor --export ABCDFE01```

Copy Keys

``` sh
scp mygpgkey_pub.gpg mygpgkey_sec.gpg user@remotehost:~/
```

Import Key

``` sh
gpg --import ~/mygpgkey_pub.gpg
gpg --allow-secret-key-import --import ~/mygpgkey_sec.gpg
rm ~/mygpgkey_sec.gpg ~/mygpgkey_pub.gpg
gpg --list-keys
```

Publish Public Key to Key Server

## Key Server

Public Key Server Services

- <https://keys.mailvelope.com/>
- <https://keyserver.ubuntu.com>
- <http://pgp.mit.edu/>
- <https://keys.openpgp.org/>

``` sh
gpg --keyserver keyserver.ubuntu.com --send-keys 8CC3D3CDE700B7DE
```

Search entry on Key Server

``` sh
gpg --keyserver hkp://keyserver.ubuntu.com --search-key 'fabian@fromm.rocks'
```

Alternativly use the webinterface e.g. <https://keys.mailvelope.com/pks/lookup?op=get&search=email@example.com>
