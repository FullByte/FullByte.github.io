# Passwords

## Passwords in XML

Obviously it is a bad idea to have passwords in cleartext in XML files. If you do, remember that some chars need to be escaped or avoided. Most Unicode characters are allowed directly (without escaping), assuming the file is encoded in UTF-8. For example:

- Letters and numbers: A-Z, a-z, 0-9
- Special characters: ä, ö, ü, ß, €, @, etc.
- Whitespace and standard punctuation: ., ,, !, ?, _, -
- Special Unicode characters like German umlauts (ä, ö, ü, ß), symbols (€, @), or similar characters generally do not need escaping if UTF-8 encoding is used.

The following five characters have special meanings in XML and must always be escaped:

| Character | Meaning               | Escaped version |
|-----------|-----------------------|-----------------|
| <         | Less than             | &lt;            |
| >         | Greater than          | &gt;            |
| &         | Ampersand             | &amp;           |
| '         | Single quotation mark | &apos;          |
| "         | Double quotation mark | &quot;          |

XML forbids control characters (0x00–0x1F) except for Tab (0x09), Linefeed (0x0A), and Carriage Return (0x0D).

## Default Passwords

Passwords that are set by default or set if nothing else is configured:

| **Product**                       | **Username**  | **Password**          | **Notes**                                       |
|-----------------------------------|---------------|-----------------------|-------------------------------------------------|
| **3Com Switches**                 | admin         | admin                 | Default for many older 3Com switches            |
| **Alpine Linux**                  | root          | (no password)         | No password, requires setup after boot          |
| **Android (ADB interface)**       | root          | (no password)         | Root access is disabled in most builds          |
| **Apple Airport**                 | admin         | public                | Older versions of Apple Airport routers         |
| **Arch Linux**                    | root          | (no password)         | No password by default, requires manual setup   |
| **Aruba Networks**                | admin         | admin                 | Default login for Aruba switches and routers    |
| **Brocade Switches**              | admin         | password              | Common on Brocade networking devices            |
| **Buffalo LinkStation NAS**       | admin         | password              | Default for older Buffalo LinkStation models    |
| **Cisco Devices**                 | admin / cisco | admin / cisco         | Common for Cisco routers and switches           |
| **Debian Live CD**                | user          | live                  | Default for live CD boot images                 |
| **Dell iDRAC**                    | root          | calvin                | Remote management interface default             |
| **Docker (swarm root)**           | root          | (no password)         | No password for Docker swarm by default         |
| **DrayTek Routers**               | admin         | admin                 | Default for DrayTek devices                     |
| **Elasticsearch**                 | elastic       | changeme              | Default user/password for Elastic stack         |
| **Fedora Live CD**                | liveuser      | (no password)         | Default for Fedora live images                  |
| **Fortinet Firewall**             | admin         | (no password)         | No password set on Fortinet devices             |
| **Foscam Cameras**                | admin         | admin                 | Default for some Foscam models                  |
| **GitLab (Community Edition)**    | root          | 5iveL!fe              | Default for GitLab after fresh installation     |
| **GlassFish Server**              | admin         | adminadmin            | Default login for GlassFish administration      |
| **Grafana**                       | admin         | admin                 | Default admin login for Grafana                 |
| **HP iLO**                        | Administrator | Label-specific        | Password found on device label                  |
| **Hikvision IP Cameras**          | admin         | 12345                 | Default for many Hikvision IP cameras           |
| **Huawei Routers**                | admin         | admin / (no password) | Default for some Huawei devices                 |
| **JBoss (WildFly default)**       | admin         | admin                 | WildFly default admin credentials               |
| **Jenkins (Docker image)**        | admin         | admin                 | Default for Jenkins Docker containers           |
| **Juniper Networks**              | root          | (no password)         | Root user with no password by default           |
| **Kali Linux (2020 and newer)**   | kali          | kali                  | Default for newer versions of Kali Linux        |
| **Kali Linux (2020 and older)**   | root          | toor                  | Default for older versions of Kali Linux        |
| **Linksys Routers**               | admin         | admin                 | Standard default for many Linksys models        |
| **MikroTik RouterOS**             | admin         | (no password)         | No password by default on MikroTik devices      |
| **MongoDB (default install)**     | (no username) | (no password)         | No password by default, requires manual config  |
| **MySQL**                         | root          | (empty)               | No password set by default on installation      |
| **Nagios (initial install)**      | nagiosadmin   | nagios                | Default for Nagios web UI                       |
| **Netgear Routers**               | admin         | password              | Popular default for home Netgear routers        |
| **Nvidia Jetson (Developer Kit)** | nvidia        | nvidia                | Default for Nvidia Jetson Developer Kits        |
| **OpenVPN Access Server**         | openvpn       | openvpn               | Default admin account for OpenVPN AS            |
| **OpenWrt (default image)**       | root          | (no password)         | No password by default on OpenWrt               |
| **Oracle Database**               | system        | manager               | Common default for Oracle DB installations      |
| **Palo Alto Firewalls**           | admin         | admin                 | Default for Palo Alto Networks firewalls        |
| **phpMyAdmin**                    | admin         | (no password)         | No password by default for phpMyAdmin           |
| **PostgreSQL (initial install)**  | postgres      | (no password)         | No password by default                          |
| **Prometheus (no login)**         | N/A           | N/A                   | Prometheus has no default login interface       |
| **QNAP NAS**                      | admin         | admin                 | Default on QNAP NAS systems                     |
| **Raspberry Pi (Raspbian)**       | pi            | raspberry             | Default for Raspbian OS on Raspberry Pi         |
| **Redis (older versions)**        | (no username) | (empty)               | No password by default, needs manual config     |
| **Redis**                         | (no username) | (no password)         | Default config has no password                  |
| **RHEL (cloud instances)**        | ec2-user      | (no password)         | No password, uses SSH keys for access           |
| **Samsung Smart TV**              | admin         | 00000000              | Default for some Samsung smart TVs              |
| **SonicWall Firewall**            | admin         | password              | Default for SonicWall devices                   |
| **SonarQube**                     | admin         | admin                 | Default credentials for SonarQube web interface |
| **Sonatype Nexus**                | admin         | admin123              | Default login for Nexus Repository Manager      |
| **Supermicro IPMI**               | ADMIN         | ADMIN                 | Default for Supermicro IPMI systems             |
| **Synology NAS**                  | admin         | admin                 | Default for older Synology NAS devices          |
| **TP-Link Routers**               | admin         | admin                 | Common for TP-Link products                     |
| **Tomcat (default web manager)**  | admin         | admin                 | Default Tomcat manager credentials              |
| **TrendNet Routers**              | admin         | admin                 | Default for TrendNet routers                    |
| **Ubiquiti UniFi**                | ubnt          | ubnt                  | Default for UniFi access points                 |
| **Ubuntu (cloud instances)**      | ubuntu        | (no password)         | Default for cloud images, uses SSH keys         |
| **Vagrant Boxes (default user)**  | vagrant       | vagrant               | Default user/password for many Vagrant boxes    |
| **WordPress (first login)**       | admin         | admin                 | Default for some WordPress quick installs       |
| **XAMPP (MySQL / phpMyAdmin)**    | root          | (no password)         | No password set for MySQL in XAMPP              |
| **Xerox Printers**                | admin         | 1111                  | Default for Xerox multifunction printers        |
| **Yealink IP Phones**             | admin         | admin                 | Default for Yealink VoIP phones                 |
| **Zabbix**                        | Admin         | zabbix                | Default admin credentials for Zabbix monitoring |
| **Zoom Room Controllers**         | admin         | 1234                  | Default for Zoom Room controllers               |
