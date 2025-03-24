========================
1. `基本使用`__
========================

.. __ : https://www.cnblogs.com/huchong/p/8227606.html#_lab2_1_0


2. URL与函数映射
===================

``app.route(<converter:variable_name>)``,其中converter就是类型名称，可以有以下几种

- ``string``: 默认的数据类型，接受任何没有斜杠 ``/\\`` 的文本
- ``int``: 接受整型
- ``float``: 接受浮点型
- ``path``: 和 ``string`` 类型类似，但是可以接受斜杠
- ``uuid``: 只接受uuid字符串
- ``any``: 可以指定多种路径

.. code-block:: python
    :linenos:

    @app.route('<any(article,blog):url_path>/<id>')
    def item(url_path,id):
        return url_path


1. 实例化Flask对象时，可选参数

.. code-block:: python
   :linenos:

    app = Flask(__name__)  # 这是实例化一个Flask对象，最基本的写法
    # 但是Flask中还有其他参数，以下是可填的参数，及其默认值
 
    def __init__(self,import_name,static_path=None,static_url_path=None,
                    static_folder='static',template_folder='templates',
                    instance_path=None,instance_relative_config=False,
                    root_path=None)

template_folder: 模板所在文件夹的名字
root_path: 可以不用填，会自动找到，当前执行文件，所在目录地址
在return render_template 时会将上面两个进行拼接，找到对应模板地址
static_folder：静态文件所在文件的名字，默认是static，可以不用填
static_url_path：静态文件的地址前缀，写成什么，访问静态文件时，就要在前面加上这个

.. code-block:: python
   :linenos:

    app = Flask(__name__,template_folder='templates',static_url_path='/xxxxxxxx')

如：在根目录下创建目录，templates和static，则return render_template时，可以找到里面的模板页面；如在static文件夹里存放11.png，在引用该图片时，静态文件地址为：/xxxxxx/11.png

instance_path和instance_relative_config是配合来用的、
这两个参数是用来找配置文件的，当用app.config.from_pyfile('settings.py')这种方式导入配置文件的时候会用到
instance_relative_config：默认为False，当设置为True时，from_pyfile会从instance_path指定的地址下查找文件。
instsnce_path：指定from_pyfile查询文件的路径，不设置时，默认寻找和app.run()的执行文件同级目录下的instance文件夹；如果配置了instance_path（注意需要是绝对路径），就会从指定的地址下里面的文件

2. 绑定路由关系的两种方式

.. code-block:: python
   :linenos:
    
    #方式一
    @app.route('/index.html',methods=['GET','POST'],endpoint='index')
    def index():
        return 'Index'
        
    #方式二
    def index():
        return "Index"

    self.add_url_rule(rule='/index.html', endpoint="index", view_func=index, methods=["GET","POST"])   
     #endpoint是别名
    # or
    app.add_url_rule(rule='/index.html', endpoint="index", view_func=index, methods=["GET","POST"])
    app.view_functions['index'] = index

添加路由关系的本质：将url和视图函数封装成一个Rule对象，添加到Flask的url_map字段中

3. Flask 中装饰器应用

.. literalinclude:: ./code/p01_flask_base/flask_wrapper.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 5
    :linenos: