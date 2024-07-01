# kubectl get events only for a pod
https://stackoverflow.com/questions/51931113/kubectl-get-events-only-for-a-pod

```
kubectl get event --namespace abc-namespace --field-selector involvedObject.name=my-pod-zl6m6
```

