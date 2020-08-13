=======================
7. Promise
=======================

为什么出现Promise
========================

在javascript开发过程中，代码是单线程执行的，同步操作，彼此之间不会等待，这可以说是它的优势，但是也有它的弊端，如一些网络操作，浏览器事件，文件等操作等，都必须异步执行，针对这些情况，起初的操作都是使用回调函数实现

.. code-block:: javascript

    function One(callback){
        if (success){
            callback(err,result);
        }else{
            callback(err,null);
        }
    }
    One(function(err,result){
        //执行完One函数内的内容，成功的结果回调回来向下执行
    })

上述代码只是一层级回调，如果代码复杂后，会出现多层级的回调，代码可读性也会很差，那有没有一种方式，不用考虑里面的内容，直接根据结果成功还是失败执行下面的代码呢？有的，Promise（承诺），在ES6中对Promise进行了同意的规范。

Promise的含义
========================

- Promise 是异步编程的一种解决方案，比传统的解决方案–回调函数和事件－－更合理和更强大。它由社区最早提出和实现，ES6将其写进了语言标准，统一了语法，原生提供了Promise

- 所谓Promise ，简单说就是一个容器，里面保存着某个未来才回结束的事件(通常是一个异步操作）的结果。从语法上说，Promise是一个对象，从它可以获取异步操作的消息。 Promise 对象的状态不受外界影响

- Promise是回调函数可以规范的链式调用

.. note::

    PS：一个函数如果首字母定义为大写，一般把这个函数当作构造函数

Promise原理与讲解
===========================

原理
>>>>>>>>>>>>>>>

- Promise的三种状态

    - pending：进行中
    - fulfilled :执行成功
    - rejected ：执行失败

注意Promise在某一时刻只能处于一种状态

- Promise的状态改变

    - pending------》fulfilled（resolved）
    - pending------》rejected

Promise的状态改变，状态只能由pending转换为rejected或者rejected，一旦状态改变完成后将无法改变（不可逆性）


- 在Promise中，有两个函数，分别是resolve（）成功之后的回调函数，reject（）失败之后的回调函数

-  在Promise构造函数prototype属性上，有一个.then() 方法，也就是说，只要Promise构造函数创建的实例，都可以访问到.then()方法

- Promise表示一个异步操作，每new一个Promise实例，这个实例就表示一个具体的异步操作

- Promise的实例是一个异步操作，内部拿到操作结果后无法使用return把操作结果返回给调用者；这个时候，只能使用回调函数的形式来把成功或失败的结果返回给调用者

- 在new 出来的Promise实例上，调用.then()方法，预先为这个Promise异步操作，指定成功(resolve)和失败(reject)的回调函数

- Prmoise一被创建就立即执行

Promise的使用

.. literalinclude:: ./code/read_file.js
    :encoding: utf-8
    :language: javascript
    :emphasize-lines: 15,24
    :linenos:

Prmise解决回调地狱

.. literalinclude:: ./code/使用Promise解决回调地狱.js
    :encoding: utf-8
    :language: javascript
    :emphasize-lines: 21-23
    :linenos:


如果前面的任何promise执行失败，则立即终止所有promise的执行

.. literalinclude:: ./code/promise异常处理.js
    :encoding: utf-8
    :language: javascript
    :emphasize-lines: 27,28
    :linenos:

.. note::

    如果前面的Promise执行失败，不想后续的Promise操作被终止，可以为每个promise指定失败的回调

Promise中Ajaxs使用Promise指定成功的回调函数

.. literalinclude:: ./code/演示jquery中的Promise.html
    :encoding: utf-8
    :language: html
    :emphasize-lines: 27,28
    :linenos:

- vs code 中 *shift* + *ctrl* + *p*  选择 Express: Host Current Workspace

- http\:\/\/localhost\/演示jquery中的Promise.html
