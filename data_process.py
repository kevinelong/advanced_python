
data = {
    "from" : "123.123.123.123",
    "info" : {
        "rawdata" : [
            [123, 356, 999],
            [121, 556, 222],
            [124, 256, 111],
            [121, 256, 234],
            [122, 356, 123],
        ]
    }
}

my_data = data["info"]["rawdata"]
ID = 0
SERVER = 1
TIME = 2

times = []
group_totals = {}

for item in my_data:
    server = item[SERVER]
    t = item[TIME]
    times.append(t)
    if server not in group_totals:
        group_totals[server] = t
    else:
        group_totals[server] += t

print(group_totals)

coins = [1,1,1,5,5,5,5,5,10,10,25,25,25]

# how many of each do we have? can exclude pennies?

output = {}
for c in coins:
    if c not in output:
        output[c] = 1
    else:
        output[c] += 1
print(output)
