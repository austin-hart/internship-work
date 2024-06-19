import json

file = open("tests/abi.json", "r")
json_obj = json.load(file)
json_str = json.dumps(json_obj)
EIP20_ABI = json.loads(json_str)
