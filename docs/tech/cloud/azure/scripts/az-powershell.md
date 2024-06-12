# Azure Powershell

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Login

If on Linux, start Powershell in bash with `pwsh`.

Login to azure:

``` ps1
Connect-AzAccount
Get-AzContext
```

Use device code to login:

``` ps1
Connect-AzAccount -Tenant <tenantID> -UseDeviceAuthentication
```

## Useful Information

Images

``` ps1
Get-AzImage -ResourceGroupName 'ResourceGroup01' -ImageName 'Image01'
```

## Helpers

Get any tenant ID when providing a name:

``` ps1
if(($result = Read-Host "Enter a tenant name you want the tenant ID of: ") -eq ''){"You need to add a tenant name"}else{Write-Host('TenantID: ' + (Invoke-WebRequest https://login.windows.net/$result.onmicrosoft.com/.well-known/openid-configuration|ConvertFrom-Json).token_endpoint.Split('/')[3])}
```

You can't rename a resource group but you can [move it](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription):

``` ps1
Get-AzureRmResource -ResourceGroupName <sourceResourceGroupName> | Move-AzureRmResource -DestinationResourceGroupName <destResourceGroupName>
```

Powershell GUI (GridView) to (in this example) have the user select the correct storag account:

``` ps1
$storageAccount = Get-AzStorageAccount | Out-GridView -Title "Select StorrageAccount" -OutputMode Single
$storageAccountName = $storageAccount | Select-Object -ExpandProperty StorageAccountName
```

### Resource Providers

Make sure all resource providers required are activated/registered:
Source: <https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types>

``` ps1
Get-AzureRmResourceProvider -ListAvailable | where {$_.RegistrationState -eq "Registered"} | Select ProviderNamespace, RegistrationState
```

To register a specific resource provider run the following Powershell command:

``` ps1
Register-AzureRmResourceProvider -ProviderNamespace ResourceProvider.Name
```

## Snippets

### Find unused Resources

``` ps1
foreach ($subscription in (Get-AzSubscription | Where-Object { $_.State -eq "Enabled" } | Select-Object -expandproperty id)) {
    Set-AzContext -subscriptionId $subscription
    Get-AzPublicIpAddress | Where-Object { $_.ipaddress -eq "Not Assigned" } | Select-Object name, PublicIpAllocationMethod, PublicIpAddressVersion | Format-Table
}
```

### Virtual Machine

#### Encrypt VM

Short example on how to [encrypt a VM](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/disk-encryption-sample-scripts)

``` ps1
Function EncryptVM($KeyVault,$KeyName,$VM){
    $kv = Get-azKeyVault -VaultName $KeyVault
    $key = Get-Azkeyvaultkey -Name $KeyName -VaultName $KeyVault
    Set-AzVmDiskEncryptionExtension -ResourceGroupName $kv.ResourceGroupName -DiskEncryptionKeyVaultId  $kv.ResourceID -DiskEncryptionKeyVaultUrl $kv.VaultURI -VMName $VM -KeyEncryptionKeyVaultId $kv.ResourceID -KeyEncryptionKeyUrl $key.id -SkipVmBackup -VolumeType "All"
}
```

#### Check if VM is encypted

The following script is based on this documentation on [how to verify the encryption status](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/how-to-verify-encryption-status).

``` ps1
foreach ($subscription in (Get-AzSubscription | Where-Object { $_.State -eq "Enabled" } | Select-Object -expandproperty id)) {
    Set-AzContext -subscriptionId $subscription
    foreach ($resourcegroup in (Get-AzResourceGroup | Where-Object { $_.ProvisioningState -eq "succeeded" } | Select-Object -expandproperty resourcegroupname)) {
        foreach ($vm in (Get-AzVM -ResourceGroupName $resourcegroup | Select-Object -expandproperty Name)) {
            Write-Host("# Status on " + $vm + " in RG " + $resourcegroup)
            Get-AzVMDiskEncryptionStatus -ResourceGroupName $resourcegroup -VMName $vm
        }
    }
}
```

Alternative Solution to List all VMs Disk Encryption status:

``` ps1
foreach ($subscription in (Get-AzSubscription | Where-Object { $_.State -eq "Enabled" } | Select-Object -expandproperty id)){
    Set-AzContext -subscriptionId $subscription
    $osVolEncrypted = {(Get-AzVMDiskEncryptionStatus -ResourceGroupName $_.ResourceGroupName -VMName $_.Name).OsVolumeEncrypted}
    $dataVolEncrypted= {(Get-AzVMDiskEncryptionStatus -ResourceGroupName $_.ResourceGroupName -VMName $_.Name).DataVolumesEncrypted}
    Get-AzVm | Format-Table @{Label="MachineName"; Expression={$_.Name}}, @{Label="OsVolumeEncrypted"; Expression=$osVolEncrypted}, @{Label="DataVolumesEncrypted"; Expression=$dataVolEncrypted}
}
```
