=========================
9. 闪现
=========================

session存在在服务端的一个字典里面，session保存起来，取一次里面还是有的，直到你删除之后才没有了

1、本质
===============================

flash是基于session创建的，flash支持往里边放值，只要你取一下就没有了，相当于pop了一下。不仅可以拿到值，而且可以把其从session里的去掉，

基于Session实现的用于保存数据的集合，其特点是：使用一次就删除。

::

 session["操作"] = "msg"   # 设置
 session.get("操作") # 获取
 session.pop("操作") # 删除

2、闪现的用途
===========================

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

基本使用
>>>>>>>>>>>>>>>

::

 from flask import flash,get_flashed_messages

 def ...:
   ...
   flash("消息",'flag')
   ...
   return ..

 {% for msg in get_flashed_messages()%}
   <p class="login-box-msg">{{msg}}</p>
 {%endfo%}

通过flag 过滤flash消息
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 flash('添加成功','ok')
 {% for msg in get_flashed_messages(category_filter=['ok'])%}
 <div class="alert alert-success alert-dismissible">
        <button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>
        <h4><i class="icon fa fa-check"></i> 操作成功!</h4>
        {{ msg }}
 </div>
 {% endfor %}

3.cookie和session
===================================

cookie:
>>>>>>>>>>>>>>>>>>>>>>

1. \`cookie\`出现的原因：在网站中，http请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。cookie的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（cookie）给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。

2. 如果服务器返回了`cookie`给浏览器，那么浏览器下次再请求相同的服务器的时候，就会自动的把`cookie`发送给浏览器，这个过程，用户根本不需要管。

3. \`cookie\`是保存在浏览器中的，相对的是浏览器。

session:
>>>>>>>>>>>>>>>>>>>>>>

 1. \`session\`介绍：

 session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是，cookie是存储在本地浏览器，而session存储在服务器。存储在服务器的数据会更加的安全，不容易被窃取。但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，一些session信息还是绰绰有余的。

 2. 使用`session`的好处：
 
 * 敏感数据不是直接发送回给浏览器，而是发送回一个`session_id`，服务器将`session_id`和敏感数据做一个映射存储在`session`(在服务器上面)中，更加安全。
 * \`session\`可以设置过期时间，也从另外一方面，保证了用户的账号安全。

Flask中session机制：
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. flask中的session机制是：把敏感数据经过加密后放入`session`中，然后再把`session`存放到`cookie`中，下次请求的时候，再从浏览器发送过来的`cookie`中读取`session`，然后再从`session`中读取敏感数据，并进行解密，获取最终的用户数据。

2. flask的这种`session`机制，可以节省服务器的开销，因为把所有的信息都存储到了客户端（浏览器）。

3. 安全是相对的，把`session`放到`cookie`中，经过加密，也是比较安全的。

操作session：
>>>>>>>>>>>>>>>>>>>>>>>

1. session的操作方式：
* 使用`session`需要从`flask`中导入`session`，以后所有和`sessoin`相关的操作都是通过这个变量来的。
* 使用`session`需要设置`SECRET_KEY`，用来作为加密用的。并且这个`SECRET_KEY`如果每次服务器启动后都变化的话，那么之前的`session`就不能再通过当前这个`SECRET_KEY`进行解密了。
* 操作`session`的时候，跟操作字典是一样的。
* 添加`session`：`session['username']`。
* 删除：`session.pop('username')`或者`del session['username']`。
* 清除所有`session`：`session.clear()`
* 获取`session`：`session.get('username')`

2. 设置session的过期时间：
* 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束
* 如果设置了session的permanent属性为True，那么过期时间是31天。
* 可以通过给`app.config`设置`PERMANENT_SESSION_LIFETIME`来更改过期时间，这个值的数据类型是`datetime.timedelay`类型。

