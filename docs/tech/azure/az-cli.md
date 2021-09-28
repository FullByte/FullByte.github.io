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
