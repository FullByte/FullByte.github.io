# Kali

## Update

```shell
sudo wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add # Get latest key
sudo dpkg --configure -a
sudo apt update && apt -y full-upgrade && apt -y autoremove
```

## WSL with GUI and seamless mode

**Set WSL version 2**

```powershell
(New-Object System.Net.WebClient).DownloadFile("https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi", "wsl_update_x64.msi") 
Start-Process msiexec.exe -Wait -ArgumentList '/I wsl_update_x64.msi /quiet' 
wsl --set-version kali-linux 2
```

**Update Kali**

```bash
sudo apt update
sudo apt install -y kali-linux-large
sudo apt install -y kali-win-kex
kex start
kex --esm --sound
```

**Add option in windows terminal**

Basic Win-KeX in seamless mode with sound:
```json
{
      "guid": "{55ca431a-3a87-5fb3-83cd-11ececc031d2}",
      "hidden": false,
      "name": "Win-KeX",
      "commandline": "wsl -d kali-linux kex --esm --sound"
}
```
