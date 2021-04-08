import json

data = {
    'a': 100,
     'b': 200,
     'c': 300
}

output = json.dumps(data, indent=4)

print(len(output))
print(output)
restored = json.loads(output)

print(restored["c"])