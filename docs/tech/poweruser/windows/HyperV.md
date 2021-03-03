# HyperV

Install Hyper V Feature

```powershell
Install-WindowsFeature -Name Hyper-V -ComputerName localhost -IncludeManagementTools -Restart
```

Check Hyper V Installation

```powershell
Get-WindowsFeature -Name Hyper-V -ComputerName HOSTNAME
```

reconfigure the service

```shell
sc config vmms start=auto  
```

stop and start the service

```shell
sc stop vmms
sc start vmms
```

Remove VM

```powershell
Remove-VM -Name "Linux" -Force
```
