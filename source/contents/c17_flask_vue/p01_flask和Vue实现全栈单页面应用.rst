=============================================
使用 Vue.js 和Flask实现全栈单页面应用
=============================================

github源代码


简介
===============

用 Vue.js,使用单页面组件，在 vue-router 开启 HTML5 history 模式

- Flask运行的服务可以访问 index.html 首页和 Vue.js 应用

- 可以从前端的单页面应用访问 Flask 的 API 接口

- 以 Node.js 服务运行的前端开发环境同样也可以访问 API 接口

步骤
======================

前端开发
>>>>>>>>>>>>>>>>>>>>>>>>

1. vue-cli搭建Vue.js的基础框架

    ``npm install -g vue-cli``

2. 创建前端的项目

.. code-block:: shell
    :linenos:

    mkdir flaskvue
    cd flaskvue
    vue init webpack frontend

3. 安装向导的项目设置

4. 进入前端项目文件夹

.. code-block:: shell
    :linenos:

    cd frontend
    npm install
    npm run dev 

----

    ``此时vue已经运行``

5. 创建其他页面

    创建 ``Home.vue`` 和 ``About.vue`` 到 ``frontend/src/components`` 文件夹

.. literalinclude:: ./code/Home.vue
    :encoding: utf-8
    :language: html
    :emphasize-lines: 1,5
    :linenos:

.. literalinclude:: ./code/About.vue
    :encoding: utf-8
    :language: html
    :emphasize-lines: 1,5
    :linenos:

6. 校验组件是否挂载成功

    输入 localhost:8080 和 localhost:8080/about 你应该看到相应的页面。

7. 自定义构建生成项目的静态资源的输出路径

在frontend/config/index.js 找到下面的两行

::

    index: path.resolve(__dirname, '../dist/index.html'),

    assetsRoot: path.resolve(__dirname, '../dist'),

然后成改如下内容

::

    index: path.resolve(__dirname, '../../dist/index.html'),

    assetsRoot: path.resolve(__dirname, '../../dist'),

这样包含 html/css/js 静态资源包的 /dist 文件夹和 /frontend 在同一级目录下运行 ``$ npm run build`` 去构建项目了

后端开发
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. 在 **frontend** 的同级目录创建后端项目 **backend**

::

    mkdir backend
    cd backend
    
2. 在**backend**目录下编写服务器端代码**run.py**

.. literalinclude:: ./code/run.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 12
    :lines: 12-
    :linenos:

3. 运行flask项目页面会跳转到index.html页面,你试图访问 /about 页面将会出现一个错误

4. 添加404页面









参考文档
======================

微信公众号：前端大学 使用 Vue.js 和Flask实现全栈单页面应用 
https://mp.weixin.qq.com/s/aCxnqu3SsIwo1WLSO4kjQA
