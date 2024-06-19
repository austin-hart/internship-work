from concurrent import futures
import logging
import grpc
from project.grpcdocs import repository_pb2
from project.grpcdocs import repository_pb2_grpc
import json


class RepositoryServicer(repository_pb2_grpc.RepositoryServicer):
    def __init__(self, repository_manager):
        self.repository_manager = repository_manager

    def GetTrade(self, GetRequest, context):
        """Initalizes trade fetcher object and gets json information from object."""
        json_data = self.repository_manager.get_trade(
            GetRequest.start_date, GetRequest.end_date, GetRequest.market, GetRequest.side, GetRequest.offset)
        response = repository_pb2.GetReturn(
            json_data=json_data)
        return response

    def PostTrade(self, PostRequest, context):
        confirmation = self.repository_manager.post_trade(
            PostRequest.json_data)
        response = repository_pb2.PostReturn(confirmation=confirmation)
        return response
