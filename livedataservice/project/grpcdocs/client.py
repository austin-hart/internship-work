# pylint: skip-file
import grpc
from project.grpcdocs import live_data_service_pb2
from project.grpcdocs import live_data_service_pb2_grpc
import json

# open grpc channel
channel = grpc.insecure_channel(
    'localhost:50051', options=(('grpc.enable_http_proxy', 0),))

# create a stub
data_feed_manager_stub = live_data_service_pb2_grpc.LiveDataServiceStub(
    channel)

# create request
odds_api_request = live_data_service_pb2.OddsApiInfo(
    event_id='0f801f5b350f46e3ee4f9d2cc4cff3e5', sport='baseball_mlb', market='h2h')
# obtain response
odds_api_response = data_feed_manager_stub.RegisterOddsApiFeed(
    odds_api_request)

odds_api_request_2 = live_data_service_pb2.OddsApiInfo(
    event_id='cf4ec3d809817928b0e9ba00765c29a5', sport='baseball_mlb', market='h2h')
# obtain response
odds_api_response_2 = data_feed_manager_stub.RegisterOddsApiFeed(
    odds_api_request_2)

print(odds_api_response, odds_api_response_2)

value_request = live_data_service_pb2.FeedIDRequest(
    uuid=odds_api_response.uuid)
value_response = data_feed_manager_stub.GetValueOfFeed(value_request)
print(json.loads(value_response.value))
