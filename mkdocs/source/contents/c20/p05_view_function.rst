=============================
20.5 视图函数
=============================

1. Flask 中的CBV 和FBV
--------------------------------------------

::

 def auth(func):
    def inner(*args,**kwargs):
        result = func(**args,**kwargs)
        return result
    return inner

 class IndexView(views.MethodView):
    # method = ['post']   #只允许post请求
    decorators = [auth,]  #如果想给所有的get,post请求加装饰器，就可以这样来写，也可以单个指定

    def get(self):      #如果是get请求需要执行的代码
        v = url_for('index')
        print(v)
        return "GET"

    def post(self):     #如果是post请求执行的代码
        return "POST"

 app.add_url_rule('/index', view_func=IndexView.as_view(name="index"))      #name即FBV中的endpoint，指别名

 if __name__ =='__main__':
    app.run()


2. 类视图及使用
---------------------------------

    视图函数不能面向对象编程，利用类视图来代替视图函数来解决这个问题

导入视图类View
    from flask.views import View

编写一个视图子类

::

 class MyView(View):
    
    def test(self):
        return "测试类视图"

    def dispatch_request(self):     # 必须重写这个方法
        resp = self.test()
        return resp


利用View子类获取到一个视图方法

    MyView.as_view('test')
    注意：.as_view方法的返回值是一个方法，而且该方法的名字就是传进去的参数

将获取到的视图方法和路径对应起来
　　　　app.add_url_rule('/test/', view_func=MyView.as_view('test')) # MyView.as_view('test') 返回的是一个方法

类视图的原理
　　　　把as_view方法返回的结果赋值给view_func
　　　　as_view方法返回的是一个方法(注意：as_view方法传入的参数就是as_view返回的那个方法的名字)，该方法会调用dispatch_request方法
　　　　一旦路由进来，就会调用 dispatch_request 方法
　　　　类视图的目的就是实现逻辑分离、方便管理

::

 from flask import Flask
 from flask.views import View

 app = Flask(__name__)

 @app.route('/')
 def index():
    return 'Hello World'

 class MyView(View): # MyView继承于View

    def test(self):  #  自定义的方法
        return '测试类视图'

    def dispatch_request(self):   # 必须重写这个方法
        resp = self.test()
        return resp


 app.add_url_rule('/test/', view_func=MyView.as_view('test')) # MyView.as_view('test') 返回的是一个方法

 print(app.url_map)

 if __name__ == '__main__':
    app.run(debug=True)

 # 把as_view方法返回的结果赋值给view_func
 # as_view方法返回的是一个方法(注意：as_view方法传入的参数就是as_view返回的那个方法的名字)，该方法会调用dispatch_request方法
 # 一旦路由进来，就会调用 dispatch_request 方法
 # 类视图的目的就是实现逻辑分离、方便管理


3. 方法视图及使用
--------------------------------

利用视图函数实现不同的请求执行不同的逻辑时比较复杂，需要在视图函数函数中进行判断；如果利用方法视图实现就比较简单

::

 @app.route('/test/', methods=['GET', 'POST'])
 def test():
    if request.method == 'GET':
        # 做GET的事情
        pass
    elif request.method == 'POST':
        # 做POST的事情
        pass
    return '测试'


导入方法视图类

    from flask.views import MethodView

创建方法视图子类

::

 class TestMethodView(MethodView):
    def get(self):
        # 处理Get请求
        return 'GET请求'
    def post(self):
        # 处理post请求
        return 'POST请求'