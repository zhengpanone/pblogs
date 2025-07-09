.. _playwright_intro:

======================
Playwright 入门指南
======================

概述
====
Playwright 是一个用于 Web 自动化测试的现代工具，支持 **Chromium、Firefox 和 WebKit**，适用于 **Node.js、Python、Java、.NET** 语言。

与传统的浏览器自动化工具相比，Playwright 拥有以下优势：

1. 更快的执行速度: Playwright 直接与浏览器引擎通信，无需依赖 WebDriver，因此执行速度更快，效率更高。

2. 更强大的功能: Playwright 提供了丰富的 API，能够模拟用户操作、处理网络请求、拦截修改数据等，满足各种自动化需求。

3. 更稳定的体验: Playwright 内置了自动等待机制，能够有效避免因页面加载延迟导致的脚本失败，提供更稳定的自动化体验。

4. 更简单的使用: Playwright 提供了简洁易懂的 API 和丰富的文档，即使是初学者也能快速上手。

本指南将介绍 Playwright 的基本使用，包括 **安装、环境配置、基本操作** 以及 **示例代码**。

安装 Playwright
=====================

Node.js 版本
-------------------

确保你已安装 **Node.js 16+**，然后运行以下命令安装 Playwright：

.. code-block:: shell

   npm init playwright@latest

或直接安装到现有项目中：

.. code-block:: shell

   npm install --save-dev playwright

安装 Python 版本
-----------------------

如果你使用 Python，可以使用 pip 安装：

.. code-block:: shell

   pip install playwright
   playwright install

环境配置
=======================

Playwright 需要下载并安装浏览器驱动，使用以下命令完成环境配置：

.. code-block:: shell

   npx playwright install

或者，如果你使用 Python 版本：

.. code-block:: shell

   playwright install

快速开始
========

创建并运行测试
----------------

Node.js 版本示例：

.. literalinclude:: ./code/p01_playwright/01_playwright.js
    :encoding: utf-8
    :language: javascript
    

Python 版本示例：

.. literalinclude:: ./code/p01_playwright/01_playwright.py
    :encoding: utf-8
    :language: python
    


使用 Playwright Test 运行测试
------------------------------

Playwright Test 是官方推荐的测试框架，可以使用以下命令执行测试：

.. code-block:: shell

   npx playwright test

示例测试文件：

.. code-block:: javascript

   import { test, expect } from '@playwright/test';

   test('basic test', async ({ page }) => {
       await page.goto('https://example.com');
       await expect(page).toHaveTitle(/Example Domain/);
   });

调试 Playwright
====================

启用调试模式
-------------------

在运行测试时，可以启用 **调试模式**，观察测试执行的过程：

.. code-block:: shell

   npx playwright test --debug

或者在代码中使用 `headless: false` 让浏览器可视化运行：

.. code-block:: javascript

   const browser = await chromium.launch({ headless: false });

录制测试脚本
----------------

Playwright 提供了录制功能，可以快速生成测试代码：

.. code-block:: shell

   npx playwright codegen https://www.baidu.com

这将打开浏览器，并记录你在页面上的操作，同时生成相应的 Playwright 代码。

结论
=======

本指南介绍了 Playwright 的基本使用，包括安装、环境配置、测试代码示例和调试方式。Playwright 提供了强大的 Web 自动化功能，适用于端到端测试、爬虫和数据抓取。

更多详细信息，请参考官方文档：

- `Playwright 官方文档 <https://playwright.dev/>`_
- `Playwright GitHub <https://github.com/microsoft/playwright>`_

