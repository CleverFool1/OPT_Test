from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask():  # 视图函数
    return 'Hello World'  # response


@app.route('/hi', methods=['GET', 'POST'])  # route()装饰器把一个函数绑定到对应的URL上
def index1():  # 视图函数

    return 'Index Page'  # response
    print('zheshizhangbinfei')


# string 接受任何不包含斜杠的文本
# int 接受正整数
# float 接受正浮点数
# path 接受包含斜杠的文本
@app.route('/user/<float:id>', methods=['GET', 'POST'])  # route()装饰器把一个函数绑定到对应的URL上
def index(id):  # 视图函数
    if id == 1.2:
        return 'Index Page1'  # response
    if id == str(2):
        return 'Index Page2'  # response
    if int(id) == 3:
        return 'Index Page3'  # response
    print('zheshi zhangbinfei ')
    return 'nothing'


# 自定义转化器  <int:id>  转化器

class RegexConverter(BaseConverter):
    '''自定义转化器类'''

    def __init__(self, url_map, regex):
        # 调用父类方法
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value: str):
        # 父类的方法 功能已经实现好 了
        print('to_python 方法被调用')
        return value


# 将自定义的转化器类添加到flask应用中,
app.url_map.converters['re'] = RegexConverter


# {'re':RegexConverter}

@app.route('/index/<re("789"):value>')  # route()装饰器把一个函数绑定到对应的URL上
def index2(value):  # 视图函数
    print(value)
    return 'Index Page2'  # response


if __name__ == '__main__':
    # app.run(debug=True)  # 启动socket
    # app.run()  # 启动socket
    # app.run(host='0.0.0.0')   # 使我的服务器公开可用
    app.run()
