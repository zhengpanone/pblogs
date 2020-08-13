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

1.5 插入数据

INSERT INTO `tablename` VALUE()

1.6 修改数据

UPATAE `tablename` SET col_name='XXX' WHERE col_id = 'XX'

1.7 删除数据

DELETE FROM `tablename` WHERE col_name = 'XXX'

1.8 其他

新建索引（CREAT INDEX）
修改表（ALTER TABLE）
删除数据库、表、索引、视图（DROP）



