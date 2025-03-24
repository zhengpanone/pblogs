================================
21. FastAPI 从入门到精通实战教程
================================

目录
--------

- :ref:`FastAPI 简介`
- :ref:`环境准备与安装`
- :ref:`创建第一个 FastAPI 应用`
- :ref:`路径操作与请求方法`
- :ref:`使用 Pydantic 定义数据模型`
- :ref:`请求体、查询参数、路径参数`
- :ref:`异步支持`
- :ref:`中间件与依赖注入`
- :ref:`异常处理`
- :ref:`自动生成 API 文档`
- :ref:`部署与生产环境`
- :ref:`进阶部分`




.. _FastAPI 简介:

1. FastAPI 简介
----------------


FastAPI 是一个现代、快速（高性能）的 Web 框架，基于 Python 3.6+ 标准类型提示构建，主要用于构建 API 服务。其主要特点包括：

高性能：基于 Starlette 和 Pydantic，性能媲美 NodeJS 和 Go。

简洁易用：借助 Python 类型提示实现代码自动校验和文档生成。

自动生成文档：内置 OpenAPI（Swagger）和 ReDoc 接口文档，开箱即用。

异步支持：内置 async/await 支持，方便构建异步高并发应用。

.. _环境准备与安装:

2. 环境准备与安装
-------------------------


创建一个 Python 项目，然后安装 FastAPI 和 Uvicorn：

.. code-block:: bash

  pip install fastapi uvicorn

安装完成后，你就可以开始编写 FastAPI 应用了。

.. _创建第一个 FastAPI 应用:

3. 创建第一个 FastAPI 应用
---------------------------

下面是一个简单的示例，通过一个 HTTP GET 请求返回一个 JSON 数据：

.. code-block:: python

  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/")
  async def read_root():
      return {"message": "Hello, FastAPI!"}

把上面的代码保存为 main.py，然后在命令行输入下面的命令，来启动服务器：

.. code-block:: bash

  uvicorn main:app --reload

默认端口是8000，通过访问 http://127.0.0.1:8000 即可看到返回的 JSON 响应。

.. _路径操作与请求方法:

4. 路径操作与请求方法
---------------------------

FastAPI 提供了多种 HTTP 方法支持（GET、POST、PUT、DELETE 等）：

.. code-block:: python

  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/items/{item_id}")
  async def get_item(item_id: int, q: str = None):
      return {"item_id": item_id, "q": q}

  @app.post("/items/add")
  async def add_item(item: dict):
      return {"item": item}

.. _使用 Pydantic 定义数据模型:

5. 使用 Pydantic 定义数据模型
--------------------------------

利用 Pydantic 模型，可以进行数据校验和自动文档生成：

.. code-block:: python

  from fastapi import FastAPI
  from pydantic import BaseModel

  app = FastAPI()

  class Item(BaseModel):
      name: str
      description: str = None
      price: float
      tax: float = None

  @app.post("/items/")
  async def create_item(item: Item):
      item_dict = item.dict()
      if item.tax:
          total_price = item.price + item.tax
          item_dict.update({"total_price": total_price})
      return item_dict

.. _请求体、查询参数、路径参数:

6. 请求体、查询参数、路径参数
-------------------------------

FastAPI 支持多种参数类型：

- 路径参数：直接从 URL 中提取，例如 /items/{item_id}。
- 查询参数：通过 URL 查询字符串传递，例如 /items/?q=search。
- 请求体：通过 POST/PUT 请求提交 JSON 数据，利用 Pydantic 模型进行校验。

.. _异步支持:

7. 异步支持
-------------------------------

FastAPI 内置对异步函数 (async def) 的支持，能够高效地处理 I/O 密集型任务。

代码案例：

.. code-block:: python

  import asyncio
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/async")
  async def get_async_data():
      await asyncio.sleep(1)  # 模拟异步操作
      return {"data": "这是异步返回的数据"}


使用异步函数可以在处理数据库、外部 API 调用等场景时显著提升性能。

.. _中间件与依赖注入:

8. 中间件与依赖注入
========================================

## 中间件

你可以添加中间件来处理请求和响应，例如记录日志、添加 CORS 支持等：

.. code-block:: python

  from fastapi import FastAPI, Request
  from fastapi.middleware.cors import CORSMiddleware

  app = FastAPI()

  # 添加跨域中间件
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  @app.middleware("http")
  async def log_requests(request: Request, call_next):
      response = await call_next(request)
      print(f"Request: {request.method} {request.url} - Status: {response.status_code}")
      return response


## 依赖注入

利用依赖注入，可以实现共享资源、权限校验等逻辑：

.. code-block:: python

  from fastapi import Depends, HTTPException

  def common_parameters(q: str = None, skip: int = 0, limit: int = 10):
      return {"q": q, "skip": skip, "limit": limit}

  @app.get("/dependencies/")
  async def read_items(commons: dict = Depends(common_parameters)):
      return commons


这种方式便于代码复用和模块化设计。

.. _异常处理:

9. 异常处理
========================

FastAPI 提供了全局异常处理机制，可以自定义异常和错误响应：

.. code-block:: python

  from fastapi import HTTPException

  @app.get("/error/{item_id}")
  async def read_item_with_error(item_id: int):
      if item_id == 0:
          raise HTTPException(status_code=404, detail="Item not found")
      return {"item_id": item_id}


此外，你也可以通过 `@app.exception_handler` 装饰器自定义处理特定异常。

.. _自动生成 API 文档:

10.   自动生成 API 文档
========================================

FastAPI 自动生成两种文档：

- **Swagger UI**: 访问 `/docs`
- **ReDoc**: 访问 `/redoc`

你可以直接在浏览器中访问这些路径，查看交互式 API 文档，非常方便调试和测试接口。

.. _部署与生产环境:

11.  部署与生产环境
========================================

在生产环境中，可以使用 Uvicorn 或 Gunicorn (配合 Uvicorn Worker) 来部署 FastAPI 应用。

示例 Gunicorn 启动命令：

.. code-block:: bash

  gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000


同时建议使用反向代理（如 Nginx）来处理静态文件和 SSL 加密。


.. _进阶部分:

12. 进阶部分
========================

## 安全性

### OAuth2 与 JWT

FastAPI 内置对 OAuth2 的支持，可以很容易地实现基于 JWT 的身份验证。

### 密码哈希

使用 passlib 等库对密码进行安全哈希处理。

## 后台任务

利用 BackgroundTasks 实现异步后台任务，例如发送邮件、数据处理等：

.. code-block:: python

  from fastapi import BackgroundTasks

  def write_log(message: str):
      with open("log.txt", "a") as f:
          f.write(message + "\n")

  @app.post("/send-notification/")
  async def send_notification(background_tasks: BackgroundTasks):
      background_tasks.add_task(write_log, "通知已发送")
      return {"message": "Notification sent in the background"}

## WebSocket 支持

FastAPI 也支持 WebSocket，可以用来实现实时通信功能：

.. code-block:: python

  from fastapi import WebSocket

  @app.websocket("/ws")
  async def websocket_endpoint(websocket: WebSocket):
      await websocket.accept()
      while True:
          data = await websocket.receive_text()
          await websocket.send_text(f"收到消息: {data}")


