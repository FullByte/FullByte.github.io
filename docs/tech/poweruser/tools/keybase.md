# Keybase

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Push your secret key

Push your secret/privat key file "privkey.asc" to keybase so you can then use it on other linked devices:

``` sh
keybase pgp import -i .\privkey.asc --push-secret
```

or from gpg

``` sh
gpg --armor --export-secret-keys MYSECRETKEYID | keybase pgp import --push-secret
```
