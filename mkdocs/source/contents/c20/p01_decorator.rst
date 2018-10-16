========================
20.1 基本使用
========================

1. 实例化Flask对象时，可选参数
::
 app = Flask(__name__)  # 这是实例化一个Flask对象，最基本的写法
 # 但是Flask中还有其他参数，以下是可填的参数，及其默认值
 
 def __init__(self,import_name,static_path=None,static_url_path=None,
 static_folder='static',template_folder='templates',instance_path=None,instance_relative_config=False,
 root_path=None)


template_folder: 模板所在文件夹的名字
root_path: 可以不用填，会自动找到，当前执行文件，所在目录地址
在return render_template 时会将上面两个进行拼接，找到对应模板地址
static_folder：静态文件所在文件的名字，默认是static，可以不用填
static_url_path：静态文件的地址前缀，写成什么，访问静态文件时，就要在前面加上这个

::
 app = Flask(__name__,template_folder='templates',static_url_path='/xxxxxxxx')