import pymysql

# 连接Mysql.我把root的密码改掉为空类
conn = pymysql.connect(host='127.0.0.1', user='root', password='', charset="utf8")
# conn = pymysql.connect(host='localhost',  user='root', password=' ', charset="utf8")
cursor = conn.cursor()





# 1.查看数据库
# 发送指令
cursor.execute("show databases")
# 获取指令的结果
result = cursor.fetchall()
print(result)
print('----------------------------------------------')



#3.删除数据库
cursor.execute("drop database db11 ")
cursor.execute("drop database db10 ")
conn.commit()
cursor.execute("show databases")
result = cursor.fetchall()
print(result)
print('----------------------------------------------')



#2.创建数据库
#发送指令
cursor.execute("create database db11 default charset utf8 collate utf8_general_ci")
conn.commit()
cursor.execute("show databases")
# 获取指令的结果
result = cursor.fetchall()
print(result)
print('----------------------------------------------')






# 4. 进入数据库,查看表
cursor.execute('use mysql')
cursor.execute('show tables')
result = cursor.fetchall()
print(result)
print('----------------------------------------------')



# 5
cursor.execute("select version()")
version=cursor.fetchall()
print("Mysql数据库版本是:%s"  % version)








# 关闭连接
cursor.close()
conn.close()
















# # 打开数据库连接
# db = pymysql.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()
