========================
20.1 `基本使用`__
========================

.. __ : https://www.cnblogs.com/huchong/p/8227606.html#_lab2_1_0

1. 实例化Flask对象时，可选参数
    ::

     app = Flask(__name__)  # 这是实例化一个Flask对象，最基本的写法
     # 但是Flask中还有其他参数，以下是可填的参数，及其默认值
 
     def __init__(self,import_name,static_path=None,static_url_path=None,
     static_folder='static',template_folder='templates',instance_path=None,instance_relative_config=False,
     root_path=None)



