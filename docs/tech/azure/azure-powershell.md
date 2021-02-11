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

```powershell
Connect-AzAccount
Get-AzContext
```

### Resource Providers

Make sure all resource providers required are activated/registered:
Source: <https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types>

```powershell
Get-AzureRmResourceProvider -ListAvailable | where {$_.RegistrationState -eq "Registered"} | Select ProviderNamespace, RegistrationState
```

To register a specific resource provider run the following Powershell command:

```powershell
Register-AzureRmResourceProvider -ProviderNamespace ResourceProvider.Name
```
