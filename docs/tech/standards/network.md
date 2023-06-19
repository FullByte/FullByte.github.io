# Network

## Ports

<http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml>
<https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers>

## Subnet

### IPv4

| CIDR | Subnet          | Addresses  | Wildcard      |
|------|-----------------|------------|---------------|
| /32  | 255.255.255.255 | 1          | 0.0.0.0       |
| /31  | 255.255.255.254 | 2          | 0.0.0.1       |
| /30  | 255.255.255.252 | 4          | 0.0.0.3       |
| /29  | 255.255.255.248 | 8          | 0.0.0.7       |
| /28  | 255.255.255.240 | 16         | 0.0.0.15      |
| /27  | 255.255.255.224 | 32         | 0.0.0.31      |
| /26  | 255.255.255.192 | 64         | 0.0.0.63      |
| /25  | 255.255.255.128 | 128        | 0.0.0.127     |
| /24  | 255.255.255.0   | 256        | 0.0.0.255     |
| /23  | 255.255.254.0   | 512        | 0.0.1.255     |
| /22  | 255.255.252.0   | 1024       | 0.0.3.255     |
| /21  | 255.255.248.0   | 2048       | 0.0.7.255     |
| /20  | 255.255.240.0   | 4096       | 0.0.15.255    |
| /19  | 255.255.224.0   | 8192       | 0.0.31.255    |
| /18  | 255.255.192.0   | 16,384     | 0.0.63.255    |
| /17  | 255.255.128.0   | 32,768     | 0.0.127.255   |
| /16  | 255.255.0.0     | 65,536     | 0.0.255.255   |
| /15  | 255.254.0.0     | 131,072    | 0.1.255.255   |
| /14  | 255.252.0.0     | 262,144    | 0.3.255.255   |
| /13  | 255.248.0.0     | 524,288    | 0.7.255.255   |
| /12  | 255.240.0.0     | 1,048,576  | 0.15.255.255  |
| /11  | 255.224.0.0     | 2,097,152  | 0.31.255.255  |
| /10  | 255.192.0.0     | 4,194,304  | 0.63.255.255  |
| /9   | 255.128.0.0     | 8,388,608  | 0.127.255.255 |
| /8   | 255.0.0.0       | 16,777,216 | 0.255.255.255 |

### IPv6

| Prefix | /48  | /56  | /64  | /127     | # Addresses |
|--------|------|------|------|----------|-------------|
| /24    | 16M  | 4G   | 1T   | 8388608Y | 16777216Y   |
| /25    | 8M   | 2G   | 512G | 4194304Y | 8388608Y    |
| /26    | 4M   | 1G   | 256G | 2097152Y | 4194304Y    |
| /27    | 2M   | 512M | 128G | 1048576Y | 2097152Y    |
| /28    | 1M   | 256M | 64G  | 524288Y  | 1048576Y    |
| /29    | 512K | 128M | 32G  | 262144Y  | 524288Y     |
| /30    | 256K | 64M  | 16G  | 131072Y  | 262144Y     |
| /31    | 128K | 32M  | 8G   | 65536Y   | 131072Y     |
| /32    | 64K  | 16M  | 4G   | 32768Y   | 65536Y      |
| /33    | 32K  | 8M   | 2G   | 16384Y   | 32768Y      |
| /34    | 16K  | 4M   | 1G   | 8192Y    | 16384Y      |
| /35    | 8K   | 2M   | 512M | 4096Y    | 8192Y       |
| /36    | 4K   | 1M   | 256M | 2048Y    | 4096Y       |
| /37    | 2K   | 512K | 128M | 1024Y    | 2048Y       |
| /38    | 1K   | 256K | 64M  | 512Y     | 1024Y       |
| /39    | 512  | 128K | 32M  | 256Y     | 512Y        |
| /40    | 256  | 64K  | 16M  | 128Y     | 256Y        |
| /41    | 128  | 32K  | 8M   | 64Y      | 128Y        |
| /42    | 64   | 16K  | 4M   | 32Y      | 64Y         |
| /43    | 32   | 8K   | 2M   | 16Y      | 32Y         |
| /44    | 16   | 4K   | 1M   | 8Y       | 16Y         |
| /45    | 8    | 2K   | 512K | 4Y       | 8Y          |
| /46    | 4    | 1K   | 256K | 2Y       | 4Y          |
| /47    | 2    | 512  | 128K | 1Y       | 2Y          |
| /48    | 1    | 256  | 64K  | 512Z     | 1Y          |
| /49    |      | 128  | 32K  | 256Z     | 512Z        |
| /50    |      | 64   | 16K  | 128Z     | 256Z        |
| /51    |      | 32   | 8K   | 64Z      | 128Z        |
| /52    |      | 16   | 4K   | 32Z      | 64Z         |
| /53    |      | 8    | 2K   | 16Z      | 32Z         |
| /54    |      | 4    | 1K   | 8Z       | 16Z         |
| /55    |      | 2    | 512  | 4Z       | 8Z          |
| /56    |      | 1    | 256  | 2Z       | 4Z          |
| /57    |      |      | 128  | 1Z       | 2Z          |
| /58    |      |      | 64   | 512E     | 1Z          |
| /59    |      |      | 32   | 256E     | 512E        |
| /60    |      |      | 16   | 128E     | 256E        |
| /61    |      |      | 8    | 64E      | 128E        |
| /62    |      |      | 4    | 32E      | 64E         |
| /63    |      |      | 2    | 16E      | 32E         |
| /64    |      |      | 1    | 8E       | 16E         |

## IP addresses

The IETF has reserved the address block of 192.0.0.0/24 for use for special purposes relating to protocol assignments. This registry contains the current assignments made by the IETF from this address block. Address prefixes listed in the Special-Purpose Address Registry are not guaranteed routability in any particular local or global context. Source: <https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml>

|        Address Block #         |                  Name #                   |                 RFC #                 | Allocation Date # | Termination Date # |
|:------------------------------:|:-----------------------------------------:|:-------------------------------------:|:-----------------:|:------------------:|
|           0.0.0.0/8            |              "This network"               |         [RFC791], Section 3.2         |      1981-09      |        N/A         |
|           0.0.0.0/32           |        "This host on this network"        |      [RFC1122], Section 3.2.1.3       |      1981-09      |        N/A         |
|           10.0.0.0/8           |                Private-Use                |               [RFC1918]               |      1996-02      |        N/A         |
|         100.64.0.0/10          |           Shared Address Space            |               [RFC6598]               |      2012-04      |        N/A         |
|          127.0.0.0/8           |                 Loopback                  |      [RFC1122], Section 3.2.1.3       |      1981-09      |        N/A         |
|         169.254.0.0/16         |                Link Local                 |               [RFC3927]               |      2005-05      |        N/A         |
|         172.16.0.0/12          |                Private-Use                |               [RFC1918]               |      1996-02      |        N/A         |
|        192.0.0.0/24 [2]        |         IETF Protocol Assignments         |        [RFC6890], Section 2.1         |      2010-01      |        N/A         |
|          192.0.0.0/29          |      IPv4 Service Continuity Prefix       |               [RFC7335]               |      2011-06      |        N/A         |
|          192.0.0.8/32          |            IPv4 dummy address             |               [RFC7600]               |      2015-03      |        N/A         |
|          192.0.0.9/32          |       Port Control Protocol Anycast       |               [RFC7723]               |      2015-10      |        N/A         |
|         192.0.0.10/32          | Traversal Using Relays around NAT Anycast |               [RFC8155]               |      2017-02      |        N/A         |
| 192.0.0.170/32, 192.0.0.171/32 |           NAT64/DNS64 Discovery           |    [RFC8880][RFC7050], Section 2.2    |      2013-02      |        N/A         |
|          192.0.2.0/24          |        Documentation (TEST-NET-1)         |               [RFC5737]               |      2010-01      |        N/A         |
|        192.31.196.0/24         |                 AS112-v4                  |               [RFC7535]               |      2014-12      |        N/A         |
|        192.52.193.0/24         |                    AMT                    |               [RFC7450]               |      2014-12      |        N/A         |
|         192.88.99.0/24         |      Deprecated (6to4 Relay Anycast)      |               [RFC7526]               |      2001-06      |      2015-03       |
|         192.168.0.0/16         |                Private-Use                |               [RFC1918]               |      1996-02      |        N/A         |
|        192.175.48.0/24         |      Direct Delegation AS112 Service      |               [RFC7534]               |      1996-01      |        N/A         |
|         198.18.0.0/15          |               Benchmarking                |               [RFC2544]               |      1999-03      |        N/A         |
|        198.51.100.0/24         |        Documentation (TEST-NET-2)         |               [RFC5737]               |      2010-01      |        N/A         |
|         203.0.113.0/24         |        Documentation (TEST-NET-3)         |               [RFC5737]               |      2010-01      |        N/A         |
|          240.0.0.0/4           |                 Reserved                  |         [RFC1112], Section 4          |      1989-08      |        N/A         |
|       255.255.255.255/32       |             Limited Broadcast             | [RFC8190]         [RFC919], Section 7 |      1984-10      |        N/A         |

Further, useful lists:

- [IPv4 Blocks](https://en.wikipedia.org/wiki/List_of_assigned_/8_IPv4_address_blocks)
- [Reserved IP Addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses)
- [IP ranges by country](https://github.com/herrbischoff/country-ip-blocks)
- [Cybercrime IP Feed](https://iplists.firehol.org/)

### IPv4 possible notations

All possible notations of the IPv4 address 8.8.8.8 ([source](https://lucb1e.com/randomprojects/php/funnip.php?ip=8.8.8.8))

- 8.8.8.8
- 134744072
- 0x8080808
- 01002004010
- 8.526344
- 8.0x80808
- 8.02004010
- 8.8.2056
- 8.8.0x808
- 8.8.04010
- 8.8.8.0x8
- 8.8.8.010
- 8.8.0x8.8
- 8.8.0x8.0x8
- 8.8.0x8.010
- 8.8.010.8
- 8.8.010.0x8
- 8.8.010.010
- 8.0x8.2056
- 8.0x8.0x808
- 8.0x8.04010
- 8.0x8.8.8
- 8.0x8.8.0x8
- 8.0x8.8.010
- 8.0x8.0x8.8
- 8.0x8.0x8.0x8
- 8.0x8.0x8.010
- 8.0x8.010.8
- 8.0x8.010.0x8
- 8.0x8.010.010
- 8.010.2056
- 8.010.0x808
- 8.010.04010
- 8.010.8.8
- 8.010.8.0x8
- 8.010.8.010
- 8.010.0x8.8
- 8.010.0x8.0x8
- 8.010.0x8.010
- 8.010.010.8
- 8.010.010.0x8
- 8.010.010.010
- 0x8.526344
- 0x8.0x80808
- 0x8.02004010
- 0x8.8.2056
- 0x8.8.0x808
- 0x8.8.04010
- 0x8.8.8.8
- 0x8.8.8.0x8
- 0x8.8.8.010
- 0x8.8.0x8.8
- 0x8.8.0x8.0x8
- 0x8.8.0x8.010
- 0x8.8.010.8
- 0x8.8.010.0x8
- 0x8.8.010.010
- 0x8.0x8.2056
- 0x8.0x8.0x808
- 0x8.0x8.04010
- 0x8.0x8.8.8
- 0x8.0x8.8.0x8
- 0x8.0x8.8.010
- 0x8.0x8.0x8.8
- 0x8.0x8.0x8.0x8
- 0x8.0x8.0x8.010
- 0x8.0x8.010.8
- 0x8.0x8.010.0x8
- 0x8.0x8.010.010
- 0x8.010.2056
- 0x8.010.0x808
- 0x8.010.04010
- 0x8.010.8.8
- 0x8.010.8.0x8
- 0x8.010.8.010
- 0x8.010.0x8.8
- 0x8.010.0x8.0x8
- 0x8.010.0x8.010
- 0x8.010.010.8
- 0x8.010.010.0x8
- 0x8.010.010.010
- 010.526344
- 010.0x80808
- 010.02004010
- 010.8.2056
- 010.8.0x808
- 010.8.04010
- 010.8.8.8
- 010.8.8.0x8
- 010.8.8.010
- 010.8.0x8.8
- 010.8.0x8.0x8
- 010.8.0x8.010
- 010.8.010.8
- 010.8.010.0x8
- 010.8.010.010
- 010.0x8.2056
- 010.0x8.0x808
- 010.0x8.04010
- 010.0x8.8.8
- 010.0x8.8.0x8
- 010.0x8.8.010
- 010.0x8.0x8.8
- 010.0x8.0x8.0x8
- 010.0x8.0x8.010
- 010.0x8.010.8
- 010.0x8.010.0x8
- 010.0x8.010.010
- 010.010.2056
- 010.010.0x808
- 010.010.04010
- 010.010.8.8
- 010.010.8.0x8
- 010.010.8.010
- 010.010.0x8.8
- 010.010.0x8.0x8
- 010.010.0x8.010
- 010.010.010.8
- 010.010.010.0x8
- 010.010.010.010

## TTL as OS identifier

There is a chance to guess the OS based on its TTL.

Here is an overview:

| OS                | Version               | Protocol     | TTL |
|-------------------|-----------------------|--------------|-----|
| *nix (Linux/Unix) |                       |              | 64  |
| AIX               | 3.2, 4.1              | ICMP         | 255 |
| AIX               |                       | TCP          | 60  |
| AIX               |                       | UDP          | 30  |
| BSDI              | BSD/OS 3.1 and 4.0    | ICMP         | 255 |
| Cisco             |                       | ICMP         | 254 |
| Compa             | Tru64 v5.0            | ICMP         | 64  |
| DEC Pathworks     | V5                    | TCP and UDP  | 30  |
| Foundry           |                       | ICMP         | 64  |
| FreeBSD           | 5                     | ICMP         | 64  |
| FreeBSD           | 3.4, 4.0              | ICMP         | 255 |
| FreeBSD           | 2.1R                  | TCP and UDP  | 64  |
| HP-UX             | 9.0x                  | TCP and UDP  | 30  |
| HP-UX             | 11                    | ICMP         | 255 |
| HP-UX             | 11                    | TCP          | 64  |
| HP-UX             | 10.2                  | ICMP         | 255 |
| HP-UX             | 10.01                 | TCP and UDP  | 64  |
| Irix              | 6.x                   | TCP and UDP  | 60  |
| Irix              | 6.5.3, 6.5.8          | ICMP         | 255 |
| Irix              | 5.3                   | TCP and UDP  | 60  |
| Linux             | Red Hat 9             | ICMP and TCP | 64  |
| Linux             | 2.4 kernel            | ICMP         | 255 |
| Linux             | 2.2.14 kernel         | ICMP         | 255 |
| Linux             | 2.0.x kernel          | ICMP         | 64  |
| MPE/IX (HP)       |                       | ICMP         | 200 |
| MacOS/MacTCP      | X (10.5.6)            | ICMP/TCP/UDP | 64  |
| MacOS/MacTCP      | 2.0.x                 | TCP and UDP  | 60  |
| NetBSD            |                       | ICMP         | 255 |
| Netgear FVG318    |                       | ICMP and UDP | 64  |
| OS/2              |                       | TCP/IP 3.0   | 64  |
| OSF/1             | V3.2A                 | TCP          | 60  |
| OSF/1             | V3.2A                 | UDP          | 30  |
| OpenBSD           | 2.6 & 2.7             | ICMP         | 255 |
| OpenVMS           | 07.01.2002            | ICMP         | 255 |
| Solaris           | 2.8                   | TCP          | 64  |
| Solaris           | 2.5.1, 2.6, 2.7, 2.8  | ICMP         | 255 |
| Solaris/AIX       |                       |              | 254 |
| Stratus           | TCP_OS (14.3+)        | TCP and UDP  | 64  |
| Stratus           | TCP_OS (14.2-)        | TCP and UDP  | 30  |
| Stratus           | TCP_OS                | ICMP         | 255 |
| Stratus           | STCP                  | ICMP/TCP/UDP | 60  |
| SunOS             | 5.7                   | ICMP and TCP | 255 |
| SunOS             | 4.1.3/4.1.4           | TCP and UDP  | 60  |
| Ultrix            | V4.2 – 4.5            | ICMP         | 255 |
| Ultrix            | V4.1/V4.2A            | TCP          | 60  |
| Ultrix            | V4.1/V4.2A            | UDP          | 30  |
| VMS/Multinet      |                       | TCP and UDP  | 64  |
| VMS/TCPware       |                       | TCP          | 60  |
| VMS/TCPware       |                       | UDP          | 64  |
| VMS/UCX           |                       | TCP and UDP  | 128 |
| VMS/Wollongong    | 1.1.1.1               | TCP          | 128 |
| VMS/Wollongong    | 1.1.1.1               | UDP          | 30  |
| Windows           | for Workgroups        | TCP and UDP  | 32  |
| Windows           | XP                    | ICMP/TCP/UDP | 128 |
| Windows           | Vista                 | ICMP/TCP/UDP | 128 |
| Windows           | Server 2008           | ICMP/TCP/UDP | 128 |
| Windows           | Server 2003           |              | 128 |
| Windows           | NT 4.0 SP6+           |              | 128 |
| Windows           | NT 4.0 SP5-           |              | 32  |
| Windows           | NT 4.0                | TCP and UDP  | 128 |
| Windows           | NT 4 WRKS SP 3, SP 6a | ICMP         | 128 |
| Windows           | NT 4 Server SP4       | ICMP         | 128 |
| Windows           | NT 3.51               | TCP and UDP  | 32  |
| Windows           | ME                    | ICMP         | 128 |
| Windows           | 98, 98 SE             | ICMP         | 128 |
| Windows           | 98                    | ICMP         | 32  |
| Windows           | 98                    | TCP          | 128 |
| Windows           | 95                    | TCP and UDP  | 32  |
| Windows           | 7                     | ICMP/TCP/UDP | 128 |
| Windows           | 2000 pro              | ICMP/TCP/UDP | 128 |
| Windows           | 2000 family           | ICMP         | 128 |
| Windows           | 10                    | ICMP/TCP/UDP | 128 |
| Windows           |                       |              | 128 |
| juniper           |                       | ICMP         | 64  |
