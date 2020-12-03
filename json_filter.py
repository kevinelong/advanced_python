data = [
    {"name": "aaa", "title": "SIONR IT ABC"},
    {"name": "bbb", "title": "SIONR ZZZ ABC"},
    {"name": "ccc", "title": "SIONR IT ABC"},
]

output = []

for e in data:
    if "IT" in e["title"]:
        output.append(e)

print(output)
