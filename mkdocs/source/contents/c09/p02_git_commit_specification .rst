========================
1.2 git 提交规范
========================

规则
===============

.. note:: <type>(scope):<subject>

- **type**
用于说明commit的类别，只允许使用下面的7个标识：

.. note:: - feat: 新功能（feature）
          - fix: 修补bug
          - docs: 文档（documentation）
          - style: 格式（不影响代码运行的变动）
          - refactor：重构（即不是新增功能，也不是修改bug的代码变动）
          - test: 增加测试
          - chore: 构建过程或辅助工具的变动

- scope

说明commint 影响范围，比如数据层、控制层、视图层等

- subject

是commit目的的简短描述，不超过50个字符

.. note::

    以动词开头，使用第一人称现在时，比如change，而不是changed或changes
    第一个字母小写
    结尾不加句号(.)

异常处理
===============


参考文档：https://mp.weixin.qq.com/s/9rK1dcKa699ZQb9qVjf7pw