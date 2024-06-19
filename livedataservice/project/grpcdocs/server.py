# pylint: skip-file
from concurrent import futures
import logging
import grpc
#from get_feed_id_pb2_grpc import add_GetFeedIDServicer_to_server
from project.grpcdocs import live_data_service_pb2
from project.grpcdocs import live_data_service_pb2_grpc
from project.service.odds_api_price_fetcher import OddsApiPriceFetcher
import json


class LiveDataServiceServicer(live_data_service_pb2_grpc.LiveDataServiceServicer):
    def __init__(self, data_feed_manager):
        self.data_feed_manager = data_feed_manager

    def RegisterOddsApiFeed(self, FeedIDRequest, context):
        price_fetcher = OddsApiPriceFetcher(
            FeedIDRequest.sport, FeedIDRequest.market, FeedIDRequest.event_id)
        uuid_str = self.data_feed_manager.register_feed(
            price_fetcher=price_fetcher, cadence=1)
        response = live_data_service_pb2.FeedIDReturn(uuid=uuid_str)
        return response

    def GetValueOfFeed(self, FeedIDRequest, context):
        value = self.data_feed_manager.get_value_by_uuid(FeedIDRequest.uuid)
        value_string = json.dumps(value)
        response = live_data_service_pb2.Value(value=value_string)
        return response

    def GetSupportedFeeds(self):
        file = open("feed_info.json")
        data = json.dumps(file)
        response = live_data_service_pb2.Context(data)
        return response

    def DeleteFeed(self, DeleteFeedID):
        self.data_feed_manager.delete_feed(DeleteFeedID)
