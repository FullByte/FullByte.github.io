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

## Kubernetes Dashboard

Running Docker for Windows with enabled Kubernetes Cluster

Deploy Kubernetes Dashboard: ```kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.4.0/aio/deploy/recommended.yaml```
Verify that it's running: ```kubectl get -f .\recommended.yaml.txt```

Get token:
- Run powershell ``` ((kubectl -n kube-system describe secret default | Select-String "token:") -split " +")[1]```
- Or on linux: ```kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | awk '/^deployment-controller-token-/{print $1}') | awk '$1=="token:"{print $2}'```

- Run ```kubectl proxy``` and open: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/ then select Token & paste the generated token and sign in

Create a user:

https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md

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
