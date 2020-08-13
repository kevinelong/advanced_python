

data = "12/12/2222 12:34:56"

# how do we get the value 56
parts = data.split(" ")
date_part = parts[0]
time_part = parts[1]

print(time_part)
time_part_list = time_part.split(":")

print(time_part_list)
print(len(time_part_list))

if len(time_part_list) == 3:
    hours = time_part_list[0]
    minutes = time_part_list[1]
    seconds = time_part_list[2]

    output_text = f"HR: {hours}, MIN: {minutes}, SECS: {seconds}, "
    print(output_text)

ip_address = "127.0.0.123"
print(ip_address.split(".")[3])

# how do we get 1

