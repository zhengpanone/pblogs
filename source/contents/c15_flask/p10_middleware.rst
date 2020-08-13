=========================
10. 中间件
=========================

在函数执行之前或函数执行之后想做点事情，有2种方式

第一种：装饰器

第二种：flask里面的扩展，相当于django中的中间件


::

 from flask import Flask,session,Session,flash,get_flashed_messages,redirect,render_template,request
 app = Flask(__name__)
 app.secret_key ='sdfsdfsdf'

 @app.before_request
 def process_request1():
    print('process_request1')

 @app.after_request
 def process_response1(response):
    print('process_response1')
    return response


 @app.before_request
 def process_request2():
    print('process_request2')

 @app.after_request
 def process_response2(response):   #参数也得有
    print('process_response2')
    return response   #必须有返回值


 @app.route('/index')
 def index():
    print('index')
    return 'Index'

 @app.route('/order')
 def order():
    print('order')
    return 'order'

 @app.route('/test')
 def test():
    print('test')
    return 'test'

 if __name__ == '__main__':
    app.run()


运行结果：

..  image:: ./image/18101710_01.png
    :align: center
    :alt: 运行结果

还有一个@app.before_first_request：表示，当程序运行起来，第一个请求来的时候就只执行一次，下次再来就不会在执行了



