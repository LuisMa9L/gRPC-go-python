# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import coronavirus_pb2 as coronavirus__pb2


class DatosCoronarirusStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Datos = channel.unary_unary(
                '/coronavirus.DatosCoronarirus/Datos',
                request_serializer=coronavirus__pb2.Request.SerializeToString,
                response_deserializer=coronavirus__pb2.Reply.FromString,
                )


class DatosCoronarirusServicer(object):
    """The greeting service definition.
    """

    def Datos(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatosCoronarirusServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Datos': grpc.unary_unary_rpc_method_handler(
                    servicer.Datos,
                    request_deserializer=coronavirus__pb2.Request.FromString,
                    response_serializer=coronavirus__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'coronavirus.DatosCoronarirus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatosCoronarirus(object):
    """The greeting service definition.
    """

    @staticmethod
    def Datos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/coronavirus.DatosCoronarirus/Datos',
            coronavirus__pb2.Request.SerializeToString,
            coronavirus__pb2.Reply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)