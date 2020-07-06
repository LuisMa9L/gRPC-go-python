package main
import (
        "context"
        "log"
        "os"
        "time"
        pb "gRPC-go-python/proto"
        "google.golang.org/grpc"
)
const (
        address     = "34.70.238.234:3001"
        defaultName = "{\"Nombre\" :\"Danilo huevo\", \"Departamento\": \"Zona18\",\"Edad\": 1234, \"Contagio\": \"Anal\",\"Estado\": \"enfermro por zurdo\"}"
)
func main() {
        log.Printf("antes")
        hola := ""
                // Set up a connection to the server.
                conn, err := grpc.Dial(address, grpc.WithInsecure(), grpc.WithBlock())
                if err != nil {
                        log.Fatalf("did not connect: %v", err)
                }
                defer conn.Close()
                c := pb.NewDatosCoronarirusClient(conn)
                // Contact the server and print out its response.
                name := defaultName
                if len(os.Args) > 1 {
                        name = os.Args[1]
                }
        
	for i := 0; i < 10000; i++ {
                ctx, cancel := context.WithTimeout(context.Background(), time.Second)
                defer cancel()
		r, err := c.Datos(ctx, &pb.Request{Datoscorona: name})
                if err != nil {
                        log.Fatalf("could not greet (No Confirmacion): %v", err)
                }
                hola = r.GetConfirmacion()
                // log.Printf("Respusta del servidor: %s", r.GetConfirmacion())
        }
        log.Printf(hola)
        
}
