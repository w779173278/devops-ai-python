## kubectl

kubectl 控制 Kubernetes 集群管理器

### Synopsis

kubectl controls the Kubernetes cluster manager.

 Find more information at: https://kubernetes.io/docs/reference/kubectl/

```
kubectl [flags]
```

### Options

```
      --as string                      Username to impersonate for the operation. User could be a regular user or a service account in a namespace.
      --as-group stringArray           Group to impersonate for the operation, this flag can be repeated to specify multiple groups.
      --as-uid string                  UID to impersonate for the operation.
      --as-user-extra stringArray      User extras to impersonate for the operation, this flag can be repeated to specify multiple values for the same key.
      --cache-dir string               Default cache directory (default "/Users/weishengdong/.kube/cache")
      --certificate-authority string   Path to a cert file for the certificate authority
      --client-certificate string      Path to a client certificate file for TLS
      --client-key string              Path to a client key file for TLS
      --cluster string                 The name of the kubeconfig cluster to use
      --context string                 The name of the kubeconfig context to use
      --disable-compression            If true, opt-out of response compression for all requests to the server
  -h, --help                           help for kubectl
      --insecure-skip-tls-verify       If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure
      --kubeconfig string              Path to the kubeconfig file to use for CLI requests.
      --kuberc string                  Path to the kuberc file to use for preferences. This can be disabled by exporting KUBECTL_KUBERC=false feature gate or turning off the feature KUBERC=off.
      --match-server-version           Require server version to match client version
  -n, --namespace string               If present, the namespace scope for this CLI request
      --password string                Password for basic authentication to the API server
      --profile string                 Name of profile to capture. One of (none|cpu|heap|goroutine|threadcreate|block|mutex|trace) (default "none")
      --profile-output string          Name of the file to write the profile to (default "profile.pprof")
      --request-timeout string         The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests. (default "0")
  -s, --server string                  The address and port of the Kubernetes API server
      --tls-server-name string         Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used
      --token string                   Bearer token for authentication to the API server
      --user string                    The name of the kubeconfig user to use
      --username string                Username for basic authentication to the API server
      --warnings-as-errors             Treat warnings received from the server as errors and exit with a non-zero exit code
```

### SEE ALSO

* [kubectl alpha](kubectl_alpha.md)	 - Commands for features in alpha
* [kubectl annotate](kubectl_annotate.md)	 - 更新一个资源的注解
* [kubectl api-resources](kubectl_api-resources.md)	 - Print the supported API resources on the server
* [kubectl api-versions](kubectl_api-versions.md)	 - Print the supported API versions on the server, in the form of "group/version"
* [kubectl apply](kubectl_apply.md)	 - Apply a configuration to a resource by file name or stdin
* [kubectl attach](kubectl_attach.md)	 - 挂接到一个运行中的容器
* [kubectl auth](kubectl_auth.md)	 - Inspect authorization
* [kubectl autoscale](kubectl_autoscale.md)	 - Auto-scale a deployment, replica set, stateful set, or replication controller
* [kubectl certificate](kubectl_certificate.md)	 - Modify certificate resources
* [kubectl cluster-info](kubectl_cluster-info.md)	 - Display cluster information
* [kubectl completion](kubectl_completion.md)	 - Output shell completion code for the specified shell (bash, zsh, fish, or powershell)
* [kubectl config](kubectl_config.md)	 - 修改 kubeconfig 文件
* [kubectl cordon](kubectl_cordon.md)	 - 标记节点为不可调度
* [kubectl cp](kubectl_cp.md)	 - Copy files and directories to and from containers
* [kubectl create](kubectl_create.md)	 - Create a resource from a file or from stdin
* [kubectl debug](kubectl_debug.md)	 - Create debugging sessions for troubleshooting workloads and nodes
* [kubectl delete](kubectl_delete.md)	 - Delete resources by file names, stdin, resources and names, or by resources and label selector
* [kubectl describe](kubectl_describe.md)	 - 显示特定资源或资源组的详细信息
* [kubectl diff](kubectl_diff.md)	 - Diff the live version against a would-be applied version
* [kubectl drain](kubectl_drain.md)	 - 清空节点以准备维护
* [kubectl edit](kubectl_edit.md)	 - 编辑服务器上的资源
* [kubectl events](kubectl_events.md)	 - List events
* [kubectl exec](kubectl_exec.md)	 - 在某个容器中执行一个命令
* [kubectl explain](kubectl_explain.md)	 - Get documentation for a resource
* [kubectl expose](kubectl_expose.md)	 - Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
* [kubectl get](kubectl_get.md)	 - 显示一个或多个资源
* [kubectl kustomize](kubectl_kustomize.md)	 - Build a kustomization target from a directory or URL
* [kubectl label](kubectl_label.md)	 - 更新某资源上的标签
* [kubectl logs](kubectl_logs.md)	 - 打印 Pod 中容器的日志
* [kubectl options](kubectl_options.md)	 - 输出所有命令的层级关系
* [kubectl patch](kubectl_patch.md)	 - Update fields of a resource
* [kubectl plugin](kubectl_plugin.md)	 - Provides utilities for interacting with plugins
* [kubectl port-forward](kubectl_port-forward.md)	 - 将一个或多个本地端口转发到某个 Pod
* [kubectl proxy](kubectl_proxy.md)	 - 运行一个指向 Kubernetes API 服务器的代理
* [kubectl replace](kubectl_replace.md)	 - Replace a resource by file name or stdin
* [kubectl rollout](kubectl_rollout.md)	 - Manage the rollout of a resource
* [kubectl run](kubectl_run.md)	 - 在集群上运行特定镜像
* [kubectl scale](kubectl_scale.md)	 - Set a new size for a deployment, replica set, or replication controller
* [kubectl set](kubectl_set.md)	 - 为对象设置指定特性
* [kubectl taint](kubectl_taint.md)	 - 更新一个或者多个节点上的污点
* [kubectl top](kubectl_top.md)	 - Display resource (CPU/memory) usage
* [kubectl uncordon](kubectl_uncordon.md)	 - 标记节点为可调度
* [kubectl version](kubectl_version.md)	 - 输出客户端和服务端的版本信息
* [kubectl wait](kubectl_wait.md)	 - Wait for a specific condition on one or many resources

