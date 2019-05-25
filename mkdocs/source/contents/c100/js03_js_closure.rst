======================================
3 JavaScript 闭包
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

.. code:: js

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