import subprocess


def run(exe):
    cmd = exe.split(" ")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


result = run("ls -la")
# print(result)

i = 0
for line in result:
    # print(line.decode().split(" ")) # WRONG
    if i > 0:
        print(i, line.decode().split(None)) #RIGHT deals with repeating white space
    i += 1

# ---

import os
# Get all filenames in working directory
# for filename in os.listdir('./'):
#     print(filename)
