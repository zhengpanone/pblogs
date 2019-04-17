=========================
2.1 re模块操作
=========================

1. re模块操作
--------------------------

::

 import re      # 导入re模块
 result = re.match(正则表达式，要匹配的字符)
 result.group()     # 如果上一步匹配到数据，可以使用group来提取数据

**re.match是用来进行正则匹配检查的方法，若字符串匹配正则表达式，则match方法返回匹配对象（Match Object）,否则返回None（不是空字符串""）
匹配对象Match Object 具有group方法,用来返回字符串的匹配部分**

示例：

::

 import re
 result = re.match('itcast','itcast.com')
 result.group()
 >>> itcast

表示字符

|字符    功能
|.       匹配任意一个字符(除了\n)
|[]      匹配[]中列举的字符
|\d      匹配数字,即0-9
|\D      匹配非数字
|\s      匹配空白字符,即空格,tab键
|\S      匹配非空白
\w      匹配单词字符,即a-z、A-Z、0-9、_

\W      匹配非单词字符
 