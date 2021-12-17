# Bicep

Bicep is a domain-specific language (DSL) that uses declarative syntax to deploy Azure resources.

- Docs: <https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview>
- Source: <https://github.com/Azure/bicep>
- Install: ```choco install -y bicep```

## From ARM to Bicep

You can export the template for a resource group, and then pass it directly to the decompile command. The following example shows how to decompile an exported template.

``` ps11
Export-AzResourceGroup -ResourceGroupName "rg-your_resource_group_name" -Path ./my-arm-file.json
```

You can now use this "my-arm-file.json" ARM template and convert it to a dicep file:

``` ps11
az bicep decompile --file .\my-arm-file.json
```

## Resource Naming

Naming conventions are important. Don't make them too complicated so you can easily follow them and note that there are maximum lenths for certain ressources and some also need to be unique. For this reason respect [name length](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules) and use [unique string](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-functions-string#uniquestring) function as a suffix.

You can change "yourPrefix" to whatever you want e.g. a resource prefix "vm-" and some vmname "webserver". This will then be followed by a random string that is cut off once the naming limit is reached:

```json
"variables": {
    "Name": "[toLower(substring(concat(parameters('yourPrefix'),uniqueString(resourceGroup().id)),0,14))]",
```

## Examples

### Storage

- Create RG: ```az group create --name exampleRG --location westeurope```
- Run main.bicep file to create strage account: ```az deployment group create --resource-group exampleRG --template-file main.bicep --parameters storageName=mystorageaccount666666666```
- Create fileshare: ```az storage fs create -n my-file-system --account-name mystorageaccount --auth-mode login```
- Create directory ```az storage fs directory create -n my-directory -f my-file-system --account-name mystorageaccount --auth-mode login```
- Upload file ```az storage fs file upload -s "C:\\myFolder\\upload.txt" -p my-directory/upload.txt  -f my-file-system --account-name mystorageaccount --auth-mode login```
- Download file: ```az storage fs file download -p my-directory/upload.txt -f my-file-system -d "C:\\myFolder\\download.txt" --account-name mystorageaccount --auth-mode login```
