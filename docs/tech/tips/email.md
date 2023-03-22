# Email

## Services

Services I use and like are listed here.

### Fastmail

[Fastmail](https://www.fastmail.com/) is a great email service.

Links to relevant Fastmail help pages:

- [Custom Domains with Fastmail](https://www.fastmail.help/hc/en-us/articles/360058753394)
- [Manual DNS settings](https://www.fastmail.help/hc/en-us/articles/360060591113-Manual-DNS-settings)
- [Setting up your domain: NS/MX](https://www.fastmail.help/hc/en-us/articles/1500000278002-Setting-up-your-domain-NS-MX)
- [Domain set up: MX only](https://www.fastmail.help/hc/en-us/articles/1500000280261-Domain-set-up-MX-only)
- [Domains: Advanced configuration](https://www.fastmail.help/hc/en-us/articles/360060591153-Domains-Advanced-configuration)

### Sendgrid

[Sendgrid](https://sendgrid.com/) is an email API service.

Powershell example on how to use the sendgrid API to send an email:

```ps1
$From = "email@address"
$To = "email@address"
$Cc = ""
$Bcc = ""
$APIKEY = "MY_API_KEY"
$Subject = "TEST"
$Body ="SENDGRID 123"

$headers = @{}
$headers.Add("Authorization","Bearer $apiKey")
$headers.Add("Content-Type", "application/json")

$jsonRequest = [ordered]@{
    personalizations= @(@{ to = @(@{email = "$To"}) subject = "$SubJect" })
    from = @{email = "$From"}
    content = @( @{ type = "text/plain"
    value = "$Body" })
} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Uri "https://api.sendgrid.com/v3/mail/send" -Method Post -Headers $headers -Body $jsonRequest 
```

Curl example on how to use the sendgrid API to send an email:

``` sh
export SENDGRID_API_KEY='something'

curl --request POST --url https://api.sendgrid.com/v3/mail/send --header "Authorization: Bearer $SENDGRID_API_KEY" --header 'Content-Type: application/json' --data '{"personalizations": [{"to": [{"email": "mail@to.you"}]}],"from": {"email": "bot@0xfab1.net"},"subject": "Hello world","content": [{"type": "text/plain", "value": "Nice, mailing with cURL :D"}]}'
```

## DNS

Further helpful tools to check DNS settings

- [mxtoolbox](https://mxtoolbox.com)
- [straight2spam](https://straight2spam.xyz/)
- [mailhardener](https://www.mailhardener.com)
- [mail-tester](https://www.mail-tester.com)

### Mail

Nobody wants to find out their email got sent to the addressed persons SPAM folder. Here are some DNS configurations that can be done to prevent that from happening.

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

##### BIMI

A BIMI Record is a type of DNS Record that is used to display a company logo inside an email inbox if the email is legitimate. Using BIMI requires ensuring DMARC authentication is set up on the domain. In fact, the BIMI concept is viewed as an extension of DMARC. Both protocols are highly beneficial to ensuring a domain’s messages are delivered and to help crack down on phishing and spoofing attempts.

DNS Settings:

``` txt
Record Type: TXT
Host : default._bimi
Value: v=BIMI1;l=https://0xfab1.net/logo.svg;
```

##### DMARC

Domain-based Message Authentication, Reporting and Conformance ([DMARC](https://datatracker.ietf.org/doc/html/rfc7489)) extends SPF and DKIM validation by adding a third validation known as alignment. Besides alignment validation, DMARC can also be used to request reporting from receiving email systems, mainly Aggregate Report (RUA) address and Forensic Report (RUF) address.

DNS Settings:

``` txt
Record Type: TXT
Host : _dmarc 
Value: v=DMARC1; p=none; rua=mailto:aggregat@0xfab1.net; ruf=mailto:forensic@0xfab1.net;
```

**Version** (v tag):

- Version of DMARC (v=DMARC1)

**Email information** (rua/ruf tag):

- Forensic feedback email: With the ruf tag you can decide where the DMARC forensic reports are sent to.
- Aggregate report email: With the rua tag you can decide where the DMARC aggregate reports are sent to.

**DMARC policy** (p tag):

- Monitor (p=none): With the DMARC policy none, Internet Service Providers who've DMARC will not do anything with email that fails the DMARC check. The email just goes into the inbox / folder of the receiver. This DMARC policy can be used to simply start analyzing who is sending emails on behalf of a domain.
- Quarantine (p=quarantine): With the DMARC policy quarantine, Internet Service Providers who've DMARC will put emails failing the DMARC check in special ‘quarantine' folders like the junk or spam folder. This DMARC policy influences the way email is handled, however failing emails will still arrive.
- Reject (p=reject): With the DMARC reject policy, Internet Service Providers who've DMARC will reject all emails that fail the DMARC check. All these email will bounce and will not end up in any folder of the receiver. This DMARC policy makes sure emails failing the DMARC check will not arrive. Be aware that everything should be in place otherwise legitimate email might be blocked.
- Policy percentage (pct=90 for 90%): The percentage tag instructs ISPs to only apply the DMARC policy to a percentage of failing emails. 'pct=50' will instruct receivers to only apply the policy for 50% of the emails that fail the DMARC check. NOTE: this will not work for the 'none' policy, but only for the 'quarantine' or 'reject' policies. E.g. for "100%" -> 100% of the messages will be filtered. The policy percentage can be a number form 1 to 100. Default is 100 which is all messages.

**Alignment mode** (adkim/aspf tag):

Since alignment is a key part of the DMARC implementation (without alignment you can't enforce your policy), it is possible to choose how alignment should be handled for DKIM signatures and your SPF setup. The chosen alignment mode influences when alignment is achieved. You can choose to set the alignment mode to 'r' (Relaxed) or 's' (Strict).

- DKIM alignment mode (adkim=s): For DKIM this means that the domain used to create the signature (and provided through the d= parameter), should match the ‘From' header. In Relaxed mode authenticated DKIM signing domains (d=) that share an organizational domain with an emails ‘From' domain will pass the DMARC check. In strict mode an exact match is required in order to achieve alignment.
- SPF alignment mode (aspf=s): For SPF this means that the ‘Return-Path' header should match the ‘From' header. In Relaxed mode authenticated SPF domains that share an organizational domain with an emails ‘From' domain will pass the DMARC check. In strict mode an exact match is required in order to achieve alignment.

**Forensic options** (fo tag)

Determines in which case you want to receive forensic reports:

- Report failures if all alignment and authentication fails
- Report failures if DKIM or SPF does not align and authentication fails (fo=1)
- Report failures if DKIM fails (fo=d)
- Report failures if SPF fails (fo=s)

##### MTA-STS

Mail Transfer Agent Strict Transport Security is an email security standard which lets senders know that your email server accepts secure email delivery using SMTP over TLS (STARTTLS), and that email should not be delivered over an insecure SMTP connection. MTA-STS mitigates Man-In-The-Middle DNS and SMTP downgrade attacks that would allow an attacker to read or manipulate email in transit.

DMS emtry

``` txt
Record Type: TXT
Host : _dmarc 
Value: v=STSv1; id=20220202T000000;
```

File name `mta-sts.txt` reachable over <https://mta-sts.0xfab1.net/mta-sts.txt>

``` txt
version: STSv1
mode: enforce
mx: in1-smtp.messagingengine.com
mx: in2-smtp.messagingengine.com
max_age: 604800
```

##### TLS-RPT

[SMTP TLS Reporting](https://datatracker.ietf.org/doc/html/rfc8460) (sometimes abbreviated as TLS-RPT) is a reporting standard for secure email delivery. SMTP TLS reporting is especially valuable in combination with MTA-STS, as enforced mode in MTA-STS will result in undeliverable email if there is a problem with TLS.

``` txt
Record Type: TXT
Host : _smtp._tls
Value: v=TLSRPTv1; rua=mailto:tlsrpt@0xfab1.net,https://tlsrpt.0xfab1.net/v1;
```

##### SPF

The Sender Policy Framework (SPF) allows domain owners to publish a policy about which senders are allowed to send email for that domain. Receivers use SPF as one of the methods for spam detection.

``` txt
Record Type : TXT
Host : @
Value: v=spf1 mx a ip4:66.111.4.54 mx:in1-smtp.messagingengine.com -all
```

##### DKIM

With DomainKeys Identified Mail ([DKIM](https://datatracker.ietf.org/doc/html/rfc6376)) the sending email system adds a cryptographic signature to the email headers using its private key. This signature is used by the receiving system to determine if the sender, and the email content, are to be trusted.
