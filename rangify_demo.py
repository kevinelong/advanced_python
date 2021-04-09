from rangify_ports import rangify_ports

#  TODO READ FROM FILE
f = open("rangify_data.txt","r")
line = f.readline()

switch_ports_raw = line.split(",")
switch_ports = []
for item in switch_ports_raw:
    item = item.strip()
    item = item[1:-1]
    switch_ports.append(item)
result = rangify_ports(switch_ports)
print(result)
#EXPECTED OUTPUT: ['1/0/10-12', '1/0/20-21', '1/0/38', '1/0/48', '2/0/8-10']