========================
20.4 路由系统
========================

1. 可传入参数
========================

::
 
 @app.route('/user/<username>')     # 常用的   不加参数时默认字符串形式
 @app.route('/post/<int：post_id>')     # 常用的    指定int 说明是整型
 @app.route('/post/<float:post_id>')
 @app.route('/post/<path:path>')
 @app.route('/login', methods=['GET', 'POST'])


::

 DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
 }

2. 反向生成URL:url_for
============================================

endpoint("name")   #别名，相当于django中的name

::

 from flask import Flask,url_for

 @app.route('/index', endpoint='xxx')   # endpoint是别名
 def index():
    v = url_for('xxx')
    print(v)
    return 'index'

 @app.route('zzz/<int:nid>',endpoint='aaa')
 def zzz(nid):
    v = url_for('aaa',nid=nid)
    print(v)
    return 'index2'

3. @app.route 和 app.add_url_rule 参数
===============================================================

::

 @app.route 和 app.add_url_rule 参数
        rule,                                               URL规则
        view_func,                                      视图函数名称
        defaults=None,                              默认值，当URL中无参数，函数需要参数是，使用defaults={k:v} 为函数提供参数
        endpoint=None,                            名称，用于反向生成URL，即： url_for('名称')
        methods=None,                            允许的请求方式，如：["GET","POST"]

        strict_slashes=None,                      对URL最后的 / 符号是否严格要求，
                                                                如：
                                                                @app.route('/index',strict_slashes=False)，　#当为False时，url上加不加斜杠都行
                                                                访问 http://www.xx.com/index/ 或 http://www.xx.com/index均可
                                                                @app.route('/index',strict_slashes=True)　　#当为True时，url后面必须不加斜杠
                                                                仅访问 http://www.xx.com/index 
        redirect_to=None,                           由原地址直接重定向到指定地址，原url有参数时，跳转到的新url也得传参，注意：新url中不用指定参数类型，直接用旧的参数的类型
                                                                如：
                                                                @app.route('/index/<int:nid>', redirect_to='/home/<nid>') # 访问index时，会直接自动跳转到home，执行home的函数，
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　不执行index的
                                            
　　　　　　　　　　　　　　　　　　　　　　　　　　或
                                                                def func(adapter, nid):
                                                                return "/home/888"
                                                                @app.route('/index/<int:nid>', redirect_to=func)

        subdomain=None,                         子域名访问
                                                                from flask import Flask, views, url_for

                                                                app = Flask(import_name=__name__)
                                                                app.config['SERVER_NAME'] = 'haiyan.com:5000'


                                                                @app.route("/", subdomain="admin")
                                                                def static_index():
                                                                """Flask supports static subdomains
                                                                This is available at static.your-domain.tld"""
                                                                
                                                                    return "admin.xxx.com"

　　　　　　　　　　　　　　　　　　　　　　　　　　　　#动态生成
                                                                @app.route("/dynamic", subdomain="<username>")
                                                                def username_index(username):
                                                                    """Dynamic subdomains are also supported
                                                                    Try going to user1.your-domain.tld/dynamic"""
                                                                    return username + ".your-domain.tld"


                                                                if __name__ == '__main__':
                                                                    app.run()
            所有的域名都得与IP做一个域名解析：
　　　　　　　　如果你想通过域名去访问，有两种解决方式：
　　　　　　　　　　方式一：
　　　　　　　　　　　　1、租一个域名   haiyan.lalala
　　　　　　　　　　　　2、租一个公网IP  49.8.5.62
　　　　　　　　　　　　3、域名解析：haiyan.com    49.8.5.62
　　　　　　　　　　　　4、吧代码放在49.8.5.62这个服务器上，程序运行起来
　　　　　　　　　　　　　 用户可以通过IP进行访问
　　　　　　　　　　方式二：如果是自己测试用的就可以用这种方式。先在自己本地的文件中找
　　　　　　　　　　　　 C:\Windows\System32\drivers\etc  找到HOST，修改配置
　　　　　　　　　　　　然后吧域名修改成自己的本地服务器127.0.0.1
　　　　　　　　　　　　加上配置：app.config["SERVER_NAME"] = "haiyan.com:5000"


::

 # =============== 子域名访问============
 @app.route("/static_index", subdomain="admin")
 def static_index():
    return "admin.bjg.com"

 # ===========动态生成子域名===========
 @app.route("/index",subdomain='<xxxxx>')
 def index(xxxxx):
    return "%s.bjg.com" %(xxxxx,)


4.自定制正则路由匹配
============================================

扩展Flask 的路由系统，让她支持正则，这个类必须这样写，必须去继承BaseConverter

::

 from flask import Flask,url_for
 from werkzeug.routing import BaseConverter
    app = Flask(__name__)
    
    # 定义转换的类
    class RegexConverter(BaseConverter):
        '''自定义URL匹配正则表达式'''

        def __init__(self, map,regex):
            super(RegexConverter,self).__init__(map)
            self.regex = regex

        def to_python(self,value):
            '''路由匹配时匹配成功后传递给视图函数中参数的值'''
            return int(value)

        def to_url(self,value):
            '''使用url_for 反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数'''
            val = super(RegexConverter,self).to_url(value)
            return val

    # 添加到converts中
    app.url_map.converters['regex'] = RegexConverter

    # 进行使用
    @app.route('/index/<regex('\d+'):nid>',endpoint='xx')
    def index(nid):
        url_for('xx',nid=123)
        return "Index"

    if __name__ == '__main__':
        app.run()
        



                    