===========================
1. python的人脸识别系统
===========================

人脸识别不同于人脸检测。在人脸检测中，我们只检测了人脸的位置，在人脸识别任务中，我们识别了人的身份。

传统人脸识别算法
=================

传统的人脸识别算法不符合现代人脸识别标准。它们旨在使用旧的传统算法识别面部。

OpenCV 提供了一些传统的面部识别算法。

- Eigenfaces：http://www.scholarpedia.org/article/Eigenfaces
- 尺度不变特征变换 (Scale Invariant Feature Transform，SIFT)：https://en.wikipedia.org/wiki/Scale-invariant_feature_transform
- Fisher faces：http://www.scholarpedia.org/article/Fisherfaces
- 局部二进制模式直方图 (Local Binary Patterns Histograms，LBPH)：https://en.wikipedia.org/wiki/Local_binary_patterns

这些方法在提取图像信息和匹配输入和输出图像的方式上有所不同。

LBPH 算法是一种简单但非常有效的方法，仍在使用中，但与现代算法相比速度较慢。

使用 Python 的人脸识别系统
===========================
有多种基于深度学习的面部识别算法可供使用。

- DeepFace
- DeepID series of systems
- FaceNet
- VGGFace

一般来说，基于地标的人脸识别器对人脸图像进行拍摄，并试图找到眉毛、嘴角、眼睛、鼻子、嘴唇等基本特征点。有60多个地标。

人脸识别涉及的步骤
=======================

1. 人脸检测：定位人脸，记下每个人脸定位的坐标，并在每个人脸周围绘制一个边界框。
#. 面部对齐。标准化人脸以获得快速训练。
#. 特征提取。从面部图片中提取局部特征进行训练，这一步由不同的算法执行不同的操作。
#. 人脸识别。将输入人脸与我们数据集中的一个或多个已知人脸进行匹配。

本文使用库 face_recognition 实现人脸识别，该库基于深度学习技术，并承诺使用单个训练图像的准确率超过 96%。

执行
=====

安装人脸识别库
>>>>>>>>>>>>>>>>>>





参考文档
==============================

`使用 Python 的人脸识别系统`_

`opencv使用`_

.. _`使用 Python 的人脸识别系统`: https://mp.weixin.qq.com/s/wj4nd9Tc2n7nEBwyLFlxiQ

.. _`opencv使用`: https://blog.csdn.net/fuhanghang/article/details/121260534

 