import json

data = [
    [123, 456],
    [234, 567],
]

f = open("json_file_io_by_line.json", "a")
for item in data:
    f.write(json.dumps(item) + "\n")
f.close()

copy_from_disk = []
f = open("json_file_io_by_line.json", "r")
for line in f.readlines():
    copy_from_disk.append(json.loads(line))

print(copy_from_disk)



