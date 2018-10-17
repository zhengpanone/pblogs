=========================
20.9 闪现
=========================

session存在在服务端的一个字典里面，session保存起来，取一次里面还是有的，直到你删除之后才没有了

1、本质
-------------------------

flash是基于session创建的，flash支持往里边放值，只要你取一下就没有了，相当于pop了一下。不仅可以拿到值，而且可以把其从session里的去掉，

基于Session实现的用于保存数据的集合，其特点是：使用一次就删除。

2、闪现的用途
----------------------------------

某个数据仅需用一次时，可以使用闪现

::

 from flask import Flask,session,Session,flash,get_flashed_messages,redirect,render_template,request
 app = Flask(__name__)
 app.secret_key ='sdfsdfsdf'

 @app.route('/users')
 def users():
    # 方式一
    # msg = request.args.get('msg','')
    # 方式二
    # msg = session.get('msg')
    # if msg:
    #     del session['msg']
    # 方式三
    v = get_flashed_messages()　　# 获取flash中的值
    print(v)
    msg = ''
    return render_template('users.html',msg=msg)

 @app.route('/useradd')
 def user_add():
    # 在数据库中添加一条数据
    # 假设添加成功，在跳转到列表页面时，显示添加成功
    # 方式一
    # return redirect('/users?msg=添加成功')
    # 方式二
    # session['msg'] = '添加成功'
    # 方式三
    flash('添加成功')
    return redirect('/users')


 if __name__ == '__main__':
    app.run(debug=True)


