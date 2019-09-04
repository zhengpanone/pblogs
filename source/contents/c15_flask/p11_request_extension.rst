=========================
20.11 请求扩展
=========================

::

 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 from flask import Flask, Request, render_template

 app = Flask(__name__, template_folder='templates')
 app.debug = True


 @app.before_first_request    # 只在第一次请求到来时执行一次，后面不会再执行
 def before_first_request1():
    print('before_first_request1')


 @app.before_first_request
 def before_first_request2():
    print('before_first_request2')


 @app.before_request    # 每次请求到来时，都会执行
 def before_request1():
    Request.nnn = 123
    print('before_request1')


 @app.before_request
 def before_request2():
    print('before_request2')


 @app.after_request    # 每次响应时执行
 def after_request1(response):
    print('before_request1', response)
    return response


 @app.after_request
 def after_request2(response):
    print('before_request2', response)
    return response


 @app.errorhandler(404)
 def page_not_found(error):
    return 'This page does not exist', 404


 @app.template_global()    # 自定义标签，所有页面都直接使用
 def sb(a1, a2):
    return a1 + a2


 @app.template_filter()    # 自定义过滤器，所有页面都直接使用
 def db(a1, a2, a3):
    return a1 + a2 + a3


 @app.route('/')    # 访问的url，不加其他后缀时，也要有/
 def hello_world():
    return render_template('hello.html')


 if __name__ == '__main__':
    app.run()

自定义标签和过滤器在页面上的调用方式：{{sb(1,2)}}  {{ 1|db(2,3)}}