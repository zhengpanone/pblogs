======================================
5. JavaScript 闭包
======================================

变量作用域
=======================

- 概念：一个变量可以使用的范围
- js中首先有一个最外层的作用域：全局作用域
- 通过函数创建一个独立的作用域，其中函数可以嵌套，作用域也可以嵌套

函数执行时，首先找到函数内部所有的变量、函数声明、把他们放在作用域中、给变量一个初始值underfined **变量可以访问** 。逐条执行代码，在执行代码的过程中，如果有赋值语句，对变量进行赋值

作用域链
========================

- 作用域相对变量，如果存在多级作用域1，这个变量又来自哪里？我们把这个变量查找的过程称之为变量的作用域链
- 意义： 查找变量，确定变量来自于哪里，变量是否可以访问


.. code:: js

 function fn(callback){
     var age = 18;
     callback()
 }

 fn(function(){
     console.log(age);
     //var age = 15;
     // 看上一级作用域，不是看函数在哪里调用，而是看函数在哪里编写，
     //因为这种特别，通常会把作用域说成是：此法作用域

 })

.. code:: 

 <body>
    <div>1</div>
    <div>22</div>
    <div>333</div>
    <div>4444</div>
    <div>55555</div>
 </body>
 <script>
    var divs = document.getElementByTagName("div")
    for(var i=0; i<divs.length;i++){
        const element = divs[i];
        element.onclick=function(){
            alert(i)
            // 弹出的是5
            // i 是来自全局作用域，执行完for循环后，i的值已经变成了5
        }
    }
    // 如何打印对应的i，闭包的解决方案
    for(var i=0;i<divs.length;i++){
        const element = divs[i];
        element.onclick=(function(j){
            return function(){
                alert(j)
            }
        })(i);
    }
 </script>


闭包
==================================

.. code:: 

 <script>
    function fn(){
        var a=5;
        return function(){
            a++;
            console.log(a);
        }
    }
    var f1=fn();    //f1指向匿名函数
    f1();           //6
    f1();           //7
    f1();           //8
    //代码执行到fn函数完毕，返回匿名函数
    // 一般认为函数执行完毕，变量就会释放，但是此时由于js引擎发现匿名函数要使用a变量，
    //所有a变量并不能得到释放，而是把a变量放在匿名函数可以访问到的地方
    // a变量存在于f1函数可以访问到的地方，当然此时a变量只能被f1函数访问

 </script>


.. code:: 

 <script>
    function fn(){
        var a=5;
        return function(){
            a++;
            console.log(a);
        }
    }
    var f1=fn();    //f1指向匿名函数
    f1();           //6
    var f2=fn();
    f2();           //6
    var f3=fn();
    f3();           //6
    //代码执行到fn函数完毕，返回匿名函数
    // 一般认为函数执行完毕，变量就会释放，但是此时由于js引擎发现匿名函数要使用a变量，
    //所有a变量并不能得到释放，而是把a变量放在匿名函数可以访问到的地方
    // a变量存在于f1函数可以访问到的地方，当然此时a变量只能被f1函数访问

 </script>

闭包的应用
>>>>>>>>>>>>>>>>>>>>

.. code::  

 <script>

 // 模块化开发
    var ktv=(function KTV(){
        // 保护leastPrice变量，将他放在函数内部
        var leastPrice=1000;

        var total=0;
        return{
            //购物
            buy:function(price){
                total+=price;
            },
            pay:function(){
                if(total<leastPrice){
                    console.log("请继续购物")
                }else{
                    console.log("欢迎下次光临")
                }
            },
            editLeast:function(id,price){
                if(id===888){
                    leastPrice=price;
                    console.log("现在最低消费"+price);
                }else{
                    console.log("权限不足");
                }
            }
        }
    })();
 
    
 </script>


闭包的问题
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

函数执行完毕后,作用域中保留了最新的变量值

闭包应用场景
>>>>>>>>>>>>>>>>>>>>>>>>>>

- 模块化
- 防止变量被破坏

闭包内存释放问题
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code:: html 

 function f1(){
     var a=5;
     return function(){
         a++;
         console.log(a);
     }
 }

 var q1=f1();
 // 要想释放q1里面保存的a,只能通过释放q1
 q1=null;   //q1=undefined


函数的4种调用方式
============================================

1. 函数调用 [1]_

#. 方法调用 [2]_

#. new调用(构造函数) [3]_

#. 上下文方式(call、apply、bind) [4]_

**在ES6的箭头函数之前的时代,想要判断一个函数内部的this指向谁,就是根据上面的四种方式来决定的**

.. [1]

1. 函数调用 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


.. literalinclude:: ./code/js05/01.函数调用.html
    :encoding: utf-8
    :language: html
    :lines: 10-20
    :emphasize-lines: 9,10
    :linenos:

.. [2]

2. 方法调用
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/02.方法调用.html
    :encoding: utf-8
    :language: html
    :lines: 10-19
    :emphasize-lines: 9
    :linenos:

.. [3]

3. new调用(构造函数)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/03.new调用.html
    :encoding: utf-8
    :language: html
    :lines: 10-19
    :emphasize-lines: 9
    :linenos:

.. [4]

4. 上下文方式(call、apply、bind)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/04.上下文方式.html
    :encoding: utf-8
    :language: html
    :lines: 10-20
    :emphasize-lines: 9
    :linenos:


this的指向
======================================

window对象中的方法都是全局函数;
window对象中的属性都是全局变量

1. 函数调用:函数内部的this指向window
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/05.函数调用-this的指向.html
    :encoding: utf-8
    :language: html
    :lines: 10-40
    :emphasize-lines: 9
    :linenos:

2. 方法调用:函数内部的this指向调用该方法的对象
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/05.方法调用-this的指向.html
    :encoding: utf-8
    :language: html
    :lines: 10-36
    :emphasize-lines: 9
    :linenos:

3. 构造函数调用:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/05.构造函数调用-this的指向.html
    :encoding: utf-8
    :language: html
    :lines: 10-36
    :emphasize-lines: 9
    :linenos:

.. literalinclude:: ./code/js05/05.构造函数调用-this的指向_2.html
    :encoding: utf-8
    :language: html
    :lines: 15-49
    :emphasize-lines: 9
    :linenos:

4. 上下文调用:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/js05/05.上下文调用方式.html
    :encoding: utf-8
    :language: html
    :lines: 10-22
    :emphasize-lines: 9
    :linenos:

call 方法的第一个参数：

    如果是对象类型,那个函数内部的this指向该对象

    如果是undefined，null，那么函数内部的this指向window

    如果是数字,this 对应Number构造函数的实例  --> new Number(1)
    
    如果是字符串,this对应String构造函数的实例 --> new String("abc")

    如果是布尔值,this对应Boolen构造函数的实例 --> new Boolean(false)

call 和apply的异同
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

call和apply都可以改变函数内部的this的值
传参的形式不同

.. literalinclude:: ./code/js05/05.call和apply异同.html
    :encoding: utf-8
    :language: html
    :lines: 10-17
    :emphasize-lines: 3
    :linenos:

bind基本用法

.. literalinclude:: ./code/js05/05.bind基本用法.html
    :encoding: utf-8
    :language: html
    :lines: 10-41
    :emphasize-lines: 9
    :linenos:

.. literalinclude:: ./code/js05/05.上下文调用bind.html
    :encoding: utf-8
    :language: html
    :lines: 10-41
    :emphasize-lines: 9
    :linenos:

call、apply是立刻执行函数,并且在执行过程中绑定了this的值
bind 并没有立刻执行这个函数,而是创建一个新函数,新函数绑定了this的值


如何解决bind的浏览器兼容性问题？
=========================================


es6内容
========================

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

