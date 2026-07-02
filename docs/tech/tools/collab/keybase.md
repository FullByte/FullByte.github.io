---
date: 2023-12-22
modified: 2023-12-22
description: 'Push your secret/privat key file "privkey.asc" to keybase so you can then use it on other linked devices:'
tags:
- Tech
- Tools
---

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
