# Sysinternals

[Sysinternals Suite](https://www.microsoft.com/en-us/p/sysinternals-suite/9p7knl5rwt25#activetab=pivot:overviewtab) is a bundle of the Sysinternals utilities including Process Explorer, Process Monitor, Sysmon, Autoruns, ProcDump, all of the PsTools, and many more.

| What          | Where                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------|
| Download      | <https://docs.microsoft.com/sysinternals/>                                                      |
| Install       | <https://www.microsoft.com/en-us/p/sysinternals-suite/9p7knl5rwt25#activetab=pivot:overviewtab> |

## PsExec

Add User to log on remotely:
LocalUser = evtl. ein service account z.B. für updates/monitoring/…
Server = name des Zielservers

``` ps1
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net user testuser2 Passw0rd1 /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Administrators" testuser /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Remote Desktop Users" testuser /add
```

## sigcheck

Trigger the script as follows:

```ps1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Tools\SigCheck\SigCheck.ps1" "%1"
```

The script

``` ps1
param (
    [Parameter(Mandatory = $true)]
    [string]$Target
)

$Sigcheck = "\\live.sysinternals.com\tools\sigcheck.exe"

if (-not (Test-Path $Sigcheck)) {
    Write-Output "ROT: sigcheck.exe (Live) nicht erreichbar"
    exit 2
}

$result = & $Sigcheck -vr -vt -nobanner -h $Target 2>&1

if (-not $result) {
    Write-Output "ROT: Keine Ausgabe von sigcheck"
    exit 2
}

$text = $result -join "`n"

if ($text -match "Unsigned" -or
    $text -match "No signature" -or
    $text -match "Invalid signature") {

    Write-Output "ROT: Unsigned oder ungültige Signatur"
    exit 2
}

if ($text -match "VirusTotal:\s+[1-9][0-9]*") {
    Write-Output "GELB: Signiert, aber VirusTotal-Treffer vorhanden"
    exit 1
}

if ($text -match "Verified:\s+Signed") {
    Write-Output "GRÜN: Signatur gültig, keine Auffälligkeiten"
    exit 0
}

Write-Output "GELB: Unklarer Status – manuelle Prüfung empfohlen"
exit 1
```

## Sysinternals live

Sysinternals live content as network drive:

``` ps1
net use T: \\live.sysinternals.com\tools
```

Remove it with

``` ps1
net use T: /delete
```

Run sysinternals tools from the explorer

``` ps1
\\live.sysinternals.com\tools\procexp.exe -nobanner
```

Or zoom ...

``` ps1
\\live.sysinternals.com\tools\ZoomIt.exe -nobanner
```
