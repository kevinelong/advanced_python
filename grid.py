data = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99],
]

print(data[1][2])  # row index 1 and column index 2 - prints what? 66

# data[1][-1] = 500
data[1][2] = 500

for row in data:
    for column in row:
        print(column, end=" ")
    print("")  # blank line
