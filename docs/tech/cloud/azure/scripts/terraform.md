
# Terraform

Docs for Azure: <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs>

## Azure prep

``` ps1
az account set --subscription="add-id"
az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/add-id"
```

## Terraform basic commands

Create a terraform file called `main.tf` (optional `outputs.tf` and `variables.tf`)

- Run init: ```terraform init```

Check main.tf:

- Check format: ```terraform fmt```
- Validate configuration: ```terraform validate```

Apply changes/get status:

- Run script (whenever changes are made that should be deployed): ```terraform apply```
- Show state: ```terraform show```
- Show state list: ```terraform state list```

Delete resources:

- remove resources: ```terraform destroy```
