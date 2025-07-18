
==========================
GitLab项目创建与基础设置
==========================

📖 基础概念解析
==========================


🌟 1. GitLab 项目的核心作用
--------------------------------

- **代码仓库**：存储代码并记录版本变更历史  
- **协作中心**：通过 Issue、MR（合并请求）实现团队协作  
- **基础配置池**：初始化设置影响后续开发流程（如分支规则、文件模板）

🔍 2. 项目三要素解析
--------------------------------

.. list-table:: 项目三要素
  :header-rows: 1
  :widths: 20 40 40

  * - 要素
    - 说明
    - 示例值
  * - 项目名称
    - 全局唯一标识，建议英文小写+连字符
    - my-webapp、api-service
  * - 可见性级别
    - Private（仅成员可见）、Internal（登录用户可见）、Public（全公开）
    - 团队项目选 Private
  * - 初始化选项
    - 自动生成 README、.gitignore、LICENSE 文件
    - 强烈建议勾选 README

⚠️ 3. 基础设置的四大核心
--------------------------------

1. ``README.md``：项目门面文档（技术栈、部署说明）  
2. ``.gitignore``：过滤无用文件（如 ``node_modules/``、``.DS_Store``）  
3. **分支保护**：防止误操作主分支  
4. **基础文件结构**：规范化目录（如 ``src/``、``docs/``、``tests/``）  

🛠 手把手操作演示
==========================

🎯 步骤 1：通过网页创建项目
--------------------------------

1. 登录 GitLab → 点击导航栏 ``+`` → **New project**  
2. 选择 **Create blank project**  
3. 填写关键信息：

  - ``Project name``：my-first-project  （🌐 按命名规范填写）  
  - ``Project URL``：自动生成（可自定义路径）  
  - ``Visibility Level``：Private（🛡️ 推荐团队项目选择）  
  - ``Initialize repository``：✔️ 勾选 README（📝 必须勾选）

4. 点击 **Create project**

⚡ 步骤 2：初始化本地仓库（命令行）
-------------------------------------------

.. code-block:: bash

  mkdir -p /data/demo
  cd /data/demo
  git clone http://gitlab.yourdomain.com/yourname/my-first-project.git
  cd my-first-project

  # 如果未勾选 README，可手动添加
  echo "# My First Project" > README.md
  echo "node_modules/" > .gitignore

  # 配置 Git 信息
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

  # 首次提交
  git add .
  git commit -m "chore: 初始化项目基础结构"
  git push -u origin main

⚙️ 步骤 3：基础配置强化
--------------------------------

① 添加 ``.gitignore`` 模板（Web 端）
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. 进入项目 → ``Add file`` → ``New file``  
2. 文件名输入 ``.gitignore``  
3. 填写内容：

.. code-block:: text

  # 通用配置
  .DS_Store
  *.log
  /dist/

  # Node 项目示例
  node_modules/
  .env

② 保护主分支（Web 端）
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. 项目设置 → ``Settings`` → ``Repository`` → ``Protected Branches``  
2. 选择 ``main`` 分支 → 设置：

  - Allowed to push: No one（🚫 禁止直接推送）  
  - Allowed to merge: Maintainers（👥 仅管理员可合并）

③ 配置基础文件结构（命令行）
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  mkdir -p src docs tests
  find . -type d -empty -exec touch {}/.gitkeep \;

  git add src/ docs/ tests/
  git commit -m "chore: 初始化项目目录"
  git push origin main

🚨 避坑指南
==========================

1. **命名禁忌**：

  - ❌ 使用空格：``my project`` → ✅ ``my-project``  
  - ❌ 大写字母：``MyProject`` → ✅ ``myproject``  

2. **可见性误区**：

  - Internal 模式下，任何登录用户均可克隆代码，敏感项目慎用！

3. **初始化必选项**：

  - 未勾选 README 会导致空仓库，首次推送需强制覆盖：

.. code-block:: bash

  git push -u origin main --force

🌰 实战演示案例：Python 项目 data-analysis
====================================================

1. 网页端操作：

  - 名称：data-analysis  
  - 勾选：README + .gitignore（Python 模板） + LICENSE（MIT）

2. 本地初始化：

.. code-block:: bash

  git clone http://gitlab.yourdomain.com/user/data-analysis.git
  cd data-analysis
  mkdir src data notebooks
  touch src/main.py data/sample.csv

3. 首次提交：

.. code-block:: bash

  git add .
  git commit -m "feat: 初始化Python项目结构"
  git push origin main

.. _gitlab_project_create_settings_references:

参考文档
-------------

- `GitLab 项目创建与基础设置`_

.. _`GitLab 项目创建与基础设置`: https://mp.weixin.qq.com/s?__biz=MzkwOTc3OTcwMQ==&mid=2247486831&idx=1&sn=701059648b0aed7ea86cca9551e27396&chksm=c1343af5f643b3e3984bdfeb50516ff8a55cc85d792d8cc5e2144648916dcfcb13640f221722&scene=178&cur_album_id=3911609890615296006&search_click_id=#rd

