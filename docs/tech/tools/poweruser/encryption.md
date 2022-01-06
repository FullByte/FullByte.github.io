# Encryption

## GPG

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

### Using a symmetric cypher (AES 256)

Encrypt with symmetric cypher

``` sh
gpg --symmetric --cipher-algo aes256 -o test.txt.gpg test.txt
```

Decrypt with symmetric cypher

``` sh
gpg -d -o test.txt test.txt.gpg
```
