## kubectl rollout

Manage the rollout of a resource

### Synopsis

Manage the rollout of one or many resources.
        
 Valid resource types include:

  *  deployments
  *  daemonsets
  *  statefulsets

```
kubectl rollout SUBCOMMAND
```

### Examples

```
  # Rollback to the previous deployment
  kubectl rollout undo deployment/abc
  
  # Check the rollout status of a daemonset
  kubectl rollout status daemonset/foo
  
  # Restart a deployment
  kubectl rollout restart deployment/abc
  
  # Restart deployments with the 'app=nginx' label
  kubectl rollout restart deployment --selector=app=nginx
```

### Options

```
  -h, --help   help for rollout
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

* [kubectl](kubectl.md)	 - kubectl 控制 Kubernetes 集群管理器
* [kubectl rollout history](kubectl_rollout_history.md)	 - 显示上线历史
* [kubectl rollout pause](kubectl_rollout_pause.md)	 - 将所指定的资源标记为已暂停
* [kubectl rollout restart](kubectl_rollout_restart.md)	 - Restart a resource
* [kubectl rollout resume](kubectl_rollout_resume.md)	 - 恢复暂停的资源
* [kubectl rollout status](kubectl_rollout_status.md)	 - 显示上线的状态
* [kubectl rollout undo](kubectl_rollout_undo.md)	 - 撤销上一次的上线

