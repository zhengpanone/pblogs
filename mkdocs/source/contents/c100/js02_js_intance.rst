========================
2 JavaScript 继承
========================

概念
=============

通过某种方式,让一个对象可以访问到另一个对象中的属性和方法,这种方式称之为继承

为什么要使用继承
===========================

::

 function Person(name.age){
     this.name=name;
     this.age=age;
     this.say=function(){}
 }
 var p1 = new Person();
 var p2 = new Person();

 // p1对象和p2对象的say 方法是否是同一个方法:false
 console.log(p1.say ===p2.say)

 //由于say方法可能功能相似但是不是同一个方法(没有指向同一块内存,会造成内存浪费)
 // 解决方案:把say 方法写在它们共同的父对象中
 // 共同的父对象可以通过Person.prototype来获取
 Person.prototype.run=function(){
     console,log("you can run")
 }
 p1.run();
 p2.run();
 // 验证p1.run 和p2.run 是否同一个方法
 console.log(p1.run == p2.run()); //true
 console.log(p1.run == Person.prototype.run) //true
 //指向同一个方法,这种方法避免了内存浪费

.. note::

 只有往某个构造函数的prototype对象中添加某个属性、方法那么这样的属性、方法都可以被所有的构造函数的实例共享
 prototype对象称之为原型对象(构造函数的实例的原型对象)

.. note::

 Person的原型对象是谁？

 Person的构造函数是: --> Function

 Person的原型对象是: --> Function.prototype

继承实现方式
====================

原型链继承
>>>>>>>>>>>>>>>>>>>>>

::

 function Person(){

 }
 Person.prototype.s1 = function(){}
 tom = new Person();

 Person.prototype = {
     // 必须要,constructor 属性指向当前对象本身
     constructor:Person,
     a1:function(){
         console.log("Hello")
     },
     a2:function(){},
     a3:function(){},
 }
 console.log(tom.s1()); //可以访问
 console.log(tom.a1()); // undefined
 tom对象在创建的时候已经有一个确定的原型对象,就旧的Person.prototype ,由于Person.prototype后面被重新赋值,但是tom对象的原型对象却没有改变,所以tom对象不能访问到对象中的a1-a5方法

如何解决,先改变原型,重新添加新实例 ,创建实例即确定了原型
一般情况,先改变原型对象,再创建对象
对于新原型,会添加一个constructor属性,从而不破坏原有的原型对象的结构

拷贝继承(混入继承:mixin)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

场景: 有时候想使用某个对象中的属性,但是又不能直接修改它,于是就可以创建一个该对象的拷贝
实际运用:
 jquery: $.extend: 编写jquery插件的必经之路
    基于jquery封装插件

::

 var o1 = {age:2};

 var o2 = o1;
 o2.age=18;
 // 1. 修改了o2对象的age属性
 // 2. 由于o2对象跟o1对象是同一个对象
 // 3. 所以此时o1对象的age属性也被修改了
  
::

 var o3={gender:"男",grade:"初三",group:"第四组",name"张三"};
 var o4={gender:"男",grade:"初三",group:"第四组",name"李四"};
 // 这样的情况可以使用拷贝继承





es6内容
===================

+ 1、解构赋值   
+ 2、函数rest参数  
+ 3、箭头函数  
    - 箭头函数和普通函数有哪些不同？(4点)
+ 4、对象的Object.assign  
+ 5、promise 
+ 6、generator 
+ 7、async 
+ 8、class 
+ 9、module