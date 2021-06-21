# Bicep

Bicep is a domain-specific language (DSL) that uses declarative syntax to deploy Azure resources.

- Docs: <https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview>
- Source: <https://github.com/Azure/bicep>
- Install: ```choco install -y bicep```

## From ARM to Bicep

You can export the template for a resource group, and then pass it directly to the decompile command. The following example shows how to decompile an exported template.

```ps1
Export-AzResourceGroup -ResourceGroupName "rg-your_resource_group_name" -Path ./my-arm-file.json
```

You can now use this "my-arm-file.json" ARM template and convert it to a dicep file:

```ps1
az bicep decompile --file .\my-arm-file.json
```

## Resource Naming

Naming conventions are important. Don't make them too complicated so you can easily follow them and note that there are maximum lenths for certain ressources and some also need to be unique. For this reason respect [name length](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules) and use [unique string](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-functions-string#uniquestring) function as a suffix.

You can change "yourPrefix" to whatever you want e.g. a resource prefix "vm-" and some vmname "webserver". This will then be followed by a random string that is cut off once the naming limit is reached:

```json
"variables": {
    "Name": "[toLower(substring(concat(parameters('yourPrefix'),uniqueString(resourceGroup().id)),0,14))]",
```
