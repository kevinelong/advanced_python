import json

data = {
    1: 111,
    2: 222,
    333: True,
    4444: 'Now is \"the\" time don\'t ...'
}

text = json.dumps(data)
print(data)
print(text)

data_copy = json.loads(text)
print(data_copy)
