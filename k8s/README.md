# Kubernetes Deployment Report

This document provides an overview of the current Kubernetes setup for the `moscow-time-app`

## Pods

The output of `kubectl get pods`:

```
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
moscow-time-app-98b54bc88-9df27   1/1     Running   0          4m29s
```

## Services

The output of `kubectl get svc`:
NAME                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes                ClusterIP   10.96.0.1        <none>        443/TCP          5m19s
moscow-time-app-service   NodePort    10.107.152.216   <none>        5000:30001/TCP   5m6s
