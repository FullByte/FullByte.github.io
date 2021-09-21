# Azure Powershell

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

## Test AZ Module (Azure)

Best way to test if the AZ-Module is installed and to get started login to your Azure Tenant with this command:
If your Azure powershell commands don't work check the following:

- You are not logged in.

```ps1
Connect-AzAccount
Get-AzContext
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

## VM-Stuff

Encrypt VM

```ps1
Function EncryptVM($KeyVault,$KeyName,$VM){
    $kv = Get-azKeyVault -VaultName $KeyVault
    $key = get-Azkeyvaultkey -Name $KeyName -VaultName $KeyVault
    Set-AzVmDiskEncryptionExtension -ResourceGroupName $kv.ResourceGroupName -DiskEncryptionKeyVaultId  $kv.ResourceID -DiskEncryptionKeyVaultUrl $kv.VaultURI -VMName $VM -KeyEncryptionKeyVaultId $kv.ResourceID -KeyEncryptionKeyUrl $key.id -SkipVmBackup -VolumeType "All"
}
```
