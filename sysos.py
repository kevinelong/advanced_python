import subprocess


def run(exe):
    cmd = exe.split(" ")
    p = subprocess.Popen(
        cmd, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        shell=True
    )
    return iter(p.stdout.readline, b'')


result = run("dir")
# print(result)

FILE_COLUMN = 4


def is_valid(line_data):
    return line_data and line_data[0] != "Directory" and line_data[0] != "Volume" and line_data[-1] != "bytes"


for line in result:
    raw_line = line.decode()
    line_data = raw_line.split()

    if is_valid(line_data):
        file_name = line_data[FILE_COLUMN]
        parts = file_name.split(".")
        if parts[-1] == "txt":
            print(file_name)

# ---

import os
# Get all filenames in working directory
# for filename in os.listdir('./'):
#     print(filename)
