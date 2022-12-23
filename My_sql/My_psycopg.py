# 导包
import psycopg2

# 创建连接对象
conn = psycopg2.connect(
    database='zhangbinfei',
    user='zhangbinfei',
    password='0212zbf',
    host='127.0.0.1',
    # port=5432

)
# 创建游标对象
cur = conn.cursor()

# 如果表存在，则先删除
cur.execute("DROP TABLE IF EXISTS student")  # 执行sql语句（创建表）
#   创建表
cur.execute("create table student(id integer, name varchar, sex varchar);")
# 执行sql语句（插入数据）
cur.execute("insert into student(id, name, sex) values (%s,%s,%s);", (1, "haha", "M"))
cur.execute("insert into student(id, name, sex) values (%s,%s,%s);", (2, "hehe", "W"))
cur.execute("insert into student(id, name, sex) values (%s,%s,%s);", (3, "heihei", "M"))


# 如果表存在，则先删除

cur.execute("DROP TABLE IF EXISTS company")  # 执行sql语句（创建表）
#   创建表
cur.execute("create table company(ID,NAME,AGE,ADDRESS,SALARY)")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 );")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")  # 获取执行结果（查询数据）
cur.execute("select * from student;")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

results = cur.fetchall()
print(results)
# 提交执行
conn.commit()
# 关闭游标
cur.close()
# 关闭连接
conn.close()
