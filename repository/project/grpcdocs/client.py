import grpc
from project.grpcdocs import repository_pb2
from project.grpcdocs import repository_pb2_grpc
import json

file = open("project/service/trade3.json", "r")
json_obj = json.load(file)
json_data = json.dumps(json_obj)  # recived single trade from oms


channel = grpc.insecure_channel(
    'localhost:50051', options=(('grpc.enable_http_proxy', 0),))

repository_stub = repository_pb2_grpc.RepositoryStub(channel)

post_request = repository_pb2.PostRequest(json_data=json_data)

post_response = repository_stub.PostTrade(post_request)  # confirmation string

print(post_response.confirmation)


get_request = repository_pb2.GetRequest(
    start_date="2017-06-29 08:15:27.243860", end_date="2018-06-29 08:16:27.243860", market='brewers-cubs-124331232', side='buy', offset=0)

get_response = repository_stub.GetTrade(
    get_request)  # json data of filtered queries

print(get_response.json_data)
