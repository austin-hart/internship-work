# pylint: skip-file
import grpc
from project.grpcdocs import oms_pb2
from project.grpcdocs import oms_pb2_grpc
import json

# open grpc channel
channel = grpc.insecure_channel(
    'localhost:50051', options=(('grpc.enable_http_proxy', 0),))

# create a stub
oms_stub = oms_pb2_grpc.OrderManagementSystemStub(
    channel)

# create request
place_order_request = oms_pb2.PlaceOrderGet(
    exchange="Polymarket", market="16678291189211314787145083999015737376658799626183230671758641503291735614088", side="buy", price=.69, size=100, kind="limit")
# obtain response
place_order_response = oms_stub.PlaceOrder(
    place_order_request)

print(place_order_response.json_data)


# add another endpoint wait for order for order confirmation
# on the oms, alpha calls place order gets id back.
# open wensocket when itilzie polymakret connection
