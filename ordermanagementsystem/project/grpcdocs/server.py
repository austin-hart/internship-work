# pylint: skip-file
from concurrent import futures
import grpc
from project.grpcdocs import oms_pb2
from project.grpcdocs import oms_pb2_grpc
from project.service.order_management_system import OrderManagementSystem
import json
import logging


class OrderManagementSystemServicer(oms_pb2_grpc.OrderManagementSystemServicer):
    def __init__(self):
        self.oms = OrderManagementSystem()

    def GetSupportedExchanges(self, request, context):
        confirmation = self.oms.get_supported_exchanges()
        response = oms_pb2.SupportedExchangesPost(json_data=str(confirmation))
        return response

    def GetSupportedMarkets(self, request, context):
        confirmation = self.oms.get_supported_market_for_exchange(
            request.exchange)
        response = oms_pb2.SupportedMarketsPost(json_data=confirmation)
        return response

    def PlaceOrder(self, request, context):
        order_id = self.oms.register_order(
            request.exchange, request.market, request.side, request.price, request.size, request.kind)
        confirmation = self.oms.place_order(order_id)
        confirmation['order_id'] = order_id
        response = oms_pb2.PlaceOrderPost(json_data=str(confirmation))
        return response

    def CancelOrder(self, request, context):
        confirmation = self.oms.cancel_order(request.order_id)
        response = oms_pb2.CancelOrderPost(json_data=confirmation)
        return response

    def GetOrderStatus(self, request, context):
        confirmation = self.oms.get_order_status(request.order_id)
        response = oms_pb2.OrderStatusPost(json_data=str(confirmation))
        return response
