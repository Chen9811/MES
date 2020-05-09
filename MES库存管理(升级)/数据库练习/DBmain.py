import sqlite3

mydb = sqlite3.connect('garbage.sqlite')  # 连接到数据库，如果没有会自动创建一个
c = mydb.cursor()
print("Opened database successfully")
trash = {1: "可回收垃圾", 2: "有害垃圾", 4: "湿垃圾", 8: "干垃圾", 16: "大件垃圾"}  # 创建字典

#def check():
cursor = c.execute("SELECT name, category from Garbage")  #选择name,category列，Garbage为表名
n = 0
gar = input('请输入垃圾名称')  # 获取文本
for row in cursor:    #row为元组格式
    if row[0] == gar:
        break  # 匹配到后退出for循环
    else:
        n = n + 1
print(n)
if n > 3985:
    print("无匹配垃圾")
else:
    print(str(trash[row[1]]))


# check()
