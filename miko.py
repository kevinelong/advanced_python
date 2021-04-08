from netmiko import ConnectHandler

linux = {
    'device_type': 'linux',
    'host':   '54.224.250.13',
    'username': 'kevin',
    'password': 'S!mpl312',
}
c = ConnectHandler(**linux) # use of kwargs optional, could just use regular parameters

r1 = c.send_command("echo hello world  > hw.txt")
print(r1)

r2 = c.send_command("cat hw.txt")
print(r2)

r3 = c.send_command("ls -la")
print(r3)
#---

lines = r3.split("\n")

NAME_INDEX = 8

for item in lines:
    #     parts = item.split(" ") # split on space
    #     parts = re.split(' +', item) # use regex to split on more than one space
    parts = item.split() # no parameters does the right thing!
    print(parts)
    if len(parts) >= NAME_INDEX:
        file_name = parts[NAME_INDEX]
        print(file_name)
        if file_name == "hw.txt":
            print("YAY!!!")
            r4 = c.send_command("rm hw.txt")
            print(r4)

# from netmiko import ConnectHandler
# import paramiko
# private_key_path = "~/.ssh/clvrclvr.pem"
# linux = {
#     'device_type': 'linux',
#     'host':   'clvrclvr.com',
#     'username': 'kevin',
#     'password': 'S!mpl312',
#     'pkey' : paramiko.RSAKey.from_private_key_file(private_key_path)
# }
# c = ConnectHandler(**linux) # use of kwargs optional, could just use regular parameters

# r1 = c.send_command("echo hello world  > hw.txt")
# print(r1)

# r2 = c.send_command("cat hw.txt")
# print(r2)

# r3 = c.send_command("ls -la")
# # print(r3)
