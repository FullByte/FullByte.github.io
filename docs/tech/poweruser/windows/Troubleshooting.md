# Troubleshooting

Fixing Windows 10 issues

## Get Information

**Get Win10 key**

```powershell
(Get-WmiObject -query ‘select * from SoftwareLicensingService’).OA3xOriginalProductKey
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
