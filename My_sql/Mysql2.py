import pymysql

# 连接Mysql.我把root的密码改掉为空类
# Mysql语句的增加\修改\删除\查找
conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset="utf8")
# conn = pymysql.connect(host='localhost',  user='root', password=' ', charset="utf8")


# 获取游标
cursor = conn.cursor()

cursor.execute("use db1")

# 如果表存在，则先删除
cursor.execute("DROP TABLE IF EXISTS student")

# 设定SQL语句

sql = """
create table student(
    sno char(5),
    sname char(10),
    ssex char(2),
    sage int);
"""


# 执行SQL语句
cursor.execute(sql)

# 插入数据
sql = "INSERT INTO student(sno,sname,ssex,sage) VALUES ('%s', '%s', '%s', %d)"
data1 = ('95001', '王小明', '男', 21)
data2 = ('95002', '张梅梅', '女', 20)
data3 = ('95003', '张三', '男', 25)
data4 = ('95004', '李四', '女', 22)
cursor.execute(sql % data1)
cursor.execute(sql % data2)
cursor.execute(sql % data3)
cursor.execute(sql % data4)
conn.commit()
print('成功插入数据')

# 修改数据
sql = "UPDATE student SET sage = %d WHERE sno = '%s' "
data = (21, '95002')
cursor.execute(sql % data)
conn.commit()
print('成功修改数据')

# 查询数据
sql = "SELECT sno,sname,ssex,sage FROM student where sno = '%s' "
data = ('95001',)  # 元组中只有一个元素的时候需要加一个逗号
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("学号:%s\t姓名:%s\t性别:%s\t年龄:%d" % row)
print('共查找出', cursor.rowcount, '条数据')

# 删除数据
sql = "DELETE FROM student WHERE sno = '%s'"
data = ('95004',)  # 元组中只有一个元素的时候需要加一个逗号
cursor.execute(sql % data)
conn.commit()
print('成功删除', cursor.rowcount, '条数据')

# 关闭数据库连接
conn.close()
