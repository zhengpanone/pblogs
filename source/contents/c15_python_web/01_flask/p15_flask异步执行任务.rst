=========================
15. Flask异步执行任务
=========================

Flask 是 Python 中有名的轻量级同步 web 框架，遇到需要长时间处理的任务，此时就需要使用异步的方式来实现，让长时间任务在后台运行，先将本次请求的响应状态返回给前端，不让前端界面「卡顿」，当异步任务处理好后，如果需要返回状态，再将状态返回。

使用线程的方式
==========================

.. literalinclude:: ./code/01.threadpoolexecutor_asyn.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 10-11
    :lines: 1-
    :linenos:  

当要执行一些比较简单的耗时任务时就可以使用这种方式，如发邮件、发短信验证码等。
但这种方式有个问题，就是前端无法得知任务执行状态。
如果想要前端知道，就需要设计一些逻辑，比如将任务执行状态存储到 redis 中，通过唯一的任务 id 进行标识，然后再写一个接口，通过任务 id 去获取任务的状态，然后让前端定时去请求该接口，从而获得任务状态信息。
全部自己实现就显得有些麻烦了，而 Celery 刚好实现了这样的逻辑，来使用一下。

使用Celery
==========================

Celery 是实时任务处理与调度的分布式任务队列，它常用于 web 异步任务、定时任务等

现在我想让前端可以通过一个进度条来判断后端任务的执行情况。使用 Celery 就很容易实现，首先通过 pip 安装 Celery 与 redis，之所以要安装 redis，是因为让 Celery 选择 redis 作为「消息代理 / 消息中间件」。

::

 pip install Celery
 pip install redis

最简单的例子 example.py


.. literalinclude:: ./code/celery实现异步/example.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 7
    :lines: 1-
    :linenos:  

启动 Celery worker:

>>> celery worker -A example.celery -l INFO

启动 Web server:

>>> python example.py

多模块，更复杂的配置，更多的 task 等
================================================

::

    .
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── config.py
    │   ├── forms
    │   ├── models
    │   ├── tasks
    │   │   ├── __init__.py
    │   │   └── email.py
    │   └── views
    │   │   ├── __init__.py
    │   │   └── account.py
    ├── celery_worker.py
    ├── manage.py
    └── wsgi.py

- 项目的根目录下，有个 celery_worker.py 的文件，这个文件的作用类似于 wsgi.py，是启动 Celery worker 的入口。
- app 包里是主要业务代码，其中 tasks 里定义里一系列的 task，提供给其他模块调用。

- app/config.py

.. literalinclude:: ./code/celery实现异步/complex_celery/app/config.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 3
    :lines: 1-
    :linenos: 

BaseConfig 是整个项目用到的配置的基类，实际上还会派生出 DevelopmentConfig, StagingConfig 和 ProductionConfig 等类

- app/__init__.py

.. literalinclude:: ./code/celery实现异步/complex_celery/app/__init__.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 3
    :lines: 1-
    :linenos: 

- app/tasks/email.py 

.. literalinclude:: ./code/celery实现异步/complex_celery/app/tasks/email.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 3
    :lines: 1-
    :linenos: 

- app/views/account.py

.. literalinclude:: ./code/celery实现异步/complex_celery/app/views/account.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 3
    :lines: 1-
    :linenos: 

- ceelry_worker.py

.. literalinclude:: ./code/celery实现异步/complex_celery/celery_worker.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 3
    :lines: 1-
    :linenos:

这个 celery_worker.py 文件有两个操作：

- 创建一个 Flask 实例
- 推入 Flask application context

第一个操作很简单，其实也是初始化了 celery 实例。

第二个操作看起来有些奇怪，实际上也很好理解。如果用过 Flask 就应该知道 Flask 的 Application Context 和 Request Context. Flask 一个很重要的设计理念是：在一个 Python 进程里可以运行多个应用（application），当存在多个 application 时可以通过 current_app 获取当前请求所对应的 application. current_app 绑定的是当前 request 的 application 的引用，在非 request-response 环境里，是没有 request context 的，所以调用 current_app 就会抛出异常（RuntimeError: working outside of application context）。创建一个 request context 没有必要，而且消耗资源，所以就引入了 application context.

app.app_context().push() 会推入一个 application context，后续所有操作都会在这个环境里执行，直到进程退出。因此，如果在 tasks 里用到了 current_app 或其它需要 application context 的东西，就一定需要这样做。（默认情况下 Celery 的 pool 是 prefork，也就是多进程，现在这种写法没有问题；但是如果指定使用 gevent，是没用的。）

**运行**
在项目的根路径下启动 Celery worker:

>>> $ celery worker -A celery_worker.celery -l INFO

参考文档
=======================

http://liyangliang.me/posts/2015/11/using-celery-with-flask/

https://github.com/miguelgrinberg/flask-celery-example

https://mp.weixin.qq.com/s/h-riGJRjwV2hyq8d2TJBdg

https://zhuanlan.zhihu.com/p/22304455