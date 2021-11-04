# Azure Powershell

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

## Login

Login to azure:

```ps1
Connect-AzAccount
Get-AzContext
```

Use device code to login:

```powershell
Connect-AzAccount -Tenant <tenantID> -UseDeviceAuthentication
```

## Useful Information

Images

```ps1
Get-AzImage -ResourceGroupName 'ResourceGroup01' -ImageName 'Image01'
```


## Helpers

One-liner to get any tenant ID without being logged in:

```ps1
if(($result = Read-Host "Enter a tenant name you want the tenant ID of: ") -eq ''){"You need to add a tenant name"}else{Write-Host('TenantID: ' + (Invoke-WebRequest https://login.windows.net/$result.onmicrosoft.com/.well-known/openid-configuration|ConvertFrom-Json).token_endpoint.Split('/')[3])}
```

You can't rename a resource group but you can [move it](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription):

```ps1
Get-AzureRmResource -ResourceGroupName <sourceResourceGroupName> | Move-AzureRmResource -DestinationResourceGroupName <destResourceGroupName>
```

### Resource Providers

Make sure all resource providers required are activated/registered:
Source: <https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types>

```ps1
Get-AzureRmResourceProvider -ListAvailable | where {$_.RegistrationState -eq "Registered"} | Select ProviderNamespace, RegistrationState
```

To register a specific resource provider run the following Powershell command:

```ps1
Register-AzureRmResourceProvider -ProviderNamespace ResourceProvider.Name
```

## Virtual Machine (VM)

### [Encrypt VM](https://docs.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)

List all VMs and if they are using Azure Disk Encryption (but not the extension version):

```ps1
$osVolEncrypted = {(Get-AzVMDiskEncryptionStatus -ResourceGroupName $_.ResourceGroupName -VMName $_.Name).OsVolumeEncrypted}
$dataVolEncrypted= {(Get-AzVMDiskEncryptionStatus -ResourceGroupName $_.ResourceGroupName -VMName $_.Name).DataVolumesEncrypted}
Get-AzVm | Format-Table @{Label="MachineName"; Expression={$_.Name}}, @{Label="OsVolumeEncrypted"; Expression=$osVolEncrypted}, @{Label="DataVolumesEncrypted"; Expression=$dataVolEncrypted}
```

[Encrypt a VM](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/disk-encryption-sample-scripts)

Short example

```ps1
Function EncryptVM($KeyVault,$KeyName,$VM){
    $kv = Get-azKeyVault -VaultName $KeyVault
    $key = get-Azkeyvaultkey -Name $KeyName -VaultName $KeyVault
    Set-AzVmDiskEncryptionExtension -ResourceGroupName $kv.ResourceGroupName -DiskEncryptionKeyVaultId  $kv.ResourceID -DiskEncryptionKeyVaultUrl $kv.VaultURI -VMName $VM -KeyEncryptionKeyVaultId $kv.ResourceID -KeyEncryptionKeyUrl $key.id -SkipVmBackup -VolumeType "All"
}
```

Full script

```ps1
$keyVaultName = "kvVMencyption"
$resourceGroupName = "rg-VM-encyption"
$keyEncryptionKeyName = "VMencyptionKey"
$location = "westeurope"

Write-Host "Creating new resource group: ($resourceGroupName)";
$resGroup = Get-AzResourceGroup -Name $resourceGroupName -ErrorAction SilentlyContinue;
if (-not $resGroup) { $resGroup = New-AzResourceGroup -Name $resourceGroupName -Location $location; }

Write-Host "Creating a new KeyVault named $keyVaultName to store encryption keys";
$keyVault = Get-AzKeyVault -VaultName $keyVaultName -ErrorAction SilentlyContinue;
if (-not $keyVault) { $keyVault = New-AzKeyVault -VaultName $keyVaultName -ResourceGroupName $resourceGroupName -Sku Standard -Location $location; }

Set-AzKeyVaultAccessPolicy -VaultName $keyVaultName -EnabledForDiskEncryption;

Write-Host "Enabling Soft Delete on KeyVault $keyVaultName";
$resource = Get-AzResource -ResourceId $keyVault.ResourceId;
$resource.Properties | Add-Member -MemberType "NoteProperty" -Name "enableSoftDelete" -Value "true" -Force;
Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties -Force;

Write-Host "Adding resource lock on  KeyVault $keyVaultName";
$lockNotes = "KeyVault may contain AzureDiskEncryption secrets required to boot encrypted VMs";
New-AzResourceLock -LockLevel CanNotDelete -LockName "LockKeyVault" -ResourceName $resource.Name -ResourceType $resource.ResourceType -ResourceGroupName $resource.ResourceGroupName -LockNotes $lockNotes -Force;

Write-Host "Creating key encryption key named:$keyEncryptionKeyName in Key Vault: $keyVaultName";
$kek = Add-AzKeyVaultKey -VaultName $keyVaultName -Name $keyEncryptionKeyName -Destination Software -ErrorAction SilentlyContinue;
$keyEncryptionKeyUrl = $kek.Key.Kid;

foreach($vm in Get-AzVm)
{
    if($vm.Location.replace(' ','').ToLower() -ne $keyVault.Location.replace(' ','').ToLower())
    {
        Write-Error "To enable AzureDiskEncryption, VM and KeyVault must belong to same subscription and same region. vm Location:  $($vm.Location.ToLower()) , keyVault Location: $($keyVault.Location.ToLower())";
        return;
    }

    Write-Host "Encrypting VM: $($vm.Name) in ResourceGroup: $($vm.ResourceGroupName) " -foregroundcolor Green;
    Set-AzVMDiskEncryptionExtension -ResourceGroupName $vm.ResourceGroupName -VMName $vm.Name -DiskEncryptionKeyVaultUrl $diskEncryptionKeyVaultUrl -DiskEncryptionKeyVaultId $keyVaultResourceId -KeyEncryptionKeyUrl $keyEncryptionKeyUrl -KeyEncryptionKeyVaultId $keyVaultResourceId -VolumeType 'All';

    Get-AzVmDiskEncryptionStatus -ResourceGroupName $vm.ResourceGroupName -VMName $vm.Name;
}
```
