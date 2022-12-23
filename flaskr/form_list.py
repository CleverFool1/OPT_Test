# form 表单的渲染
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)


@app.route('/index2')  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask1():  # 视图函数
    return render_template('index.html')  # 表单渲染


if __name__ == '__main__':
    app.run()
