========================================
12.2 观察者模式（Observer）
========================================

概述
========================================

观察者模式（有时又被称为模型-视图（View）模式、源-收听者(Listener)模式或从属者模式）是软件设计模式的一种。在此种模式中，一个目标物件管理所有相依于它的观察者物件，并且在它本身的状态改变时主动发出通知。这通常透过呼叫各观察者所提供的方法来实现。此种模式通常被用来实现事件处理系统。


定义
========================================

定义：对象间的一对多的依赖关系，当一个对象的状态发生改变时，所有依赖它的对象都得到通知并自动刷新
这种模式都是类与类之间的关系，不涉及继承，Observer类似于邮件订阅和RSS订阅，关系图如下： |image0|

这些类的作用：MySubject类就是主对象，Observer1和Observer2是依赖MySubject对象，当MySubject变化时，ObServer1和ObServer2必然变化。AbstractSubject类中定义着需要监控的对象列表，可以对其进行修改：增加或删除被监控对象，当MySubject变化时，负责通知在列表内存在的对象。


Java实现代码：
========================================

一个Observer接口：

.. code:: java

 public interface Observer{

    public void update();
 }

两个实现类：

::

 public class Observer1 implements Observer{
    
    @Override
    public void update(){

        System.out.println("observer1 has received!");
    }

 }

::

 public class Observer2 implements Observer{
 
    @Override
    public void update(){

        System.out.println('observer2 has received!')
    }
 
 }

Subject 接口及实现类：

.. code:: java

 public interface Subject{
    
    /**增加观察者**/
    public void add(Observer observer);

    /**删除观察者**/
    public void del(Observer observer);

    /**通知所有观察者**/
    public void notifyObservers();

    /**自身操作**/
    public void operation();

::

 public abstract class AbstractSubject implements Subject{
 
    private Vector<Observer> vector = new Vector<Observer>();

    @Override
    public void add(Observer observer){

        vector.add(observer)
    }

    @Override
    public void del(Observer observer){

        vector.remove(observer)
    }

    @Override
    public void notifyObservers(){

        Enumeration<Observer> enumo = vector.elements();

        while(enumo.hasMoreElements()){

            enumo.nextElement().update();
        }
    }
 
 }

::

 public class MySubject extends AbstractSubject{
    
    @Override
    public void operation(){

        System.out.println("update self!")

        notifyObservers();
    }
 }

测试类

.. code:: java

 public class ObserverTest{
    
    public static void main(String[] args){

        Subject sub = new MySubject();
        
        sub.add(new Observer1);
        sub.add(new Observer2);
        sub.operation();
    }
 }

输出：

 ::

 >>> update self!
 >>> observer1 has received
 >>> observer2 has received


Python 实现代码：
========================================

|image0|

 



 
 






.. |image0| image:: ./img/2.jpg



