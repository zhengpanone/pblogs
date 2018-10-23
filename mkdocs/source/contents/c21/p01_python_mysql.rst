========================
21.1 操作mysql
========================

1. 语法基础
-----------------------------------------

1.1 DDL（ 数据定义语句）
CREAT TABLE/DATABASE  创建
ALTER TABLE/DATABASE  修改
DROP TABLE/DATABASE   删除


1.2DML（数据管理语句）
INSERT  增
DELETE  删
UPATAE  改
SELECT  查

1.3 创建数据库

CREATE DATABASE `mydatabase`;
USE `mydatabase`;

1.4 查看已有的数据库
SHOW DATABASES;


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



