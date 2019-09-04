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




参考文档
======================

微信公众号：前端大学 使用 Vue.js 和Flask实现全栈单页面应用 
https://mp.weixin.qq.com/s/aCxnqu3SsIwo1WLSO4kjQA
