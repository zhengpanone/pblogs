===========================
1. 栈、队列的实现
===========================

栈
=============

定义：栈(Stack)是限制插入和删除操作只能在一个位置进行的表，该位置是表的末端，称为栈的顶(top)。栈的基本操作有PUSH(入栈)和POP(出栈)。栈又被称为LIFO(后入先出)表。

实现：

.. code:: python

 class Stack(object):
    def __init__(self):
        self.stack = []


队列
=============

定义：队列(queue)也是表，使用队列时插入和删除在不同的端进行。队列的基本操作是Enqueue(入队)，在表的末端(rear)插入一个元素，还有出列(Dequeue)，删除表开头的元素。

实现：

.. code:: python

 class Queue(object):
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError,'queue is empty'

    def size(self):
        reutrn len(self.queue)

    