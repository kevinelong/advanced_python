import json
from json import JSONEncoder

data = {
    1 : 111,
    2: 222
}

text = json.dumps(data)
print(data)
print(text)

data_copy = json.loads(text)
print(data_copy)
