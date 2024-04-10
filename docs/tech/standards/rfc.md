# RFCs

![https://xkcd.com/927](_standards.png)

## Interesting RFCs

- First RFC (7 April 1969): <https://tools.ietf.org/html/rfc1>
- RFC Key word ("MUST", "REQUIRED", "SHALL", "SHOULD", "RECOMMENDED", "MAY", "OPTIONAL",..): <https://tools.ietf.org/html/rfc>
- Choosing a Name for Your Computer: <https://www.rfc-editor.org/rfc/rfc1178>
- The Twelve Networking Truths <https://www.rfc-editor.org/rfc/rfc1925>
- The Hyper Text Coffee Pot Control Protocol for Tea Efflux Appliances <https://www.rfc-editor.org/rfc/rfc7168> (Updates [RFC 2324](https://www.rfc-editor.org/rfc/rfc2324))
- IP over Avian Carriers with Quality of Service <https://datatracker.ietf.org/doc/html/rfc2549>

## SSH

### Core RFCs

|                 Specification                  |          Description          |
|:----------------------------------------------:|:-----------------------------:|
| [RFC4250](https://tools.ietf.org/html/rfc4250) | SSH Protocol Assigned Numbers |
| [RFC4251](https://tools.ietf.org/html/rfc4251) |   SSH Protocol Architecture   |
| [RFC4252](https://tools.ietf.org/html/rfc4252) |  SSH Authentication Protocol  |
| [RFC4253](https://tools.ietf.org/html/rfc4253) | SSH Transport Layer Protocol  |
| [RFC4254](https://tools.ietf.org/html/rfc4254) |    SSH Connection Protocol    |

### Extension RFCs

|                 Specification                  | Versions |                                    Description                                    |
|:----------------------------------------------:|:--------:|:---------------------------------------------------------------------------------:|
| [RFC4255](https://tools.ietf.org/html/rfc4255) |          |            Using DNS to Securely Publish SSH Key Fingerprints (SSHFP)             |
| [RFC4256](https://tools.ietf.org/html/rfc4256) |          |        Generic Message Exchange Authentication (aka keyboard-interactive)         |
| [RFC4335](https://tools.ietf.org/html/rfc4335) |          |                        SSH Session Channel Break Extension                        |
| [RFC4344](https://tools.ietf.org/html/rfc4344) |          |     SSH Transport Layer Encryption Modes (aes128-ctr, aes192-ctr, aes256-ctr)     |
| [RFC4345](https://tools.ietf.org/html/rfc4345) | 4.1-7.6  |            Improved Arcfour Modes for the SSH Transport Layer Protocol            |
| [RFC4419](https://tools.ietf.org/html/rfc4419) |          |                           Diffie-Hellman Group Exchange                           |
| [RFC4462](https://tools.ietf.org/html/rfc4462) |          |     GSS-API Authentication and Key Exchange (only authentication implemented)     |
| [RFC4716](https://tools.ietf.org/html/rfc4716) |          |        SSH Public Key File Format (import and export via ssh-keygen only).        |
| [RFC5656](https://tools.ietf.org/html/rfc5656) |          |                    Elliptic Curve Algorithm Integration in SSH                    |
| [RFC6594](https://tools.ietf.org/html/rfc6594) |   6.1-   |                          SHA-256 SSHFP Resource Records                           |
| [RFC6668](https://tools.ietf.org/html/rfc6668) |   5.9-   |          SHA-2 Data Integrity Algorithms (hmac-sha2-256, hmac-sha2-512)           |
| [RFC7479](https://tools.ietf.org/html/rfc7479) |   6.5-   |                          ED25519 SSHFP Resource Records                           |
| [RFC8160](https://tools.ietf.org/html/rfc8160) |   7.3-   |                                IUTF8 Terminal Mode                                |
| [RFC8270](https://tools.ietf.org/html/rfc8270) |   7.1-   |                       Increase Diffie-Hellman Modulus Size                        |
| [RFC8308](https://tools.ietf.org/html/rfc8308) |   7.2-   | Extension Negotiation in the Secure Shell (SSH) Protocol (ext-info-s, ext-info-c) |
| [RFC8332](https://tools.ietf.org/html/rfc8332) |   7.2-   |              Use of RSA Keys with SHA-2 (rsa-sha2-256, rsa-sha2-512)              |
| [RFC8709](https://tools.ietf.org/html/rfc8709) |   6.5-   |            Ed25519 and Ed448 Public Key Algorithms (ssh-ed25519 only)             |
| [RFC8731](https://tools.ietf.org/html/rfc8731) |   7.3-   |    Key Exchange Method Using Curve25519 and Curve448 (curve25519-sha256 only)     |

### Other

|                                         Specification                                          |                                                                                                                                          Description                                                                                                                                          |
|:----------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                         [RFC1928](https://tools.ietf.org/html/rfc1928)                         |                                                                                                                  SOCKS protocol version 5.  Used for ssh(1) DynamicForward.                                                                                                                   |
| [RFC1349](https://tools.ietf.org/html/rfc1349), [RFC8325](https://tools.ietf.org/html/rfc8325) | IP Type of Service (ToS) and Differentiated Services. OpenSSH will automatically set the IP Type of Service according to RFC8325 unless otherwise specified via the IPQoS keyword in ssh_config and sshd_config. Versions 7.7 and earlier will set it per rfc1349 unless otherwise specified. |
