from flask import Flask, url_for
from flask import request

app = Flask(__name__)  # 创建1个Flask实例


@app.route('/')  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask():  # 视图函数
    return 'Hello World'  # response


@app.route('/')  # route()装饰器把一个函数绑定到对应的URL上
def index():  # 视图函数
    return 'Index Page'  # response


#  '''给URL添加变量部分,标记特殊字段'''


@app.route('/user/<username>')
def show_user_profile(username):  # 显示用户配置文件
    return 'User %s'  # username>


@app.route('/post/<int:post_id>')
def show_post(post_id):  # 显示带有给定id的地址
    return 'Post %s'  # post_id>


#  ''' 唯一URL/重定向行为:基于Werkzeug的路由模块'''

@app.route('/projects/')
def projects():  # 尾段有一个斜线
    return 'The project page'  # post_id>


@app.route('/about')
def about():  # 无斜线
    return 'The about page'  # post_id>


@app.route('/login')
def login(): pass


@app.route('/user/<username>')
def profile(username): pass


# url_for构造Url
with    app.test_request_context('hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

    print
    url_for('index')
    print
    url_for('login')
    # print
    # url_for('login', next('/'))
    print
    url_for('profile', username='ZhangBinFei')

if __name__ == '__main__':
    app.run(debug=True)  # 启动socket
    # app.run()  # 启动socket
    # app.run(host='0.0.0.0')   # 使我的服务器公开可用
    app.run()
