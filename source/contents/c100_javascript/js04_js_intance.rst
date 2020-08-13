========================
4. JavaScript 继承
========================

概念
=============

通过某种方式,让一个对象可以访问到另一个对象中的属性和方法,这种方式称之为继承

为什么要使用继承
===========================

.. code:: js

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
     console.log("you can run")
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

1. 原型链继承
>>>>>>>>>>>>>>>>>>>>>

.. code:: js

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

2. 拷贝继承(混入继承:mixin)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- 场景: 有时候想使用某个对象中的属性,但是又不能直接修改它,于是就可以创建一个该对象的拷贝,各大框架都有拷贝继承的应用
- 实际运用:

    + jquery: $.extend: 编写jquery插件的必经之路

        + 基于jquery封装插件

.. code:: js

 var o1 = {age:2};

 var o2 = o1;
 o2.age=18;
 // 1. 修改了o2对象的age属性
 // 2. 由于o2对象跟o1对象是同一个对象
 // 3. 所以此时o1对象的age属性也被修改了
  
.. code:: js

 var o3={gender:"男",grade:"初三",group:"第四组",name"张三"};
 var o4={gender:"男",grade:"初三",group:"第四组",name"李四"};
 // 这样的情况可以使用拷贝继承

 //实现拷贝继承:
 // 1. 已经拥有o3对象
 // 2. 创建o3对象的拷贝(克隆) for (var key in o3){ o3[key]}
 // 3. 修改克隆对象,对克隆对象修改name属性

**浅拷贝和深拷贝**
深拷贝实现了递归原理,将对象的若干层属性拷贝出来
浅拷贝只拷贝一层属性

封装拷贝继承函数
>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code:: js

 function extend(source,target){
    for (var key in source){
        target[key] = source[key];
    }
 }

 var o4 = {};
 extend(o3,04);
 console.log(o4.name)

ES6中有了《对象扩展运算符》专门为拷贝继承而生:优化浅拷贝

.. code:: js 

 var source = {name:"张三",age:15};
 var target = {...source};
 var target = {...source,age:18}; //简化浅拷贝

4. 原型式继承
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- 场景：

    + 创建一个纯洁的对象：对象什么属性都没有
    + 创建一个继承自某个父对象的子对象

    .. code:: js

     var parent={age:18,gender:"男"};
     var student=Object.create(parent);
     //student.__proto__===parent

- 使用方式：

    + 空对象：Object.create(null)
    + .. code:: js

         var o1 = {say:function(){}};
         var o2 = Object.create(o1);

5. 接用构造函数实现继承
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- 场景：适用于2种构造函数之间逻辑有相似的情况
- 原理：函数的call、apply调用方式
- 局限性：父类构造函数的代码必须完全适用于子类构造函数

.. code:: js

 function Animal(name,age,gender){
     this.name=name;
     this.age=age;
     this.gender=gender;
 }
 function Person(name,age,gender,say){
     // 错误调用,这种函数调用方式,函数内部的this只能指向window
     //Animal(name,age,gender);
     // 正确方式,将Animal函数内部的this指向Person的实例
     Animal.call(this,name,age,gender);
     // 等价于:
     Animal.apply(this,[name,age,gender])
     this.say=say
 }

 var p1 = new Persion("test",18,"男",
 function(){})

- 以上代码用借用构造函数实现

.. code:: js

 function Animal(name,age){
     this.name=name;
     this.age=age;
 }


原型链
======================================

- JS里的对象可能会有父对象，父对象还有父对象
- 根本：继承

 + 属性：对象中几乎都会有一个__proto__属性,指向他的父对象
  
  - 意义：可以实现让该对象访问到父对象中相关属性

- 根对象：Object.prototype

 + var arr=[1,3,5]
 + arr.__proto__:Array.prototype
 + arr.__proto__.__proto__ 找到根对象



