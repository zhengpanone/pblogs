=============================================
1. 使用 Vue.js 和Flask实现全栈单页面应用
=============================================

github源代码_. 


简介
===============

单页面应用(SinglePage Web Application,SPA ),

用 Vue.js,使用单页面组件，在 vue-router 开启 HTML5 history 模式

- Flask运行的服务可以访问 index.html 首页和 Vue.js 应用

- 可以从前端的单页面应用访问 Flask 的 API 接口

- 以 Node.js 服务运行的前端开发环境同样也可以访问 API 接口

步骤
======================

前端开发
>>>>>>>>>>>>>>>>>>>>>>>>

1. vue-cli搭建Vue.js的基础框架
:::::::::::::::::::::::::::::::::::::::::::

.. code-block:: shell
    

    npm install -g vue-cli

2. 创建前端的项目
:::::::::::::::::::::::::::::::::::::::::::

.. code-block:: shell
    

    mkdir flaskvue
    cd flaskvue
    vue init webpack frontend

3. 安装向导的项目设置
:::::::::::::::::::::::::::::::::::::::::::

- Vue build — Runtime only （Vue 构建的版本 - 运行时）

- Install vue-router? — Yes （安装 vue-router？- 是）

- Use ESLint to lint your code? — Yes （使用 ESLint 校验你的代码？- 是）

- Pick an ESLint preset — Standard （选择 ESList 的预置版本 - 标准）

- Setup unit tests with Karma + Mocha? — No （使用 Karma + Mocha 设置单元测试？- 否）

- Setup e2e tests with Nightwatch? — No （使用 Nightwatch 设置端到端测试？- 否）

4. 进入前端项目文件夹
:::::::::::::::::::::::::::::::::::::::::::

.. code-block:: shell
    
    cd frontend
    npm install
    npm run dev 

----

    **此时vue已经运行**

5. 创建其他页面
:::::::::::::::::::::::::::::::::::::::::::

    创建 ``Home.vue`` 和 ``About.vue`` 到 ``frontend/src/components`` 文件夹

.. literalinclude:: ./code/Home.vue
    :encoding: utf-8
    :language: html
    :emphasize-lines: 1,5
    

.. literalinclude:: ./code/About.vue
    :encoding: utf-8
    :language: html
    :emphasize-lines: 1,5
    

----

    修改frontend/src/router/index.js文件

.. literalinclude:: ./code/index.js
    :encoding: utf-8
    :language: javascript
    :emphasize-lines: 13
    :lines: 1-6,8-23
      

6. 校验组件是否挂载成功
:::::::::::::::::::::::::::::::::::::::::::

    输入 localhost:8080 和 localhost:8080/about 你应该看到相应的页面。

7. 自定义构建生成项目的静态资源的输出路径
:::::::::::::::::::::::::::::::::::::::::::

在frontend/config/index.js 找到下面的两行

.. code-block:: python
    
  index: path.resolve(__dirname, '../dist/index.html'),

  assetsRoot: path.resolve(__dirname, '../dist'),

然后成改如下内容

.. code-block:: python

  index: path.resolve(__dirname, '../../dist/index.html'),

  assetsRoot: path.resolve(__dirname, '../../dist'),

这样包含 html/css/js 静态资源包的 /dist 文件夹和 /frontend 在同一级目录下运行 ``$ npm run build`` 去构建项目了

后端开发
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. 在 **frontend** 的同级目录创建后端项目 **backend**
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


.. code-block:: shell

    mkdir backend
    cd backend
    
2. 在 **backend** 目录下编写服务器端代码 **run.py**
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. literalinclude:: ./code/run.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 1
    :lines: 11-17,21-27,36-39,42-43
    

3. 运行flask项目页面会跳转到index.html页面,你试图访问 /about 页面将会出现一个错误
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Flask 会抛出一个找不到请求地址的错误。实际上是因为在 vue-router 用了 HTML5 的 history 模式, 所以我们需要配置我们的后台服务去重定向所有的路由都跳转到 index.html 上。这在 Flask 上可以很简单做到。做如下修改：

.. literalinclude:: ./code/run.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 1
    :lines: 11-17,21-33,42-43
    

4. 添加404页面
::::::::::::::::::::::::::::::::::::::

在 Vue.js 应用里处理未定义的路由。当然，所有的工作均可在我们的路由文件设置。在 frontend/src/router/index.js 增加一行：

.. literalinclude:: ./code/index.js
    :encoding: utf-8
    :language: python
    :emphasize-lines: 4
    :lines: 4-9
    

通配符 **\*** 在 vue-router 里的含义是以上路由定义之外的情况。现在我们需要在 /components 文件夹新建 NotFound.vue 文件。我简单地创建它：

.. literalinclude:: ./code/NotFound.vue
    :encoding: utf-8
    :language: python
    :emphasize-lines: 1
    :lines: 1-15
    

通过 npm run dev 重新启动前台服务然后随意输入网址像 localhost:8080/gljhewrgoh。可以看到 “Not Found” 两个单词。

5. 添加后端API接口
::::::::::::::::::::::::

5.1 后端新增路由
,,,,,,,,,,,,,,,,,,,,,,,,,,

.. literalinclude:: ./code/run.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 12
    :lines: 1-15
    

5.2 前端通过axios库连接后端
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

axios将允许我们创建能返回 Promise 对象的 HTTP 请求

.. code-block:: shell
    

    cd frontend

    npm install --save axios

在文件顶部，我们先导入 axios 库。然后用 axios 去异步调用新方法 getRandonFromBackend 接收返回的结果。最后， getRandom 方法调用 getRandomFromBackend 去获取随机值。

保存文件，打开浏览器，再次运行前端开发服务器环境，刷新 localhost:8080 然后... 你应该看到控制台报了没有随机值的错误。但不用担心，一切正常运行中。我们得到 cors 的错误，它的意思是我们的 Flask 后台 API 默认不对其他的域名和端口（我们的例子运行的是 Vue.js 应用）开放。当你用 npm run build 生成包然后打开 localhost:5000（Flask 服务）你会看到应用正常运行不再报错了。但如果每次在客户端改了一点东西都要重新构建包，显然不是很方便。

5.3 安装flask的CORS插件允许我们为访问 API 创建规则
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. code-block:: shell
    

    pip install flask-cors

服务器上开启 CORS。我这里将会用资源指定的方法应用 {"origins": "*"} 去允许所有 /api/* 下的路由（所以任何人都可以访问 /api 接口）。修改 run.py：

.. literalinclude:: ./code/run.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 13
    :lines: 1-15
    

此时可以从前端的开发环境调用 Flask API 接口了

后期想法

避免在客户端硬编码 API 路由。也许你需要思考为 API 接口创建映射表。所以当你改变 API 路由，你所需要做的只是更新映射表。前端的调用接口将不需要改变

参考文档
======================

微信公众号：前端大学 使用Vue.js和Flask实现全栈单页面应用_. 


.. _github源代码: https://github.com/zhengpanone/flask_web/tree/master/flask_vue_spa
.. _使用Vue.js和Flask实现全栈单页面应用: https://mp.weixin.qq.com/s/aCxnqu3SsIwo1WLSO4kjQA