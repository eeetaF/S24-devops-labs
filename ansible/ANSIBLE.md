# Ansible deployment output

## Deployment command logs
```
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_vm]

TASK [web_app : Ensure Docker is installed] ************************************
ok: [yandex_vm]

TASK [web_app : Pull the Docker image] *****************************************
ok: [yandex_vm]

TASK [web_app : Create and start the web application container] ****************
changed: [yandex_vm]

PLAY RECAP *********************************************************************
yandex_vm                  : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Remote Docker logs
```
sudo docker logs moscow-time-app_container
 * Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
46.226.162.31 - - [12/Nov/2024 18:13:39] "GET / HTTP/1.1" 200 -
46.226.162.31 - - [12/Nov/2024 18:13:39] "GET /static/moscow.jpg HTTP/1.1" 304 -
46.226.162.31 - - [12/Nov/2024 18:13:40] "GET / HTTP/1.1" 200 -
46.226.162.31 - - [12/Nov/2024 18:13:40] "GET /static/moscow.jpg HTTP/1.1" 304 -
```