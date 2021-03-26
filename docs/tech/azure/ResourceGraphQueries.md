# Resource Graph Queries

Get my subscriptions (e.g. a good way to get the quotaId)

```powershell
az graph query -q 'resourcecontainers | where type == "microsoft.resources/subscriptions" | where properties.state != "Disabled" | project subscriptionId, name, properties.subscriptionPolicies.quotaId'
```
