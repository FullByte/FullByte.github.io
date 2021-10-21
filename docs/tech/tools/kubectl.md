# Kubectl

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

kubectl controls the Kubernetes cluster manager

- Docs: <https://kubernetes.io/docs/reference/kubectl/kubectl/>
- Cheatsheet: <https://kubernetes.io/docs/reference/kubectl/cheatsheet/>
- AKS: <https://docs.microsoft.com/en-us/azure/aks/>
- AKS Concepts: <https://docs.microsoft.com/en-us/azure/aks/concepts-clusters-workloads>

## Basics

Some basics to get information:

```shell
kubectl get nodes
kubectl describe node <your-node>
kubectl get namespaces
kubectl get pods -o wide --all-namespaces
```

- Set contect to namespace: ```kubectl config set-context --current --namespace=<your-namespace>```
- Dump pod logs, with label name=myLabel (stdout): ```kubectl logs -l name=myLabel -c my-container```
- Restart Rollout (and pull container image if imagePullPolicy: Always): ```kubectl rollout restart deployment/frontend```
- Auto scale a deployment "foo": ```kubectl autoscale deployment foo --cpu-percent=20 --min=1 --max=10```
- Delete Nodepool: ```az aks nodepool delete -n OldNodePool --cluster-name MyManagedCluster -g MyResourceGroup```

## Azure Kubernetes Service (AKS)

- Login: ```az aks get-credentials --resource-group <myResourceGroup> --name <myAKSCluster>```
- List Nodepools: ```az aks nodepool list --cluster-name MyManagedCluster -g MyResourceGroup -o table```
- Add Nodepool: ```az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-vm-size=Standard_XX --mode User```

## Other Kubernetes Tools

- Lens (Kubernetes IDE): <https://github.com/lensapp/lens>
- <https://learnk8s.io/troubleshooting-deployments>