SHOW DATABASES [LIKE 'PATTERN']; # 显示所有的数据库

USE databasename; # 选择数据库

CREATE DATABASE [if not exists] 数据库名 数据库选项  # 创建数据库
    数据库选项
        CHARACTER SET charset_name
        COLLATE collation_name

SELECT DATABASE(); # 查看当前数据库

SELECT now(), user(), version(); # 显示当前时间、用户、数据库版本

SHOW TABLES; # 查看数据库中的所有表

SHOW CREATE TABLE 表名\G; # 查看创建SQL

desc 表名;  # 查看表字段




