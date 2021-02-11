# IPFS

Examples using IPFS

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

## Find Peers

```bash
ipfs dht findpeer QmYtQ3iJi5RAQYxWJLts7xN1dRNK2n258QEXk4N1eLMZFM
```

## Share encrypted files with IPFS

create key

```bash
gpg --gen-key
gpg --export --armor -email > pubkey.asc
```

share and import key

```bash
gpg --import pubkey.asc
gpg --list-keys
```

share enrypted files

```bash
ipfs init
gpg --encrypt --recipient "Cory Heath" myriad.pdf
ipfs add myriad.pdf.gpg
```

get encrypted files

```bash
ipfs get QmYqSCWuzG8cYo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL
gpg --decrypt QmYqSCWUZg8Cyo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL > myriad.pdf
```
