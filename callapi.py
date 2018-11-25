import requests
import json

client = requests.session()
parameters = {
    "mytest" : "hello",
    "age": 2,
    "name" : ["malu","jasu","gopi"]
}

output = client.post("http://localhost:5000", json=parameters)

if output.status_code == 200:
    out = output.content
    json_out = json.loads(out)
    print(json_out)

else:
    print("Failure response from API")
    print(output.reason)
    print(output.content)

