==================
12.2 观察者模式（Observer）
==================

一、定义
-----------

定义：对象间的一对多的依赖关系，当一个对象的状态发生改变时，所有依赖它的对象都得到通知并自动刷新
这种模式都是类与类之间的关系，不涉及继承，Observer类似于邮件订阅和RSS订阅，关系图如下： |image0|

这些类的作用：MySubject类就是主对象，Observer1和Observer2是依赖MySubject对象，当MySubject变化时，ObServer1和ObServer2必然变化。AbstractSubject类中定义着需要监控的对象列表，可以对其进行修改：增加或删除被监控对象，当MySubject变化时，负责通知在列表内存在的对象。










.. |image0| image:: ./img/2.jpg



