### 1. Variables de entorno para para poder utilizar el de proto3 plugin

```
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOROOT:$GOPATH:$GOBIN
```


### 2. Compilando proto para python

    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. coronavirus.proto


### 3. Compilando proto para golang

    protoc --go_out=plugins=grpc:client proto/coronavirus.proto

