# Proto3 para gRCP
### 1. Instalar [Protocol Buffer Compiler](https://grpc.io/docs/protoc-installation/)


- Linux
  
```sh
apt install -y protobuf-compiler
protoc --version # 
```
- MacOS
```sh
brew install protobuf
protoc --version  #
```
### 2. Instalar las librearias de proto dependiendo del lenguaje    

### 3. Variables de entorno para poder utilizar el plugin de proto en golang

```
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOROOT:$GOPATH:$GOBIN
```


### 4. Compilando archivo proto para python

    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. coronavirus.proto


### 5. Compilando archivo proto para golang

    protoc --go_out=plugins=grpc:client proto/coronavirus.proto

