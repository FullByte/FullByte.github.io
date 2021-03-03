# Sysinternals

Download Microsoft Sysinternals: <https://docs.microsoft.com/en-us/sysinternals/>

## PsExec

Add User to log on remotely:
LocalUser = evtl. ein service account z.B. für updates/monitoring/…
Server = name des Zielservers

PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net user testuser2 Passw0rd1 /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Administrators" testuser /add
PsExec.exe \\Server -u "Server\\LocalUser" -p "LocalUserPW" net localgroup "Remote Desktop Users" testuser /add
