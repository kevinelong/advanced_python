# netmikofrom netmiko import ConnectHandler
#
# linux = {
#     'device_type': 'linux',
#     'host':   '3.80.187.178',
#     'username': 'kevin',
#     'password': 'S!mpl312',
# }
# c = ConnectHandler(**linux) # use of kwargs optional, could just use regular parameters
#
# r1 = c.send_command("echo hello world  > hw.txt")
# print(r1)
#
# r2 = c.send_command("cat hw.txt")
# print(r2)
#
# r3 = c.send_command("ls -la")
# print(r3)


from netmiko import ConnectHandler
import paramiko
private_key_path = "~/.ssh/clvrclvr.pem"
linux = {
    'device_type': 'linux',
    'host':   'clvrclvr.pem',
    'username': 'kevin',
    'password': 'S!mpl312',
    'pkey' : paramiko.RSAKey.from_private_key_file(private_key_path)
}
c = ConnectHandler(**linux) # use of kwargs optional, could just use regular parameters

r1 = c.send_command("echo hello world  > hw.txt")
print(r1)

r2 = c.send_command("cat hw.txt")
print(r2)

r3 = c.send_command("ls -la")
print(r3)
