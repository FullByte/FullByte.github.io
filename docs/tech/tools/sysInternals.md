# Sysinternals

Download Microsoft Sysinternals: <https://docs.microsoft.com/sysinternals/>

## PsExec

Add User to log on remotely:
LocalUser = evtl. ein service account z.B. für updates/monitoring/…
Server = name des Zielservers

```powershell
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net user testuser2 Passw0rd1 /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Administrators" testuser /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Remote Desktop Users" testuser /add
```

## Sysinternals live

Run sysinternals tools from the explorer

```powershell
\\live.sysinternals.com\tools\procexp.exe
```

Or zoom ...

```powershell
\\live.sysinternals.com\tools\ZoomIt.exe
```

You get the idea :)
