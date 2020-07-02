import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pattern', help='pattern to search for')
parser.add_argument('path', help='file to search')
args = parser.parse_args()

search_file = open(args.path)
line_number = 0
count = 0
for line in search_file.readlines():
    line = line.strip('\n\r')
    line_number += 1
    search_result = re.search(args.pattern, line, re.M | re.I)

    if search_result:
        print(str(line_number) + ': ' + line)
        count += 1

if count == 0:
    print("no match")
