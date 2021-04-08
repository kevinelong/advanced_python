
#PARSE JSON DATA FROM REDDIT API
#https://www.reddit.com/r/todayilearned/top.json?limit=100
import json
f=open("json_data.json", "r")
copy_from_disk = json.load(f) #READ

#use debugger set break point and browse results then copy square bracket path from  from "Evalute Expression"

print(copy_from_disk["data"]["children"][-1]["data"]["title"])
#dense
# how_many_children = len(copy_from_disk["data"]["children"])
# print("how_many_children =", how_many_children)
# for index in range(0, how_many_children):
#     print(index, copy_from_disk["data"]["children"][index]["data"]["title"])
#a few levels at a time with sensible local var names

item_list = copy_from_disk['data']['children']
for item in item_list:
    # print(item["data"]["title"])
    d = item["data"]
    if d['upvote_ratio'] > 0.96:
        print(d["title"])
        print("")
