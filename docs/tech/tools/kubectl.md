# Kubectl

kubectl controls the Kubernetes cluster manager

- Docs: <https://kubernetes.io/docs/reference/kubectl/kubectl/>
- Cheatsheet: <https://kubernetes.io/docs/reference/kubectl/cheatsheet/>

## Azure Kubernetes Service (AKS)

Dump pod logs, with label name=myLabel (stdout)

```shell
kubectl logs -l name=myLabel -c my-container
```

Restart Rollout (and pull container image if imagePullPolicy: Always)

```shell
kubectl rollout restart deployment/frontend 

Auto scale a deployment "foo"

```shell
kubectl autoscale deployment foo --cpu-percent=20 --min=1 --max=10 
```

List Nodepools

```shell
az aks nodepool list --cluster-name MyManagedCluster -g MyResourceGroup -o table
```

Add Nodepool

```shell
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-vm-size=Standard_XX --mode User
```

Delete Nodepool

```shell
az aks nodepool delete -n OldNodePool --cluster-name MyManagedCluster -g MyResourceGroup
```
