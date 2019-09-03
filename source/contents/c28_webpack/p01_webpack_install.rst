=================
1. webpack安装
=================

安装
=========

.. code:: bash 

    npm i webpack -g # 全局安装webpack


创建项目流程
===============

* 创建项目文件夹 mkdir webpack_test

* 进入项目文件夹 cd webpack_test 

* package进行初始化 npm init -y  该操作会在项目文件夹下创建package.json 和package-lock.json 两个文件

* 在项目文件夹下创建 dist、src，在src下创建css 、images、js 等文件夹

* 在src下创建并编写index.html 、main.js 文件

* 在项目根目录运行webpack 命令：**webpack ./src/main.js -o ../dist/bundle.js**

* 在 index.html中引入bundle.js文件

* 配置webpack，在项目根目录创建webpack.config.js文件 

.. code::

 const path = require('path')

 module.exports={
    entry:path.join(__dirname, './src/main.js'),
    output:{
        path:path.join(__dirname, './dist'),
        filename: 'bundle.js'
    },
    mode:'development'
 }

* 在项目根目录直接运行 **webpack** 命令

使用webpack-dev-server来实现自动打包编译功能
================================================

安装 
>>>>>>>>>>>>>

.. code:: bash 

    npm i webpack-dev-server -D 把这个工具安装到项目本地开发依赖

使用
>>>>>>>>>>>>>

打开package.json 编写  scripts 项 ，在test下面添加**"dev": "webpack-dev-server --inline --hot --open --port 8000"**

.. code::note

 在使用webpack-dev-server的过程中要注意webpack和webpack-dev-server的版本兼容性

 webpack-dev-server 打包生成的bundle.js文件，并没有存放到实际的物理磁盘上，而是直接托管到电脑内存中，所以在我们的项目的根目录下找不到打包好的bundle.js

常用的命令
>>>>>>>>>>>>>>>>>>>>>>

webpack-dev-server --inline --hot --open --port 8000 --contentBase src

--hot 实现浏览器无刷新的热重载
--contentBase 指定打开的目录
--open自动打开浏览器


html-webpack-plugin在内存中生成html的插件
==============================================

安装
>>>>>>>>>>>>>>>>>>>>

.. code:: bash

    cnpm i html-webpack-plugin -D


打包处理css的加载器
==================================

安装
>>>>>>>>>>>>>>>

.. code:: bash

    cnpm i style-loader css-loader -D


babel
==============================

babel的用处
