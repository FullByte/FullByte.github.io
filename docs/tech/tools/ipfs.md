# IPFS

IPFS (InterPlanetary File System) is a distributed, peer-to-peer file storage and sharing system designed to make the web faster, safer, and more resilient. It is an open-source project that aims to address some of the limitations and centralization issues associated with traditional web protocols, like HTTP. IPFS works by leveraging a content-addressed, distributed file system, which means that files and other data are identified based on their cryptographic hash rather than their location on a specific server. This approach ensures that the content remains available even if a particular node goes offline, as multiple nodes can host the same content.

| What          | Where                                      |
|---------------|--------------------------------------------|
| Official Page | <https://ipfs.io/>                         |
| Documentation | <https://docs.ipfs.io/>                    |
| Source        | <https://github.com/ipfs>                  |
| Download      | <https://github.com/ipfs/go-ipfs/releases> |

In the following chapters there are some examples how to use IPFS.

## Find Peers

``` sh
ipfs dht findpeer QmYtQ3iJi5RAQYxWJLts7xN1dRNK2n258QEXk4N1eLMZFM
```

## Share encrypted files with IPFS

create key

``` sh
gpg --gen-key
gpg --export --armor -email > pubkey.asc
```

share and import key

``` sh
gpg --import pubkey.asc
gpg --list-keys
```

share enrypted files

``` sh
ipfs init
gpg --encrypt --recipient "Mr Universum" 0xfab1.pdf
ipfs add 0xfab1.pdf.gpg
```

get encrypted files

``` sh
ipfs get QmYqSCWuzG8cYo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL
gpg --decrypt QmYqSCWUZg8Cyo4MFQzqKcC14ct4ybAWyrAc9qzdJaFYTL > 0xfab1.pdf
```

## Fleek

I am using [fleek](https://fleek.co/) to host [0xfab1.net on IPFS](https://ipfs.0xfab1.net).

With Fleek you get a fleek adress, the IPFS address and I added a CNAME to make it easy to reach:

Here is a list of public gateways: <https://ipfs.github.io/public-gateway-checker/>
