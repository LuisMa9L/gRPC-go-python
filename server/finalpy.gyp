
from concurrent import futures
from threading import Thread
#import logging
import grpc
import coronavirus_pb2
import coronavirus_pb2_grpc
import json
import pymongo
import redis
# mongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb://doch.ml/coronavirusDoch")
db = client.coronavirusDoch
infectados = db.datos
# redis
cr = redis.Redis('doch.ml')
class DatosCoronavirus(coronavirus_pb2_grpc.DatosCoronarirusServicer):
    def Datos(self, request, context):
        def parse_request():
            #print(request.datoscorona)
            # mongo
            datoinfectado = json.loads(request.datoscorona)
            infectados.insert(datoinfectado)
            # redis
            contador = 0
            for key in cr.scan_iter("CORONAVIRUSDOCH:*"):
                contador = contador + 1
            cr.hmset("CORONAVIRUSDOCH:" + str(contador + 1),{"Nombre": datoinfectado['Nombre'], "Departamento": datoinfectado['Departamento'], "Edad": datoinfectado['Edad'], "Contagio": datoinfectado['Contagio'], "Estado": datoinfectado['Estado']})# """
        t = Thread(target=parse_request)
        t.start()
        response = coronavirus_pb2.Reply(confirmacion='Datos recibidos: --> %s!' % request.datoscorona)
        print("Datos insertados")
        return response
def serve():
    print("Servidor corriendo...")
    server = grpc.server(futures.ThreadPoolExecutor())
    coronavirus_pb2_grpc.add_DatosCoronarirusServicer_to_server(DatosCoronavirus(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()
if __name__ == '__main__':
    #logging.basicConfig()
    serve()