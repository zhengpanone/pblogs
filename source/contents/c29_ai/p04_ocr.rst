================
PaddleOCR
================

PaddleOCR 是一个基于 PaddlePaddle 开发的开源 OCR 工具库。

在 PaddleOCR 中：

.. code-block:: text

  det = Detection（文本检测）
  rec = Recognition（文本识别）
  cls = Classification（文本方向分类）

OCR 一般分为三个阶段：

.. code-block:: text

  图片
  ↓
  det（找文字位置）
  ↓
  cls（判断文字方向）
  ↓
  rec（识别文字内容）
  ↓
  结果

.. todo:: 

   * 介绍 PaddleOCR 的安装和使用方法
   * 展示 PaddleOCR 的实际应用案例