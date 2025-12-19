## kubectl config

修改 kubeconfig 文件

### Synopsis

Modify kubeconfig files using subcommands like "kubectl config set current-context my-context".

 The loading order follows these rules:

  1.  If the --kubeconfig flag is set, then only that file is loaded. The flag may only be set once and no merging takes place.
  2.  If $KUBECONFIG environment variable is set, then it is used as a list of paths (normal path delimiting rules for your system). These paths are merged. When a value is modified, it is modified in the file that defines the stanza. When a value is created, it is created in the first file that exists. If no files in the chain exist, then it creates the last file in the list.
  3.  Otherwise, ${HOME}/.kube/config is used and no merging takes place.

```
kubectl config SUBCOMMAND
```

### Options

```
  -h, --help                help for config
      --kubeconfig string   use a particular kubeconfig file
```

### Options inherited from parent commands

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
      --insecure-skip-tls-verify       If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure
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

* [kubectl](kubectl.md)	 - kubectl 控制 Kubernetes 集群管理器
* [kubectl config current-context](kubectl_config_current-context.md)	 - Display the current-context
* [kubectl config delete-cluster](kubectl_config_delete-cluster.md)	 - 从 kubeconfig 中删除指定的集群
* [kubectl config delete-context](kubectl_config_delete-context.md)	 - 从 kubeconfig 中删除指定的上下文
* [kubectl config delete-user](kubectl_config_delete-user.md)	 - Delete the specified user from the kubeconfig
* [kubectl config get-clusters](kubectl_config_get-clusters.md)	 - 显示在 kubeconfig 中定义的集群
* [kubectl config get-contexts](kubectl_config_get-contexts.md)	 - 描述一个或多个上下文
* [kubectl config get-users](kubectl_config_get-users.md)	 - Display users defined in the kubeconfig
* [kubectl config rename-context](kubectl_config_rename-context.md)	 - Rename a context from the kubeconfig file
* [kubectl config set](kubectl_config_set.md)	 - Set an individual value in a kubeconfig file
* [kubectl config set-cluster](kubectl_config_set-cluster.md)	 - Set a cluster entry in kubeconfig
* [kubectl config set-context](kubectl_config_set-context.md)	 - Set a context entry in kubeconfig
* [kubectl config set-credentials](kubectl_config_set-credentials.md)	 - Set a user entry in kubeconfig
* [kubectl config unset](kubectl_config_unset.md)	 - Unset an individual value in a kubeconfig file
* [kubectl config use-context](kubectl_config_use-context.md)	 - Set the current-context in a kubeconfig file
* [kubectl config view](kubectl_config_view.md)	 - 显示合并的 kubeconfig 配置或一个指定的 kubeconfig 文件

