=====================
3. 配置文件
=====================

::
 
 # 方式一
 app.config['DEBUG'] = True
 ps：由于Config 对象本质上是字典，所以还可以使用app.config.update(...)

 # 方式二
 app.config.from_pyfile('python 文件名称')
 如：
    setting.py
        DEBUG = True
    app.config.from_pyfile('setting.py')

 app.config.from_envvar("环境变量名称")
    环境变量的值为python 文件名称，内部调用from_pyfile方法

 app.config.from_json('json文件名称')
    JSON 文件名称，必须是json格式，因为内部会执行json.loads

 app.config.from_mapping({'DEBUG':True})
    字典格式

 app.config.from_object('python类或类路径')
    app.config.from_object('pro_flask.settings.TestingConfig')
    setting.py

        class Config(object):
            DEBUG = False
            TESTING = False
            DATABASE_URL = 'sqlite://memory:'
        
        class ProductionConfig(Config):
            DATABASE_URL = 'mysql://user@localhsot/foo'

        class DevelopmentConfig(Config):
            DEBUG = True
        
        class TestingConfig(Config):
            TESTING = True

    PS：从sys.path 中已经存在路径开始写
 PS: setting.py 文件默认路径要存放再程序root_path 目录，如果instance_relative_config 为True,则就是instance_path目录