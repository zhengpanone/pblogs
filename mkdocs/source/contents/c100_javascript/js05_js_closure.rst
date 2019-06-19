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


闭包
==================================

.. code:: js

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


.. code:: js

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

.. code:: js 

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

函数的4种调用方式

1 函数调用
# 方法调用
# new调用(构造函数)
# 上下文方式(call、apply、bind)

**在ES6的箭头函数之前的时代,想要判断一个函数内部的this指向谁,就是根据上面的四种方式来决定的**

.. code:: js 

 var age=18;
 var p={
     age:15
     say:function(){
         console.log(this.age);
     }
 }
 var s1=p.say()
 s1();      //函数调用


.. code:: js 

 var age=18;
 var p={
     age:15
     say:function(){
         console.log(this.age);
     }
 }
 p.say()    //方法调用

.. code:: js 

 var age=18;
 var p={
     age:15
     say:function(){
         console.log(this.age);
     }
 }
 new p.say()    //构造函数调用

.. code:: js 

 var length=21;
 function f1(){
     console.log(this.length);

 }

 f1.call([1,3,5])
 f1.apply(this)
 f1.call(5)     //上下文方式

闭包内存释放问题
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code:: js 

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
 