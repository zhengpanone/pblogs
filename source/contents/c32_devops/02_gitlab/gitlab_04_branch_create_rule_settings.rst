==========================================
GitLab 分支保护规则配置
==========================================

为什么需要分支保护？
=============================

① 核心价值 
----------------------

- **防御性编程**：防止误操作直接修改主分支（如 master/main）  
- **质量门禁**：强制代码审查（MR）+ 自动化测试（CI）才能合并  
- **权限隔离**：区分开发者提交权限与管理员合并权限  

② 不设保护的潜在风险
----------------------------------

- 新人误删重要分支  
- 未测试代码直接进入生产环境  
- 敏感信息（如密钥）意外提交  

③ 保护规则三大核心
-------------------------------

.. list-table:: 分支保护核心规则
  :header-rows: 1
  :widths: 25 40 35

  * - 规则类型
    - 作用
    - 推荐配置
  * - 推送权限
    - 控制谁能直接提交代码
    - No one（禁止直接推送）
  * - 合并权限
    - 控制谁能批准合并请求
    - Maintainers / Owners
  * - 代码所有者审查
    - 指定模块负责人必须批准
    - 根据 CODEOWNERS 文件自动匹配

步配置分支保护规则
=============================

🎯 步骤①：进入保护设置界面
-----------------------------

1. 进入项目 → ``Settings`` → ``Repository``  
2. 滚动至 **Protected Branches** 板块

⚙️ 步骤②：选择目标分支
------------------------

- Branch: ``main`` 或 ``master`` （保护主分支）  
- Branch: ``release/*`` （可选：保护发布分支）

👥 步骤③：设置合并权限
--------------------------

Allowed to merge:

- Developers + Maintainers  
- Maintainers      ✅ 推荐  
- Specific roles/groups  
- No one  

📝 步骤④：允许推送合并
--------------------------

Allowed to push and merge: ✔️

- Developers + Maintainers  
- Maintainers      ✅ 推荐  
- Specific roles/groups  
- No one  

🔒 步骤⑤：设置强制推送权限
------------------------------

Allowed to force push: **关闭**

高阶配置技巧
======================

🌰 案例 1：基于 CODEOWNERS 的自动化审查
------------------------------------------

创建 `.gitlab/CODEOWNERS` 文件 

.. code-block:: text

  # 文件路径模式 → 负责人
  *.js              @frontend-lead
  /src/api/*.java   @backend-team
  /docs/**/*.md     @tech-writer

合并请求自动指派对应负责人

启用后，MR 将自动分配给对应的模块负责人审批。

🔧 案例 2：API 批量配置（适合多项目）
----------------------------------------

.. code-block:: bash

  curl --request POST \
    --header "PRIVATE-TOKEN: <your_access_token>" \
    --data "name=master&push_access_level=0&merge_access_level=40&code_owner_approval_required=true" \
    "http://gitlab.yourdomain.com/api/v4/projects/123/protected_branches"

参数说明

- ``push_access_level=0``：禁止推送  
- ``merge_access_level=40``：仅 Maintainers 可合并  

🚨 紧急情况处理
-----------------

临时允许直接推送（需 Owner 权限）

1. 关闭分支保护规则  
2. 执行紧急修复  
3. 重新启用保护规则  

命令行强制推送（慎用！）

.. code-block:: bash

   git push origin main --force

常见问题排查
=====================

❌ 问题 1：合并请求无法提交
-----------------------------

- **原因**：未满足代码所有者审查要求  
- **解决**：

  1. 检查 `.gitlab/CODEOWNERS` 文件语法  
  2. 确认被 @ 成员有审批权限  

❌ 问题 2：保护规则不生效
----------------------------

- **原因**：通配符分支未正确匹配  
- **验证**：

  1. 当前分支是否匹配 `main` 或 `release/*`  
  2. 是否在规则生效后创建新分支  

❌ 问题 3：误删保护规则
--------------------------

- **恢复方法**：

  1. 通过审计日志查看操作记录  
     路径：``Settings`` → ``Audit Events``  
  2. 重新配置规则  

附：设置中文界面
=========================

GitLab 支持中文界面切换：

1. 点击右上角头像 → Preferences  
2. 在 Language 中选择：简体中文（Simplified Chinese）  
3. 点击 Save changes

.. _gitlab_branch_create_rule_references:

参考文档
-------------

- `GitLab 分支保护规则配置`_


.. _`GitLab 分支保护规则配置`: https://mp.weixin.qq.com/s?__biz=MzkwOTc3OTcwMQ==&mid=2247486831&idx=1&sn=701059648b0aed7ea86cca9551e27396&chksm=c1343af5f643b3e3984bdfeb50516ff8a55cc85d792d8cc5e2144648916dcfcb13640f221722&scene=178&cur_album_id=3911609890615296006&search_click_id=#rd
