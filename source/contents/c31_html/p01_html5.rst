=============================
1. HTML5全局属性汇总
=============================

- **局部属性** ：有些元素能规定自己的属性，这种属性称为局部属性。

    比如link元素，它具有的局部属性有href、 rel、 hreflang、 media、 type、 sizes这六个。

- **全局属性** ：可以用来配置所有元素共有的行为，这种属性称为全局属性，可以用在任何一个元素身上。

----

1. accesskey属性
==============================

使用accesskey属性可以设定一个或几个用来选择页面上的元素的快捷键。

2. contenteditable属性
================================

contenteditable是HTML5中新增加的属性，，其用途是让用户能够修改页面上的内容。

.. literalinclude:: ./code/html5全局属性.html
    :encoding: utf-8
    :language: html
    :emphasize-lines: 2
    :lines: 12,13
    :linenos:  

3. dir属性
================================

dir属性用来规定元素中文字的方向。有效值有两个：ltr(从左到右)、rtl(从右到左)。

.. literalinclude:: ./code/html5全局属性.html
    :encoding: utf-8
    :language: html
    :emphasize-lines: 2
    :lines: 14-16
    :linenos:  

4. draggable属性
===============================

draggable属性是html5支持拖放操作的方式之一,用来表示元素是否可以被拖放
提示：**链接和图像默认是可拖动的。**

``<element draggable="true|false|auto">``

======  =====================
值      描述
------  ---------------------
true    规定元素的可拖动的。
false   规定元素不可拖动。
auto    使用浏览器的默认行为。 
======  =====================

.. literalinclude:: ./code/draggable属性.html
    :encoding: utf-8
    :language: html
    :emphasize-lines: 27
    :lines: 9-
    :linenos:  

5 dropzone属性
==========================

dropzone属性是HTML5支持拖放操作的方式之一，与draggable属性搭配使用

6 hidden属性
=========================

hidden是个布尔属性，表示相关元素当前不需要关注，浏览器对它的处理方式是隐藏相关元素（隐隐想起来控制一个元素的展示隐藏的时候，会自定义一个hidden类，然后在里面写隐藏样式）

.. literalinclude:: ./code/html5全局属性.html
    :encoding: utf-8
    :language: html
    :emphasize-lines: 2
    :lines: 21,22
    :linenos:  

7 lang属性
===========================

lang属性用于说明元素内容使用的语言。lang属性必须使用有效的ISO语音代码，使用这个属性的目的在于，让浏览器调整其表达元素内容的方式，比如在使用了文字朗读器的情况下正确发音。

.. code-block:: html
    :linenos:

    <!-- lang属性应用 -->
    <p lang="en">Hello - how are you?</p>


8、spellcheck属性
==============================

spellcheck属性用来表明浏览器是否应该对元素的内容进行拼写检查，这个属性只有用在用户可以编辑的元素上时才有意义。 spellcheck属性可以接受的值有两个：true和false。至于拼写检查的实现方式则因浏览器而异。

.. code-block:: html
    :linenos:

    <!-- spellcheck属性应用 -->
    <textarea name="" id="" cols="30" rows="10" spellcheck="true">
    This is some lalalala text</textarea>
