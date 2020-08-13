====================================================
Tornado 源码分析 异步上下文管理（StackContext）
====================================================


https://www.jianshu.com/p/3e58f977b908

异步函数执行的时候，抛出的异常已经和主函数的上下文不一致，为了解决这个问题，可以使用Python的上下文管理器进行wrapper。下面的代码，就存在异步异常在主函数中无法捕获的问题：

.. code-block:: python
    :emphasize-lines: 1,2
    :linenos:
    

    import tornado.ioloop
    import tornado.stack_context

    ioloop = tornado.ioloop.IOLoop.instance()


