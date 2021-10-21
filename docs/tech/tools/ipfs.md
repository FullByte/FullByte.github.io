# IPFS

Examples using IPFS

## Info

|What|Where|
|-|-|
|Official Page|<https://ipfs.io/>|
|Documentation|<https://docs.ipfs.io/>|
|Source|<https://github.com/ipfs>|
|Download|<https://github.com/ipfs/go-ipfs/releases>|

## Find Peers

```sh
ipfs dht findpeer QmYtQ3iJi5RAQYxWJLts7xN1dRNK2n258QEXk4N1eLMZFM
```

## Share encrypted files with IPFS

create key

```sh
gpg --gen-key
gpg --export --armor -email > pubkey.asc
```

share and import key

```sh
gpg --import pubkey.asc
gpg --list-keys
```

share enrypted files

```sh
ipfs init
gpg --encrypt --recipient "Cory Heath" myriad.pdf
ipfs add myriad.pdf.gpg
```

get encrypted files

```sh
ipfs get QmYqSCWuzG8cYo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL
gpg --decrypt QmYqSCWUZg8Cyo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL > myriad.pdf
```

## Hosting

For 0xfab1.net I am using [fleek](https://fleek.co/) to host the website on IPFS.

With Fleek you get a fleek adress, the IPDS address and I added a CNAME to make it easy to reach:

- Fleek IPFS: <https://ipfs.fleek.co/ipfs/QmXUY11j72BsYCqURakrfFyVCBjdnNiEcPT7csXN5LRFaJ/>
- IPFS <https://ipfs.io/ipfs/QmXUY11j72BsYCqURakrfFyVCBjdnNiEcPT7csXN5LRFaJ>
- CNAME: <https://ipfs.0xfab1.net/>

List of public gateways: <https://ipfs.github.io/public-gateway-checker/>
