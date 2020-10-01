
#PARSE JSON DATA FROM REDDIT API
#https://www.reddit.com/r/todayilearned/top.json?limit=100
import json
f=open("json_data.json", "r")
copy_from_disk = json.load(f) #READ

#use debugger set break point and browse results then copy square bracket path from  from "Evalute Expression"

#dense
# for index in range(len(copy_from_disk["data"]["children"])):
#     print(copy_from_disk["data"]["children"][index]["data"]["title"])
#a few levels at a time with sensible local var names

item_list = copy_from_disk['data']['children']
for item in item_list:
    # print(item["data"]["title"])
    d = item["data"]
    if d['upvote_ratio'] > 0.96:
        print(d["title"])
