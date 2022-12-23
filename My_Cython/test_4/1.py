# coding: utf-8
# 这个import会先找hello.py，找不到就会找hello.so
import hello  # 导入了hello.so

hello.say_hello_to('张三')
print(hello.logsum(2,6))