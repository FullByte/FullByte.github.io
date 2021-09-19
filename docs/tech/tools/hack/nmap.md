# Nmap

Press "v" if you forgot du add "-v" in the scan and need to increase verbosity.

## Simple IP scan

```sh
nmap -sC -sV <ip>
```

## Enumerate the SMB shares

```sh
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>
```

## [ncat](https://nmap.org/ncat/)

todo
