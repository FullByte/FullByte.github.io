# Fastmail

[Fastmail](https://www.fastmail.com/) is a great email service. This page deals with helpful settings.

## DNS

### Mail

Nobody want to hear that the mail they sent landed in SPAM folder. Here are some things that can be done to prevent that from happening.

Links to relevant Fastmail help pages:

- [Custom Domains with Fastmail](https://www.fastmail.help/hc/en-us/articles/360058753394)
- [Manual DNS settings](https://www.fastmail.help/hc/en-us/articles/360060591113-Manual-DNS-settings)
- [Setting up your domain: NS/MX](https://www.fastmail.help/hc/en-us/articles/1500000278002-Setting-up-your-domain-NS-MX)
- [Domain set up: MX only](https://www.fastmail.help/hc/en-us/articles/1500000280261-Domain-set-up-MX-only)
- [Domains: Advanced configuration](https://www.fastmail.help/hc/en-us/articles/360060591153-Domains-Advanced-configuration)

Further helpful tools to check DNS settings

- [mxtoolbox](https://mxtoolbox.com)
- [straight2spam](https://straight2spam.xyz/)
- [mailhardener](https://www.mailhardener.com)
- [mail-tester](https://www.mail-tester.com)

#### Basic Settings

IMAP and POP3: Allows email clients to automatically find the correct settings for your account.

``` txt
SRV _submission._tcp.0xfab1.net 0 1 587 smtp.fastmail.com
SRV _imap._tcp.0xfab1.net 0 0 0 .
SRV _imaps._tcp.0xfab1.net 0 1 993 imap.fastmail.com
SRV _pop3._tcp.0xfab1.net 0 0 0 .
SRV _pop3s._tcp.0xfab1.net 10 1 995 pop.fastmail.com
SRV _jmap._tcp.0xfab1.net 0 1 443 jmap.fastmail.com
```

CardDAV auto-discovery: Allows CardDAV clients to automatically find the correct settings for your account.

``` txt
SRV _carddav._tcp.0xfab1.net 0 0 0 .
SRV _carddavs._tcp.0xfab1.net 0 1 443 carddav.fastmail.com
```

CalDAV auto-discovery: Allows CalDAV clients to automatically find the correct settings for your account.

``` txt
SRV _caldav._tcp.0xfab1.net 0 0 0 .
SRV _caldavs._tcp.0xfab1.net 0 1 443 caldav.fastmail.com
```

#### Authentic sender

**BIMI**: A BIMI Record is a type of DNS Record that is used to display a company logo inside an email inbox if the email is legitimate. Using BIMI requires ensuring DMARC authentication is set up on the domain. In fact, the BIMI concept is viewed as an extension of DMARC. Both protocols are highly beneficial to ensuring a domain’s messages are delivered and to help crack down on phishing and spoofing attempts.

DNS Settings:

``` txt
Record Type: TXT
Host : default._bimi
Value: v=BIMI1;l=https://0xfab1.net/logo.svg;
```

**DMARC**: Domain-based Message Authentication, Reporting and Conformance ([DMARC](https://datatracker.ietf.org/doc/html/rfc7489)) extends SPF and DKIM validation by adding a third validation known as alignment. Besides alignment validation, DMARC can also be used to request reporting from receiving email systems, mainly Aggregate Report (RUA) address and Forensic Report (RUF) address.

DNS Settings:

``` txt
Record Type: TXT
Host : _dmarc 
Value: v=DMARC1; p=none; rua=mailto:aggregat@0xfab1.net; ruf=mailto:forensic@0xfab1.net;
```

**MTA-STS**: Mail Transfer Agent Strict Transport Security is an email security standard which lets senders know that your email server accepts secure email delivery using SMTP over TLS (STARTTLS), and that email should not be delivered over an insecure SMTP connection. MTA-STS mitigates Man-In-The-Middle DNS and SMTP downgrade attacks that would allow an attacker to read or manipulate email in transit.

DMS emtry

``` txt
Record Type: TXT
Host : _dmarc 
Value: v=STSv1; id=20220202T000000;
```

File name `mta-sts.txt` reachable over https://mta-sts.0xfab1.net/.well-known/mta-sts.txt

``` txt
version: STSv1
mode: enforce
mx: in1-smtp.messagingengine.com
mx: in2-smtp.messagingengine.com
max_age: 604800
```

**TLS-RPT**: [SMTP TLS Reporting](https://datatracker.ietf.org/doc/html/rfc8460) (sometimes abbreviated as TLS-RPT) is a reporting standard for secure email delivery. SMTP TLS reporting is especially valuable in combination with MTA-STS, as enforced mode in MTA-STS will result in undeliverable email if there is a problem with TLS.

``` txt
Record Type: TXT
Host : _smtp._tls
Value: v=TLSRPTv1; rua=mailto:tlsrpt@0xfab1.net,https://tlsrpt.0xfab1.net/v1;
```

**SPF**: The Sender Policy Framework (SPF) allows domain owners to publish a policy about which senders are allowed to send email for that domain. Receivers use SPF as one of the methods for spam detection.

``` txt
Record Type : TXT
Host : @
Value: v=spf1 mx a ip4:66.111.4.54 mx:in1-smtp.messagingengine.com -all
```

**DKIM**: With DomainKeys Identified Mail ([DKIM](https://datatracker.ietf.org/doc/html/rfc6376)) the sending email system adds a cryptographic signature to the email headers using its private key. This signature is used by the receiving system to determine if the sender, and the email content, are to be trusted.
