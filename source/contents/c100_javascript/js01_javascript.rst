========================
1. JavaScript 数据类型
========================

JS 由三部分组成：

- ECMAScript：基础语法（数据类型、运算符、函数。。。。）
- BOM（浏览器对象模型）：window、location、history、navigator。。。
- DOM（文档对象模型）：div、p、span。。。



1. 数据类型
--------------

- 原始类型：number、string、boolean、null、undefined
- object ： Function、Array、Date、Regx ...

.. note::

 如果变量未声明，获取该变量的值，是会产生**语法错误**，而不是undefined

 一个变量声明，但未赋值，值默认为undefined,

 一个变量声明，并且赋值了一个undefined的值

 一个**对象**中，不存在的属性的值也是undefined

2.隐式转换
--------------

类型相同，同===

类型不同，尝试类型转换和比较：
null == undefined 相等
number ==string转number 1=='1.0' //true
boolean ==? 转number 1==true //true
object ==number | string 尝试对象转为基本类型 new String('hi') == 'hi' //true
其他：false

3.包对象
-----------

创建对象

::

 var student = {
     name:"test",
     grade:"5",
     say:function(){
         console.log("Hello World")
     },
     run:function(speed){
         console.log("正在以"+speed+"米/秒的速度奔跑！")
     }
 }

对象是键值对的集合：对象是由属性和方法构成；ps：对象皆属性，方法也是属性

对象属性操作
1. 获取属性：

.. note::

 student.name           # 获取到属性的值
 student.say            # 获取一个函数

 student["name"]        # 等价于students.name
 student["say"]         # 等价于student.say

**.** 语法更方便，但是有局限性

- **.** 后面不能使用js中的关键字、保留字（class、this、function...）
- **.** 后面不能使用数字

**[]** 使用更广泛

- student[变量名]
- ["class"]、["this"] 都可以随意使用  
- [0]、[2] 也可以使用       // obj[3]=obj["3"]
- 甚至可以这样使用["[object Array]"]    //jquery中有这样的实现
- 也可以这样用["{abc}"]   

2.设置属性

student["gender"] = "男" 等价于 student.gender="男"

含义：
    如果student对象中没有gender属性，就添加一个gender属性，
    如果student对象中有gender属性，就修改gender属性的值

3.删除属性

delete student["gender"]

delete student.gender  

可以删除对象中属性，不能删除变量  var a = 100; delete a; 是错误的

清空对象
person = {};     // person对象不在具有任何属性
person = null;  //表示将person 变量的值赋值为null,从此person不在是一个对象

通过构造函数创建对象

::
 
 function Person(name,age){
     this.name = name
     this.age = age
 }

 p1 = new Person("张三",18)

 var xiaoming = new Object() ==> var xiaoming = {}
 var now = new Date()
 var rooms = new Array(1,2,3) ==> var rooms = [1,2,3]
 var isMale = /123/; ==> var isMale = new RegExp("123");

Object、Date、Array 都是内置构造函数

构造函数的概念
任何函数都可以当作构造函数
只要把一个函数通过new 的方式来调用，就把这次函数的调用方式称为构造函数的调用

构造函数的执行过程
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 var p1 = new Person();

1. 创建一个对象(把这个对象称之为Person构造函数的实例_p1)
#. 创建一个内部对象，this,将this指向该实例(_p1)
#. 执行函数内部代码,其中,操作this的部分就是操作了该实例(_p1)
#. 返回值:
    - 如果函数没有返回值,就返回p1
    - 如果函数返回了一个基本数据类型的值,那么本次构造函数的返回值就是该实例(_p1)
    - 如果函数返回了一个复杂数据类型的值,那么本次构造函数的返回值就是该值

::

 function fn3(){
     return [1,3,5];
     // 数组是一个对象类型的值；
     // 所以数组是一个复杂数据类型的值,
     // -> 本次构造函数的真正返回值就是该数组
     // -> f3不再是fn3构造函数的实例
 } 
 var f3 = new fn3();

.. note::

    什么数据是复杂数据类型：除了5个基本数据类型外的都为复杂数据类型

如何判断一个对象是否是某个构造函数的实例？

::

 console.log(p1 instanceof Person) // true,就是Person的实例

 xx.__proto__属性,也是对象,该对象中一般都会有一个constructor属性,如果指向ppp函数,那么就可以认为:xxx是ppp构造函数的实例;


.. note::

 typeof 运算符,只能判断:数字、字符串、布尔值、undefined、函数 ;
 
 typeof 不能判断对象的构造函数

 typeof null === "object"

 typeof {} === "object"

 typeof [] === "object"
 
 typeof function(){} === "function"


|image1|

str 是基本类型，strObj是对象类型，是sting类型对应的包装类


|image2|


::

 var a = "string";
 alert(a.length);//6
 a.t = 3;
 alert(a.t);//undefined

4.类型检测
-----------------

+ typeof
+ instanceof
+ Object.prototype.toString
+ constructor
+ duck type

|image3|

obj instanceof Object

|image4|
|image5|

|image6|


练习
------

请在index.html文件中，编写arraysSimilar函数，实现判断传入的两个数组是否相似。具体需求：

1. 数组中的成员类型相同，顺序可以不同。例如[1, true] 与 [false, 2]是相似的。

2. 数组的长度一致。

3. 类型的判断范围，需要区分:String, Boolean, Number, undefined, null, 函数，日期, window.

当以上全部满足，则返回"判定结果:通过"，否则返回"判定结果:不通过"。

::

 function arraySimialr(arr1,arr2){
    //判断边界
    if(!(arr1 instanceof Array)) || !(arr2 instanceof Array){
    return false;
    }
    //判断长度
    if(arr1.length 1== arr2.length) return false;

    var i = 0,
        n = arr1.length,
        countMap1 = {},
        countMap2 = {},
        t1,t2,
        TYPES = ['String','boolean','number','undefined','null','function','date','window'];

    for (;i<n;i++){
        t1 = typeOf(arr1[i]);
        t2 = typeOf(arr2[i]);
        if (countMap1[t1]){
            countMap1[t1]++;
        }else{
            countMap1[t1] = 1;
        }
        if (countMap2[t2]){
            countMap2[t2]++;
        }else{
            countMap2[t2] = 1;
        }
    }

    function typeOf(else){
        var r;
        if (else ==null) r = 'null';
        else if (else instanceof Array) r = 'array';
        else if (else ==window) r = 'window';
        else if (else instanceof Date) r = 'date';
        else r = typeof else;
        return r;
    }

    for (i =0,n=TYPES.length;i<n;i++){
        if (countMap1[TYPES[i]] !== countMap2[TYPES[i]]){
            return false;
        }
    }
    return true;
 }

表达式
---------

|image7|
|image8|
|image9|

调用表达式 func();
对象创建表达式 new Func(1,2); new Object;

|image10|

运算符
----------

|image11|
|image12|
|image13|

::

 window.x = 1
 'x' in window;//treu

 {} instanceof Object;//true
 typeof 100 === 'number';//true

|image14|

this运算符

|image15|

总结特殊运算符
------------------

|image16|















.. |image1| image:: ./img/20181228151757.png
.. |image2| image:: ./img/20181228152702.png
.. |image3| image:: ./img/20181228153311.png
.. |image4| image:: ./img/20181228170519.png
.. |image5| image:: ./img/20181228170653.png
.. |image6| image:: ./img/20181228171103.png
.. |image7| image:: ./img/20181229083516.png
.. |image8| image:: ./img/20181229083720.png
.. |image9| image:: ./img/20181229083818.png
.. |image10| image:: ./img/20181229090635.png
.. |image11| image:: ./img/20181229091012.png
.. |image12| image:: ./img/20181229091848.png
.. |image13| image:: ./img/20181229100108.png
.. |image14| image:: ./img/20181229100433.png
.. |image15| image:: ./img/20181229100546.png
.. |image16| image:: ./img/20181229100827.png
