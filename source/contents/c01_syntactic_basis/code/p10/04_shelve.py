import shelve

# 打开文件，设置键值对
sh = shelve.open("shelve")
sh["name"] = "古明地觉"
sh["score"] = [80, 80, 80]
sh.close()

# 重新打开文件，修改键值对
sh = shelve.open("shelve", writeback=True)
sh["name"] = "芙兰朵露"
sh["score"].append(90)
sh.close()

# 再次重新打开文件，查看键值对
sh = shelve.open("shelve")
print(sh["name"])
print(sh["score"])
"""
芙兰朵露
[80, 80, 80, 90]
"""
sh.close()