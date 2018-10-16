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

    


