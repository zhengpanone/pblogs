import dbm

# 第一个参数是文件名
# 第二个参数是模式，有以下几种
#     r：只读，要求文件必须存在，默认就是这个模式
#     w：可读可写，要求文件必须存在
#     c：可读可写，文件不存在会创建，存在则追加
#     n：可读可写，文件不存在会创建，存在则清空
# 第三个参数是权限，用八进制数字表示，默认 0o666，即可读可写不可执行
db = dbm.open('store','c')

# 打开文件就可以存储值了，key 和 value 必须是字符串或 bytes 对象
db['name']='S せんせい'
db["age"] = "18"
db[b"corporation"] = "小摩".encode("utf-8")

# 获取所有的 key，直接返回一个列表
print(db.keys())

# 判断一个 key 是否存在，key 可以是字符串或 bytes 对象
print("name" in db, "NAME" in db)

# 获取一个 key 对应的 value，得到的是 bytes 对象
print(db["name"].decode("utf-8"))
print(db[b"corporation"].decode("utf-8"))

# key 如果不存在，会抛出 KeyError，我们可以使用 get 方法
print(db.get("NAME", b"unkonwn"))

# 当然也可以使用 setdefault 方法，key 不存在时，自动写进去
print(db.setdefault('gender',b'female'))
print(db['gender'])

db.close()