data = """
 *>i  10.93.16.0/22    172.23.111.3           100    100      0 i
 *>i  10.93.20.0/23    172.23.111.3           100    100      0 i
 *>i  10.93.22.0/24    172.23.111.3           100    100      0 i 
 *>i  10.93.0.0/16     172.23.111.1           100    100      0 i
 *>i  10.93.250.16/32  172.23.111.1           100    100      0 i
 *>i  10.93.250.17/32  172.23.111.1          1000    100      0 i
 *>i  10.93.62.0/23    172.23.111.5           100    100      0 i 
 *>i  10.93.250.10/32  172.23.111.5           100    100      0 i
 *>i  10.93.250.9/32   172.23.111.3           100    100      0 i 
"""

lines = data.split("\n")
rows = []
for line in lines:
    rows.append(line.split())

print(rows)

output = {}

KEY_ROUTE_INDEX=1
KEY_IP_INDEX=2
KEY_MED_INDEX=3

for row in rows:
    if len(row) > 0:
        if row[KEY_MED_INDEX] == '100':
            ip = row[KEY_IP_INDEX]
            route = row[KEY_ROUTE_INDEX]
            parts = route.split("/")
            prefix = parts[1]

            if ip not in output:
                output[ip] = []
            if prefix == "32":
                output[ip].insert(0,route)
            else:
                output[ip].append(route)
# print(output)
import json
print(json.dumps(output, indent=12))