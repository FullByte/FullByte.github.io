# Windows Store

## File Recovery

Link: <https://www.microsoft.com/en-us/p/windows-file-recovery/9n26s50ln705?activetab=pivot:overviewtab>

TODO

## Windows Terminal

Link: <https://www.microsoft.com/de-de/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab>

Open a new Terminal Window with powershell 7, cmd and WSL (in my case ubuntu)

```powershell
wt -p "PowerShell 7" `; split-pane -p "cmd" `; split-pane -H wsl.exe
```

## WSL

**Set WSL version 2**

```powershell
(New-Object System.Net.WebClient).DownloadFile("https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi", "wsl_update_x64.msi") 
Start-Process msiexec.exe -Wait -ArgumentList '/I wsl_update_x64.msi /quiet' 
wsl --set-version kali-linux 2
```

### Ubuntu 20.04 LTS

Link: <https://www.microsoft.com/de-de/p/ubuntu-2004-lts/9n6svws3rx71?cid=msft_web_chart&activetab=pivot:overviewtab>

### Kali with GUI

```bash
sudo apt update
sudo apt install -y kali-linux-large
sudo apt install -y kali-win-kex
kex start
kex --esm --sound
```
