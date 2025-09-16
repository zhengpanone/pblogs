=========================
itertools模块
=========================

``itertools`` 是 Python 标准库中一个专门用于操作迭代器的模块，提供了高效的迭代器生成函数。

模块核心功能分类
=========================

``itertools`` 的能力可以分为三大类：

.. list-table::
  :header-rows: 1
  :widths: 20,80,30

  * - 功能类别
    - 代表方法
    - 主要作用
  * - 无限迭代器
    - count(), cycle(), repeat()
    - 生成无限流
  * - 组合迭代器
    - product(), permutations(), combinations(), combinations_with_replacement()
    - 排列组合
  * - 过滤与切片
    - islice(), compress(), dropwhile(), takewhile(), filterfalse()
    - 按条件取数据
  * - 聚合与分组
    - accumulate(), groupby(), tee(), chain(), zip_longest()
    - 数据聚合与拆分

无限迭代器
=========================

count
-------------------------

生成不间断的 ID
>>>>>>>>>>>>>>>>>

.. code-block:: python

  from itertools import count

  order_id = count(start=1001, step=1)  # 从 1001 开始，每次+1
  
  for _ in range(5):
    id = next(order_id)
    print(id)
      
适合用于模拟数据库自增 ID 或批量编号。

cycle
-------------------------

循环播放任务
>>>>>>>>>>>>>>>>>

.. code-block:: python

  from itertools import cycle

  tasks = ["下载", "解压", "处理", "上传"]
  for i, task in zip(range(8), cycle(tasks)):
    print(f"Step {i+1}: {task}")

可以用在轮询任务调度、重复播放等场景。

product
-------------------------

排列组合：密码字典生成
>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python

  from itertools import product

  charset = "abc"
  for p in product(charset, repeat=3):
    print("".join(p))

.. code-block:: console

  aaa
  aab
  aac
  ...


在安全测试、验证码爆破、排列组合问题中很常用。


用于求多个可迭代对象的笛卡尔积(Cartesian Product)，它跟嵌套的 for 循环等价.即: 

>>> product(A, B) 等价于 ((x,y) for x in A for y in B)

它的一般使用形式如下：

>>> itertools.product(*iterables, repeat=1)

iterables是可迭代对象,repeat指定iterable重复几次,即:

>>> product(A,repeat=3) # 等价于product(A,A,A)

从 3 个数字列表中，寻找是否存在和为 12 的 3 个数

.. code-block:: python
    
  def find_twelve(num_list1, num_list2, num_list3):
  """
  从 3 个数字列表中，寻找是否存在和为 12 的 3 个数
  """
  for num1 in num1_list1:
    for num2 in num_list2:
      for num3 in num_list3:
        if num1+ num2 + num3 == 12:
          return num1, num2,num3 

对于这种需要嵌套遍历多个对象的多层循环代码，我们可以使用 product() 函数来优化它。product() 可以接收多个可迭代对象，然后根据它们的笛卡尔积不断生成结果。

.. code-block:: python
    
  from itertools import product

  def find_twelve_v2(num_list1, num_list2, num_list3):
    for num1, num2, num3 in product(num1_list1, num_list2, num_list3):
      if num1 + num2 + num3 == 12:
        return num1, num2, num3

islice
-----------

按条件截取数据
>>>>>>>>>>>>>>>>>

.. code-block:: python

  from itertools import islice

  data = range(100)
  for num in islice(data, 10, 20):  # 截取下标 10~19
      print(num)

islice()实现循环内隔行处理
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

islice(seq,start,end,step) 函数和数组切片操作（ list[start:stop:step] ）有着几乎一模一样的参数。如果需要在循环内部进行隔行处理的话，只要设置第三个递进步长参数 step 值为 2 即可（默认为 1）。

有一份包含 Reddit 帖子标题的外部数据文件，里面的内容格式是这样的：

.. code-block:: pycon
  
  python-guide: Python best practices guidebook, written for humans.
  ---
  Python 2 Death Clock
  ---
  Run any Python Script with an Alexa Voice Command
  ---
  <... ...>

我们需要获取文件里所有的标题列表，所以在遍历文件内容的过程中，必须跳过这些无意义的分隔符。

.. code-block:: python
    
  def parse_titles(filename):
    """
    
    """
    with open(filename, 'r') as fp:
      for i, line in enumerate(fp):
        if i%2 == 0:
          yield line.strip()
  
使用islice()修改

.. code-block:: python
    
  from itertools import islice

  def parse_titles_v2(filename):
    with open(filename, 'r') as fp:
      for line in islice(fp, 0 None, 2):
        yield line.strip()

groupby
-----------

分组统计（按首字母分组）
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python

  from itertools import groupby

  words = ["apple", "apricot", "banana", "blueberry", "cherry"]
  for k, g in groupby(sorted(words), key=lambda x: x[0]):
      print(k, list(g))
  

// TODO 未完
https://mp.weixin.qq.com/s/7Rq7MLfga9RIth7IMjKCaQ



combinations
======================

.. code-block:: python
    

    from itertools import combinations
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for game in combinations(teams, 2):
        print game

    >>> ( Packers ,  49ers )
    >>> ( Packers ,  Ravens )
    >>> ( Packers ,  Patriots )
    >>> ( 49ers ,  Ravens )
    >>> ( 49ers ,  Patriots )
    >>> ( Ravens ,  Patriots )




takewhile  替代 break 语句
=============================

takewhile(predicate,iterable)会在迭代 iterable 的过程中不断使用当前对象作为参数调用 predicate 函数并测试返回结果，如果函数返回值为真，则生成当前对象，循环继续。否则立即中断当前循环。


.. code-block:: python
    

    from itertools import takewhile

    for user in takewhile(is_qualified ,users):
        pass



https://mp.weixin.qq.com/s?__biz=Mzg2NjExNDI0MQ==&mid=2247483669&idx=1&sn=f1fde152bfc7a8a606967b18824f42dc&chksm=ce4e8ebbf93907adabff31678bbf92d3a47c4708cd6b1a232dc74064005a6118b775867fc008&scene=21#wechat_redirect


