# Kubernetes

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

kubectl controls the Kubernetes cluster manager

- Docs: <https://kubernetes.io/docs/reference/kubectl/kubectl/>
- Cheatsheet: <https://kubernetes.io/docs/reference/kubectl/cheatsheet/>
- AKS: <https://docs.microsoft.com/en-us/azure/aks/>
- AKS Concepts: <https://docs.microsoft.com/en-us/azure/aks/concepts-clusters-workloads>

## kubectl

Some basics to get information:

``` sh
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

Delete all evicted pods:

``` sh
kubectl get pod -n mynamespace | grep Evicted | awk '{print $1}' | xargs kubectl delete pod -n mynamespace
```

### Port forwarding

Simple example:

``` sh
kubectl port-forward mycontainer 8080:3000
```

Retrieve information about resources in the cluster

- List all pods: ```kubectl get pods```
- ist all deployments ```kubectl get deployments```
- List all services ```kubectl get services```
- List all nodes in the cluster ```kubectl get nodes```

Provide detailed information about a specific resource

- Get pod details ```kubectl describe pod <pod-name>```
- Get deployment details ```kubectl describe deployment <deployment-name>```
- Get service details ```kubectl describe service <service-name>```

Create a resource from a YAML or JSON file

- Create a resource from a YAML file ```kubectl create -f <filename.yaml>```
- Create a deployment using a specified image ```kubectl create deployment <deployment-name> --image=<image-name>```

Delete a resource

- Delete a pod ```kubectl delete pod <pod-name>```
- Delete a deployment ```kubectl delete deployment <deployment-name>```
- Delete a service ```kubectl delete service <service-name>```

Other

- Scale deployment replicas ```kubectl scale deployment <deployment-name> --replicas=<number>```
- Print pod logs ```kubectl logs <pod-name>```
- Execute a command on a pod ```kubectl exec -it <pod-name> -- <command>```
- Apply changes to a resource using a YAML file ```kubectl apply -f <filename.yaml>```

## Kubernetes Dashboard

Running Docker for Windows with enabled Kubernetes Cluster

Deploy Kubernetes Dashboard: ```kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.4.0/aio/deploy/recommended.yaml```
Verify that it's running: ```kubectl get -f .\recommended.yaml.txt```

Get token:

- PowerShell: ``` ((kubectl -n kube-system describe secret default | Select-String "token:") -split " +")[1]```
- Linux: ```kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | awk '/^deployment-controller-token-/{print $1}') | awk '$1=="token:"{print $2}'```

- Run ```kubectl proxy``` and open: <http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/> then select Token & paste the generated token and sign in

Create a user:

<https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md>

- Create a Cluster Admin service account: ```kubectl create serviceaccount dashboard -n default```
- Add the cluster binding rules to your dashboard account: ```kubectl create clusterrolebinding dashboard-admin -n default --clusterrole=cluster-admin --serviceaccount=default:dashboard```
- Get the secret token with this command: ```kubectl get secret $(kubectl get serviceaccount dashboard -o jsonpath="{.secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode```
- Choose token authentication in the Kubernetes dashboard login page.

https://docs.docker.com/get-started/kube-deploy/

## Azure Kubernetes Service (AKS)

Login

```az
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
az acr login --name myAKSCluster
docker login myAKSCluster.azurecr.io
```

Nodepools

```az
az aks nodepool list --cluster-name MyManagedCluster -g MyResourceGroup -o table```
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-vm-size=Standard_XX --mode User
```

Pods and namespaces

```az
kubectl get nodes
kubectl describe node your-node
kubectl get namespaces
kubectl get pods -o wide --all-namespaces
kubectl config set-context --current --namespace=your-namespace
```

### Other Kubernetes Tools

- Lens (Kubernetes IDE): <https://github.com/lensapp/lens>
- <https://learnk8s.io/troubleshooting-deployments>

## More tools

- <https://github.com/portainer/portainer>
- <https://github.com/opsgenie/kubernetes-event-exporter>
