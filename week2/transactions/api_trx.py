import json
import requests

trxhash = "84c104d9677c0b0f9ad3c411eff5d1493c6b0da21f846b942d4ccae140ab89a7"

resp = requests.get("https://blockchain.info/rawtx/"+trxhash)

outputs = json.loads(resp.text)['out']

inputs = json.loads(resp.text)['inputs']
# print(inputs)
print("INPUTS")
for inp in inputs:
	inp = inp['prev_out']
	print(f"{inp['addr']} - {inp['value']} satoshi")

print("OUTPUTS")
for output in outputs:
	print(f"{output['addr']} - {output['value']} satoshi")