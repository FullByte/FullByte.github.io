# Azure CLI

## Login

Use device code to login:

```bash
az login --tenant <tenantID> --use-device-code
```

## Who am I

Login and check the current context

```bash
az login
az account show --output table
az ad signed-in-user show
az group list --output table
az logout
```

## JQ

Use jq to filter for only the results you want.

Example:

```bash
az account list | jq -r '.[].tenantId'
```

## Useful Information

Images

```bash
az vm image list-publishers --location westus
az vm image list-offers --location westus --publisher Canonical
az vm image list-skus --location westus --publisher Canonical --offer UbuntuServer
imageId=$(az sig image-definition show --resource-group images --gallery-name imagegallery --gallery-image-definition ubuntu_standard --query id --output tsv)

az sig image-definition create -g images -r imagegallery --gallery-image-definition MyImage --publisher Me --offer Ubuntu --sku 18.04 --os-type linux
az sig image-definition create -g images -r imagegallery --gallery-image-definition MyImage --publisher Me --offer Windows --sku mysku --os-type windows
```
