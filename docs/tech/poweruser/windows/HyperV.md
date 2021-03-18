# HyperV

## Install and config

Install Hyper V Feature

```powershell
Install-WindowsFeature -Name Hyper-V -ComputerName localhost -IncludeManagementTools -Restart
```

Check Hyper V Installation

```powershell
Get-WindowsFeature -Name Hyper-V -ComputerName HOSTNAME
```

Reconfigure the service

```shell
sc config vmms start=auto  
```

Stop and start the service

```shell
sc stop vmms
sc start vmms
```

Remove VM

```powershell
Remove-VM -Name "Linux" -Force
```

## Helper

Get VHD owner

```powershell
param ($HyperVNodes,$VHDName)

Foreach ($HyperVNode in $HyperVNodes)
{
	$VMs = Get-WmiObject -Namespace "root\virtualization" -ComputerName $HyperVNode -class Msvm_ComputerSystem | where {$_.Caption -match "Virtual Machine"}
	Foreach ($VM in $VMs)
	{
		$VMSettingData = Get-WmiObject -Namespace "root\virtualization" -ComputerName $HyperVNode `
		-Query "Associators of {$VM} Where ResultClass=Msvm_VirtualSystemSettingData AssocClass=Msvm_SettingsDefineState" 
		$VirtualDiskResource = Get-WmiObject -Namespace "root\virtualization" -ComputerName $HyperVNode `
		-Query "Associators of {$VMSettingData} Where ResultClass=Msvm_ResourceAllocationSettingData AssocClass=Msvm_VirtualSystemSettingDataComponent" | `
		Where-Object { $_.ResourceSubType -match "Microsoft Virtual Hard Disk" }
		$VHDPath = $null
		Foreach ($VHD in $VirtualDiskResource)
		{
			$VHDPath = $VHDPath + $VHD.Connection[0] + ","
		}
		if ($VHDPath -Match $VHDName)
		{
			Write-Host "The VM named $($VM.ElementName) is connected to the VHD $VHDName"
		}
	}
}
```
