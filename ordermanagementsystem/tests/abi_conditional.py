import json

file = open("tests/abi_conditional.json", "r")
json_obj = json.load(file)
json_str = json.dumps(json_obj)
EIP20_ABI_CON = json.loads(json_str)
