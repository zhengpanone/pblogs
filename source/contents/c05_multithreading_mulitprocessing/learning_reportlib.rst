Reportlib学习
====================

1. demo
 实例化canvas.Canvas,创建pdf对象 

.. code-block:: python
   

   from reportlab.pdfgen import canvas

   def hello(c):
      c.dravString(100,100,'Hello World')

   c = canvas.Canvas('hello.pdf')
   hello(c)
   c.showPage()
   c.save()


