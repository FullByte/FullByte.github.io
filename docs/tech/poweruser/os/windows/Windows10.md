# Windows 10

Notes on Windows 10.

## Windows Commands

### Helpful basics

- Umfangreiche Systeminformationen: systeminfo
- Betriebssystemversion: ver
- Aktive Verbindungen: netstat –a
- Standards DNS-Server: nslookup
- Per RPC auf Server: MSTSC server00123 /f
- net user <username> <neuespasswort>
- net localgroup &lt;Gruppe z.B."Remote Desktop Users"> <username> /add
- route print
- Msconfig

### Merge files

#### To hide something

```shell
copy /b secret.jpg + pic1.jpg newpic.jpg
```

#### To merge video files

```shell
copy /b video1.avi + video2.avi video.avi
```

### Netsh

Die Angaben hinter „ssid=“ (Netzname) sowie „key=“ (Kennwort) können Sie frei wählen. Gehen Sie nach Eingabe des zweiten Befehls über die Systemsteuerung auf „Netzwerk- und Freigabecenter -> Adaptereinstellungen ändern“. Dort konfigurieren Sie die Verbindung des Kabel-Netzadapters neu. Klicken Sie mit der rechten Maustaste auf den primären Netzadapter (meist „Ethernet“), und wählen Sie „Eigenschaften“. Auf der Registerkarte „Freigabe“ aktivieren Sie die „Gemeinsame Nutzung der Internetverbindung“. Wählen Sie unter „Freigabe“ per Drop-down-Feld den vorher eingerichteten virtuellen Adapter aus.

```shell
netsh wlan set hostednetwork mode=allow ssid=meinwlan key=meinwlan  netsh wlan start hostednetwork
netsh wlan start hostednetwork
```

Falls der letzte befehl nicht klappt: Das Problem lässt sich meist über den Gerätemanager lösen. Suchen Sie dort nach dem „Microsoft Virtual WiFi Miniport Adapter“ und aktivieren Sie diesen.

#### Versteckte wlans finden

```shell
Netsh wlan show networks mode=bssid
```

### Reply from IP: TTL expired in transit

```shell
ARP -p <IP> <MAC>
```

### Firewall config

```shell
netsh advfirewall show currentprofile
```

### Send Message

Anderen usern auf einem System eine Nachricht schicken:

```shell
net send /users This is a test message
msg \* /SERVER:localhost /TIME:666 /W This is a test message
```

### Get MAC Address of remote PC

Option 1

```shell
net view machinename
nbtstat -a machinename
```

Option 2

```shell
Ping <IP/machinename>
Arp –a
```

Option 3

```shell
getmac
```

### Netzwerkverkehr umleiten

Die Addresse 8.8.8.8 mit der eigenen IP 10.155.84.186 aufrufen:

```shell
route add 8.8.8.8 MASK 255.255.255.255 10.155.84.186
route print
```

### traceroute

pathping (alternative to tracert: https://de.wikipedia.org/wiki/Pathping)

Using ICMP

```shell
traceroute -I www.microsoft.com
```

Using UDP

```shell
traceroute -U www.microsoft.com
```

Using TCP Port 80 (usually allowed by firewalls)

```shell
traceroute -T -p 80 www.microsoft.com
```

### Laufwerk Benchmark

```shell
Winsat disk –write –ran –ransize 262144 –drive f
```

### Symbolic links

```shell
fsutil hardlink create <destination_path> <file_path>
```

## Windows 10 boots in Recovery Mode

**Recovery Deaktivieren**

Problembehandlung -> Eingabeaufforderung -> command:

```cmd
bcdedit /set {current} recoveryenabled No
```

**MBR reparieren**

Problembehandlung -> Eingabeaufforderung -> commands:

```cmd
bootrec.exe /fixmbr
bootrec.exe /fixboot
bootrec.exe /rebuildbcd
```

Sektor bzw. Festplatten reparieren
Problembehandlung -> Eingabeaufforderung -> command:

```cmd
chkdsk /f /r
```

**Windows 10 abgesicherten Modus**

Problembehandlung“, dann „Erweiterte Optionen“, dann „Starteinstellungen“, dann „Neu starten“
Drücke auf „F5-Taste“, um Abgesicherten Modus mit Netzwerktreibern zu aktivieren.
