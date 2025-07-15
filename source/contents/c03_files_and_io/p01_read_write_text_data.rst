=======================
文件处理
=======================

- r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
- rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
- r+	打开一个文件用于读写。文件指针将会放在文件的开头。
- rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
- w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
- ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
- a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
- ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。


读文件

.. code-block:: python

  f = open('/opt/work/user/zhengpanone/test.txt','r')

标识符'r',标识只读;
如果文件不存在,open()函数会抛出异常IOError的错误

.. code-block:: pycon

 >>> f=open('/Users/michael/notfound.txt', 'r')
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

如果文件打开成功,调用read()方法可以一次读取文件全部内容,python把文件内容读到内存,用一个str对象表示：


 >>> f.read()
 >>> 'hello python!'

最后一步调用close()方法关闭文件。文件使用完毕必须关闭,因为文件对象会占用系统资源,且操作系统同时能打开的文件数量也是有限的：

 >>> f.close()

由于文件读写都有可能产生IOError,一旦文件出错,后面的f.close就不会调用。所以,为了保证无论是否出错都能正确的关闭文件,使用try... finally 实现：

.. code-block:: python

  try:
    f = open('path/file','r')
    print(f.read())
  finally:
    if f:
        f.close()


使用with 读写文件

.. code-block:: python

  with open('path/file','r') as f, open('path/file2','w') ad f2:
    for l in a:
      f2.write(l.readline())


