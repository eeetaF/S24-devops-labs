# HELM

This document outlines the status of the moscow-time-app.

## PODS

The output of `kubectl get pods`:

```
$ kubectl get pods
NAME                               READY   STATUS    RESTARTS   AGE
moscow-time-app-5ccdcc795f-ztf8v   1/1     Running   0          12m
```

### SERVICES

The output of `kubectl get svc`:

```
$ kubectl get svc
NAME              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes        ClusterIP   10.96.0.1      <none>        443/TCP   15m
moscow-time-app   ClusterIP   10.99.219.17   <none>        80/TCP    13m
```