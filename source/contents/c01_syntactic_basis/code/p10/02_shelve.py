import shelve

class People:
  def __init__(self,name,age) -> None:
    self.name = name
    self.age = age

  @property
  def print_info(self):
    return f"name is {self.name} and age is {self.age}"

# 第二个参数表示模式，默认是 c
# 因此文件不存在会创建，存在则追加
sh = shelve.open('shelve')

sh["name"] = ["S 老师", "高老师", "电烤🐔架"]
sh["age"] = {18}
sh["job"] = {"tutu": "大学生", "xueer": "医生"}
p = People("群主",58)
sh['People'] = People
sh["p"] = p

print(sh["name"])
print(sh["name"][2]=='电烤🐔架')

print(sh['age'])

print(sh["job"])

try:
  sh["People"]
except AttributeError as e:
  print(e)

print(sh['People'] is People)
print(sh['p'].print_info)

print(sh["People"]('张三', 38).print_info)


# 关闭文件，刷到磁盘中
sh.close()