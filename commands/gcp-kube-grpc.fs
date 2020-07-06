kubectl get nodes

//crear despliegue
kubectl create deployment servidor --image=nginx

kubectl get pods

//para borrar 
//kubectl delete deploy/simple-deployment svc/simple-service

//exponer y crear sercio 
kubectl expose deployment servidor-go-1 --type=LoadBalancer --port=3001
kubectl expose deployment servidor-go-2 --type=LoadBalancer --port=3001
kubectl expose deployment servidor-py-1 --type=LoadBalancer --port=3001
kubectl expose deployment servidor-py-2 --type=LoadBalancer --port=3001
kubectl expose deployment nginx-lb --type=LoadBalancer --port=3001
kubectl get services

kubectl get pods

//entrar al contenedor  
kubectl exec -it pod -- /bin/bash

kubectl scale deployment --replicas=3 servidor
     

    2  apt update

    4  apt install python
    5  apt install nano

    7  python --version
    8  apt install git -y

    10  cd home/

   12  git clone https://github.com/soylmml/gRPC-go-python.git

   14  cd gRPC-go-python/

   16  cd server/

   18  python corona_server.py
   19  apt instal pip
   20  apt install pip
   21  apt install python-pip
   22  python corona_server.py
   23  pip install grpcio grpcio-tools
   24  pip freeze
   25  pip install grpcio grpcio-tools
   26  python corona_server.py
   27  apt install python-pip3
   28  apt install python3
   29  apt install python-pip3
   30  apt install python3-pip
   31  virtualenv -p python3.6 /tmp/country
   32  python install virtualenv
   33  pip install virtualenv
   34  virtualenv -p python3.6 /tmp/country
   35  apt install python3
   36  virtualenv -p python3.6 /tmp/country
   37  virtualenv -p python /tmp/country
   38  virtualenv -p python3 /tmp/country
   39  source /tmp/corona/bin/activate
   40  pip install grpcio grpcio-tools
   41  pip freeze   