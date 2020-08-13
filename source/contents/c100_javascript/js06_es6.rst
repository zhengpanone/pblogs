==================================
6 ES6
==================================

let
====================

声明的变量只在let命令所在的代码块内有效，用于定义变量

.. code-block:: javascript
    :linenos:

    {
     let a = 10;
     var b = 1;
    }

>>> a // a is not defined.
>>> b // 1

上面代码在代码块之中，分别用let和var声明了两个变量。然后在代码块之外调用这两个变量，结果let声明的变量报错，var声明的变量返回了正确的值。这表明，let声明的变量只在它所在的代码块有效。

for循环的计数器，就很合适使用let命令。

.. code-block:: javascript
    :linenos:

    for (let i =0; i < 10; i++){
        // ...
    }
    console.log(i);
    //  ReferenceError: i is not defined

上面代码中，计数器i只在for循环体内有效，在循环体外引用就会报错。

下面的代码如果使用var，最后输出的是10。

.. code-block:: javascript
    :linenos:

    var a = [];
    for(var i = 0; i < 10; i++){
        a[i] = function(){
            console.log(i);
        }
    }
    a[6](); // 10

上面代码中，变量i是var命令声明的，在全局范围内都有效，所以全局只有一个变量i。每一次循环，变量i的值都会发生改变，而循环内被赋给数组a的函数内部的console.log(i)，里面的i指向的就是全局的i。也就是说，所有数组a的成员里面的i，指向的都是同一个i，导致运行时输出的是最后一轮的i的值，也就是 10。

如果使用let，声明的变量仅在块级作用域内有效，最后输出的是 6。

.. code-block:: javascript
    :linenos:

    var a = [];
    for(let i = 0; i < 10; i++){
        a[i] = function(){
            console.log(i);
        }
    }
    a[6](); // 6


const
=================

用于定义常量


结构赋值
========================


属性的简写
======================

.. code-block:: javascript
    :linenos:

    var a = 3;
    var c = 10;
    var b = { a, c }
    console.log(b) // {a: 3, c: 10}

函数的扩展
=============================

rest参数
>>>>>>>>>>>>>>>>>>>>>>>>



箭头函数
>>>>>>>>>>>>>>>>>>>>>>>>>>




