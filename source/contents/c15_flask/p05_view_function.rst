=============================
15.5 视图函数
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


注意：视图类中的方法就是支持的请求类型

..  image:: ./image/18101701.png
    :align: center
    :alt: 请求类型


利用方法视图子类创建一个视图函数
    TestMethodView.as_view('testMethodView')
    注意：as_view返回的是一个视图函数，而且该视图函数逇名称就是传进去的参数
 
将获取到的视图方法和路径对应起来
    app.add_url_rule('/test02/', view_func=TestMethodView.as_view('testMethodView'))

::

 from flask import Flask
 from flask import request
 from flask.views import MethodView

 app = Flask(__name__)

 @app.route('/')
 def index():
    return '测试主页面'

 @app.route('/test/', methods=['GET', 'POST'])
 def test():
    if request.method == 'GET':
        # 做GET的事情
        pass
    elif request.method == 'POST':
        # 做POST的事情
        pass
    return '测试'

 class TestMethodView(MethodView):
    def get(self):
        # 处理Get请求
        return 'GET请求'
    def post(self):
        # 处理post请求
        return 'POST请求'

 app.add_url_rule('/test02/', view_func=TestMethodView.as_view('testMethodView'))
 # method = TestMethodView.as_view('testMethodView');
 # app.add_url_rule('/test02/<name>/', view_func=method, methods=['GET'])

 print(app.url_map)

 if __name__ == '__main__':
    app.run(debug=True)

虽然在方法视图中定义的函数就是支持的请求类型，但是我们可以在配置路径时指定哪个路径对应哪中类型的请求
利用方法视图子类获取一个名字为testMethodView02的视图函数，该视图函数只能支持GET请求，而且支持转换器

::

 method02 = TestMethodView.as_view('testMethodView02');
 app.add_url_rule('/test02/<name>/', view_func=method02, methods=['GET'])

利用利用方法视图子类获取一个名字为testMethodView03的视图函数，该视图函数只能支持POST请求

::

 method03 = TestMethodView.as_view('testMethodView03')
 app.add_url_rule('/test03/', view_func=method03, methods=['POST'])

..  image:: ./image/18101702.png
    :align: center
    :alt: POST请求


::

 from flask import Flask
 from flask import request
 from flask.views import MethodView

 app = Flask(__name__)

 @app.route('/')
 def index():
    return '测试主页面'

 @app.route('/test/', methods=['GET', 'POST'])
 def test():
    if request.method == 'GET':
        # 做GET的事情
        pass
    elif request.method == 'POST':
        # 做POST的事情
        pass
    return '测试'

 class TestMethodView(MethodView):
    def get(self, name):
        # 处理Get请求, 也可以在这些方法中调用其他的方法
        return 'GET请求' + name
    def post(self):
        # 处理post请求, 也可以在这些方法中调用其他的方法
        return 'POST请求'

 # app.add_url_rule('/test02/', view_func=TestMethodView.as_view('testMethodView'))
 method02 = TestMethodView.as_view('testMethodView02');
 app.add_url_rule('/test02/<name>/', view_func=method02, methods=['GET'])
 method03 = TestMethodView.as_view('testMethodView03')
 app.add_url_rule('/test03/', view_func=method03, methods=['POST'])

 print(app.url_map)

 if __name__ == '__main__':
    app.run(debug=True)




