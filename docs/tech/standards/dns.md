# DNS

## Public DNS

A list of public DNS Servers

| Provider                                                                     | IPv4                              | IPv6                                                    | DNS over HTTPS & TLS                                                                                       |
|------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [AliDNS](https://alidns.com/)                                                | 223.5.5.5 / 223.6.6.6             |                                                         | [HTTPS](https://dns.alidns.com/dns-query), [TLS](tls://9999.alidns.com):                                   |
| [Alternate DNS](https://alternate-dns.com/)                                  | 198.101.242.72 / 23.253.163.53    | 2602:fcbc::ad / 2001:4800:780e:510:a8cf:392e:ff04:8982  | [HTTPS](https://dns.alternate-dns.com/dns-query), [TLS](tls://dns.alternate-dns.com)                       |
| [Cisco OpenDNS FamilyShield](https://www.opendns.com/cisco-opendns/)         | 208.67.222.123 / 208.67.220.123   | 2620:119:35::123 / 2620:119:53::123                     | [HTTPS](https://doh.familyshield.opendns.com/dns-query)                                                    |
| [Cisco OpenDNS Standards](https://www.opendns.com/cisco-opendns/)            | 208.67.222.222 / 208.67.220.220   | 2620:119:35::35 / 2620:119:53::53                       | [HTTPS](https://doh.opendns.com/dns-query)                                                                 |
| [CleanBrowsing Adult](https://cleanbrowsing.org/guides/)                     | 185.228.168.10 / 185.228.169.11   | 2a0d:2a00:1::1 / 2a0d:2a00:2::1                         | [HTTPS](https://adult-filter-dns.cleanbrowsing.org)                                                        |
| [CleanBrowsing Family](https://cleanbrowsing.org/guides/)                    | 185.228.168.168 / 185.228.169.168 | 2a0d:2a00:1:: / 2a0d:2a00:2::                           | [HTTPS](https://family-filter-dns.cleanbrowsing.org)                                                       |
| [CleanBrowsing Security](https://cleanbrowsing.org/guides/)                  | 185.228.168.9 / 185.228.169.9     | 2a0d:2a00:1::2 / 2a0d:2a00:2::2                         | [HTTPS](https://security-filter-dns.cleanbrowsing.org)                                                     |
| [Cloudflare](https://developers.cloudflare.com/1.1.1.1/)                     | 1.1.1.1 / 1.0.0.1                 | 2606:4700:4700::1111 / 2606:4700:4700::1001             | [HTTPS](https://1dot1dot1dot1.cloudflare-dns.com)                                                          |
| [Comodo DNS](https://securedns.dnsbycomodo.com/support/)                     | 8.26.56.26 / 8.20.247.20          | N/A                                                     | N/A                                                                                                        |
| [Comodo Secure Internet Gateway](https://securedns.dnsbycomodo.com/support/) | 8.26.56.10 / 8.20.247.10          | N/A                                                     | N/A                                                                                                        |
| [Digital Courage](https://digitalcourage.de/support/zensurfreier-dns-server) | 5.9.164.112 / 46.182.19.48        | 2a02:2970:1002::18                                      | [HTTPS](https://dns3.digitalcourage.de)                                                                    |
| [dns.watch](https://dns.watch/)                                              | 84.200.69.80 / 84.200.70.40       | 2001:1608:10:25::1c04:b12f / 2001:1608:10:25::9249:d69b | [HTTPS](https://resolver2.dns.watch/dns-query)                                                             |
| [Dyn DNS](https://help.dyn.com/internet-guide-setup/)                        | 216.146.35.35 / 216.146.36.36     | N/A                                                     | N/A                                                                                                        |
| [FreeDNS](https://freedns.zone)                                              | 172.104.237.57 / 37.235.1.177     | N/A                                                     | N/A                                                                                                        |
| [Google](https://developers.google.com/speed/public-dns/docs/using)          | 8.8.8.8 / 8.8.4.4                 | 2001:4860:4860::8888 / 2001:4860:4860::8844             | [HTTPS](https://dns.google), [TLS](tls://dns.google)                                                       |
| [Hurricane Electric](https://dns.he.net/)                                    | 74.82.42.42                       | 2001:470:20::2                                          | N/A                                                                                                        |
| [OpenNIC](https://servers.opennic.org/)                                      | 69.195.152.204 / 23.94.60.240     | N/A                                                     | N/A                                                                                                        |
| [Quad9](https://www.quad9.net/service/service-addresses-and-features/)       | 9.9.9.9 /  149.112.112.112        | 2620:fe::fe / 2620:fe::9                                | [HTTPS](https://dns11.quad9.net/dns-query), [TLS](tls://dns11.quad9.net)                                   |
| [UncensoredDNS](https://blog.uncensoreddns.org/dns-servers/)                 | 91.239.100.100 / 89.233.43.71     | 2001:67c:28a4:: / 2a01:3a0:53:53::                      | [HTTPS](https://anycast.uncensoreddns.org/dns-query), [HTTPS](https://unicast.uncensoreddns.org/dns-query) |
| [Yandex.DNS Standard](https://dns.yandex.com/)                               | 77.88.8.8 / 77.88.8.1             | N/A                                                     | N/A                                                                                                        |
| [Yandex.DNS Safe](https://dns.yandex.com/)                                   | 77.88.8.88 / 77.88.8.2            | N/A                                                     | N/A                                                                                                        |
| [Yandex.DNS Family](https://dns.yandex.com/)                                 | 77.88.8.7 / 77.88.8.3             | N/A                                                     | N/A                                                                                                        |

## DDNS service

- [DuckDNS](https://www.duckdns.org/)
- [Cloudflare Tunnels](https://www.cloudflare.com/products/tunnel/)

## DNS root zones

A list of [DNS root zones](https://www.iana.org/domains/root/servers):

| Hostname           | IPv4           | IPv6                | Operator                                                         |
|--------------------|----------------|---------------------|------------------------------------------------------------------|
| a.root-servers.net | 198.41.0.4     | 2001:503:ba3e::2:30 | Verisign Inc.                                                    |
| b.root-servers.net | 199.9.14.201   | 2001:500:200::b     | University of Southern California Information Sciences Institute |
| c.root-servers.net | 192.33.4.12    | 2001:500:2::c       | Cogent Communications                                            |
| d.root-servers.net | 199.7.91.13    | 2001:500:2d::d      | University of Maryland                                           |
| e.root-servers.net | 192.203.230.10 | 2001:500:a8::e      | NASA (Ames Research Center)                                      |
| f.root-servers.net | 192.5.5.241    | 2001:500:2f::f      | Internet Systems Consortium Inc.                                 |
| g.root-servers.net | 192.112.36.4   | 2001:500:12::d0d    | US Department of Defense (NIC)                                   |
| h.root-servers.net | 198.97.190.53  | 2001:500:1::53      | US Army (Research Lab)                                           |
| i.root-servers.net | 192.36.148.17  | 2001:7fe::53        | Netnod                                                           |
| j.root-servers.net | 192.58.128.30  | 2001:503:c27::2:30  | Verisign Inc.                                                    |
| k.root-servers.net | 193.0.14.129   | 2001:7fd::1         | RIPE NCC                                                         |
| l.root-servers.net | 199.7.83.42    | 2001:500:9f::42     | ICANN                                                            |
| m.root-servers.net | 202.12.27.33   | 2001:dc3::35        | WIDE Project                                                     |

## More Services

DNS Services

- <https://www.rethinkdns.com/>
- [DNS toys](https://www.dns.toys) offers some handy utilites (time, conversions, weather)
- [NextDNS API](https://nextdns.github.io/api/)

DNS Provider

- <https://www.publicdns.xyz/>
- <https://public-dns.info/>
- <https://dns.google/>

Other Lists

- ISPs per country <https://www.nirsoft.net/countryip/>
- Root zones: <https://www.internic.net/domain/root.zone>
- Root Servers: <https://root-servers.org/>
