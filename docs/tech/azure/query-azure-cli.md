# Query Azure CLI

Docs: <https://docs.microsoft.com/de-de/cli/azure/query-azure-cli>

## Query VM

Get public key from given Linux VM:

``` ps11
az vm show -g resourcegroup -n LinuxVM --query osProfile.linuxConfiguration.ssh.publicKeys -o json

[
  {
    "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAAD...a8EufjquNi1p9 fab1@fab1",
    "path": "/home/fab1/.ssh/authorized_keys"
  }
]
```

If you only want the keyData you need to be more specific with your request e.g.:

``` ps11
az vm show -g resourcegroup -n LinuxVM --query 'osProfile.linuxConfiguration.ssh.publicKeys[0].keyData' -o json

"ssh-rsa AAAAB3NzaC1yc2EAAAAD...a8EufjquNi1p9 fab1@fab1"
```

## Query Resource Graph

Get my subscriptions (e.g. a good way to get the quotaId)

``` ps11
az graph query -q 'resourcecontainers | where type == "microsoft.resources/subscriptions" | where properties.state != "Disabled" | project subscriptionId, name, properties.subscriptionPolicies.quotaId'
```
