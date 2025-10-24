# kubectl get events only for a pod
https://stackoverflow.com/questions/51931113/kubectl-get-events-only-for-a-pod

```
kubectl get event --namespace abc-namespace --field-selector involvedObject.name=my-pod-zl6m6
```



## Kubernetes API - Get Pods on Specific Nodes

```
kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=<node>
```


## How to copy files from Kubernetes Pods to local system
https://stackoverflow.com/questions/52407277/how-to-copy-files-from-kubernetes-pods-to-local-system

```
kubectl cp --help
Copy files and directories to and from containers.
Examples:
# !!!Important Note!!!
# Requires that the 'tar' binary is present in your container
# image.  If 'tar' is not present, 'kubectl cp' will fail.

# Copy /tmp/foo_dir local directory to /tmp/bar_dir in a remote pod in the default namespace
kubectl cp /tmp/foo_dir <some-pod>:/tmp/bar_dir

# Copy /tmp/foo local file to /tmp/bar in a remote pod in a specific container
kubectl cp /tmp/foo <some-pod>:/tmp/bar -c <specific-container>

# Copy /tmp/foo local file to /tmp/bar in a remote pod in namespace <some-namespace>
kubectl cp /tmp/foo <some-namespace>/<some-pod>:/tmp/bar

# Copy /tmp/foo from a remote pod to /tmp/bar locally
kubectl cp <some-namespace>/<some-pod>:/tmp/foo /tmp/bar

Options:
-c, --container='': Container name. If omitted, the first container in the pod will be chosen

Usage:
kubectl cp <file-spec-src> <file-spec-dest> [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
```