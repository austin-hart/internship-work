# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import repository_pb2 as repository__pb2


class RepositoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTrade = channel.unary_unary(
                '/Repository/GetTrade',
                request_serializer=repository__pb2.GetRequest.SerializeToString,
                response_deserializer=repository__pb2.GetReturn.FromString,
                )
        self.PostTrade = channel.unary_unary(
                '/Repository/PostTrade',
                request_serializer=repository__pb2.PostRequest.SerializeToString,
                response_deserializer=repository__pb2.PostReturn.FromString,
                )


class RepositoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTrade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostTrade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RepositoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTrade': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrade,
                    request_deserializer=repository__pb2.GetRequest.FromString,
                    response_serializer=repository__pb2.GetReturn.SerializeToString,
            ),
            'PostTrade': grpc.unary_unary_rpc_method_handler(
                    servicer.PostTrade,
                    request_deserializer=repository__pb2.PostRequest.FromString,
                    response_serializer=repository__pb2.PostReturn.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Repository', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Repository(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTrade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Repository/GetTrade',
            repository__pb2.GetRequest.SerializeToString,
            repository__pb2.GetReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostTrade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Repository/PostTrade',
            repository__pb2.PostRequest.SerializeToString,
            repository__pb2.PostReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
