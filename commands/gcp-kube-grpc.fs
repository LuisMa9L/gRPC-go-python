kubectl get nodes

//crear despliegue
kubectl create deployment servidor --image=nginx

kubectl get pods

//para borrar 
//kubectl delete deploy/simple-deployment svc/simple-service

//exponer y crear sercio 
kubectl expose deployment servidor-go-1 --type=LoadBalancer --port=3001
kubectl expose deployment servidor-go-2 --type=LoadBalancer --port=3004
kubectl expose deployment servidor-py-1 --type=LoadBalancer --port=3001
kubectl expose deployment servidor-py-2 --type=LoadBalancer --port=3002
kubectl get services

kubectl get pods

kubectl exec -it pod /bin/bash

kubectl scale deployment --replicas=3 servidor
    
    1  apt update
    2  apt install git -y && apt install nano
    3  apt install python
    4  apt install python3
    5  apt install python-pip
    6  apt install python3-pip -y
    7  pip install virtualenv
    8  virtualenv -p python3.6 /tmp/country
    9  virtualenv -p python3 /tmp/country
   10  virtualenv -p python3 /tmp/corona
   11  source /tmp/corona/bin/activate
   12  pip install grpcio grpcio-tools
   13   pip freeze
   14  cd /home/
   15  git clone https://github.com/soylmml/gRPC-go-python.git
   16  cd gRPC-go-python/server/
   17  python corona_server.py
   18  python corona_server.py
   19  exit
   20  history