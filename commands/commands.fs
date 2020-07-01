(* variables de entorno para protoc pligin *)

export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOROOT:$GOPATH:$GOBIN


(* Compilando proto para python *)

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. coronavirus.proto


(* Compilando proto para golang *)

protoc --go_out=plugins=grpc:client proto/coronavirus.proto

