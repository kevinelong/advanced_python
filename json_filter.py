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

# >>> even_squares = [x * x for x in range(10) if x % 2 == 0]
# do it in one line with a list comprehension! ugly? hard to read? maybe.
it_folks = [e for e in data if "IT" in e["title"]]
print(it_folks)
