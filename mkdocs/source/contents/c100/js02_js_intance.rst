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
 //指向同一个方法,这种方法避免了内存浪费




