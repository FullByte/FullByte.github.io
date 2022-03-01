# Sysinternals

Info

| What          | Where                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------|
| Official Page |                                                                                                 |
| Download      | <https://docs.microsoft.com/sysinternals/>                                                      |
| Install       | <https://www.microsoft.com/en-us/p/sysinternals-suite/9p7knl5rwt25#activetab=pivot:overviewtab> |

### PsExec

Add User to log on remotely:
LocalUser = evtl. ein service account z.B. für updates/monitoring/…
Server = name des Zielservers

``` ps1
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net user testuser2 Passw0rd1 /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Administrators" testuser /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Remote Desktop Users" testuser /add
```

### Sysinternals live

Run sysinternals tools from the explorer

``` ps1
\\live.sysinternals.com\tools\procexp.exe
```

Or zoom ...

``` ps1
\\live.sysinternals.com\tools\ZoomIt.exe
```
