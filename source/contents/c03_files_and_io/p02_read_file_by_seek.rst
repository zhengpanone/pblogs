=======================================
2. 如何读取大文件
=======================================

python 文件指针seek()操作文件

文件读写模式

- r+ 文件指针在头部, 写方式 覆盖

- w+ 文件指针在头部, 写方式 清除

- a+ 文件指针在尾部, 写方式 追加


seek(offset[,wherece])

offset 偏移量,可以是负值,代表向前移动

wherece 偏移相对位置, 分别有: os.SEEK_SET(相对文件起始位置,也可用"0"表示); os.SEEK_CUR(相对文件当前位置,也可用"1"表示);os.SEEK_END(相对文件结尾位置,可以用"2"表示)

seek(x, 0): 表示指针从开头位置移动到x个位置

seek(x, 1): 表示指针从文件当前位置向后移动x个位置

seek(-x, 2): 表示文件指针从文件结尾向前移动x个位置

在使用seek（）函数时，有时候会报错为  “io.UnsupportedOperation: can't do nonzero cur-relative seeks”， 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常。将  f=open("aaa.txt","r+")  改成

f = open("aaa.txt","rb")   就可以了

https://www.cnblogs.com/xuexizongjie/p/10674306.html