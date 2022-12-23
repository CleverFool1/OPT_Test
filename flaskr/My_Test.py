# request 包含所有前端发送过来的所有请求数据


from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, redirect, make_response, json, jsonify
from wtforms import StringField,PasswordField
# from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 关闭config属性


@app.route('/index2', methods=['GET', 'POST'])  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask1():  # 视图函数

    if request.method == 'POST':  # '判断是post请求'
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)
        return 'this is post'
    if request.method == 'GET':  # '判断是get请求':
        return render_template('index.html')  # 表单渲染
    else:
        return 'hello word'


@app.route('/index')  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask():  # 视图函数
    print('123')
    return redirect('https://www.baidu.com')  # 重定向


@app.route('/index3')  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask3():  # 视图函数

    return redirect(url_for('first_flask'))  # 重定向 定向到自己内部定义的函数


@app.route('/index4')
def first_flask4():
    date = {'name': '张三'

            }
    # respone = make_response(json.dumps(date, ensure_ascii=False))  # 返回json数据给前端
    # respone.mimetype = 'application/json'
    # return respone

    return jsonify(date)  # 返回json数据给前端(第二种方法)
    # return jsonify(json.dumps(date,ensure_ascii=False))


# raise 主动抛出异常
# abort 在网页当中抛出异常
@app.route('/index5/', methods=['GET', 'POST'])
def first_flask5():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'zhang san' and password == '123':
            return 'login success'
        else:
            abort(404)
            return None


# 模板 jinja2
@app.route('/index6')
def first_flask6():
    data = {'name': '张三',
            'age': '18',
            'mylist': [1, 2, 3, 4, 2]}
    return render_template('index2.html', data=data)


# 自定义过滤器
def list_step(Li):
    return Li[::2]


# 注册过滤器,第一个 写自定义函数名字,第二个写自己要用的名字
app.add_template_filter(list_step, 'li')


# 表单模型类
@app.route('/index7')
def first_flask7():
    data = {'name': '张三',
            'age': '18',
            'mylist': [1, 2, 3, 4, 2]}
    return render_template('index2.html', data=data)





if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 9, 10]
    print(list_step(li))
    app.run()
