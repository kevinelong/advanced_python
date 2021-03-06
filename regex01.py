import re

line = "I think I thought I thunk."

match_result = re.match('think', line, re.M | re.I)
# print(match_result)
# 0-255 0x00000001

# rwx - chmod 770   owner,group,public rwxrwxrwx

# 000 700 770 755
# 101 rwx
#
#
if match_result:
    print("Match Found: " + match_result.group())
else:
    print("No match was found")

search_result = re.search('think', line, re.M | re.I)

if search_result:
    print("Search Found: " + search_result.group())
else:
    print("Nothing found in search")
