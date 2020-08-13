import json

data = [
    [123, 456],
    [234, 567],
]

json.dump(data, open("json_file_io.json", "w")) #WRITE

copy_from_disk = json.load(open("json_file_io.json", "r")) #READ

print(copy_from_disk)



