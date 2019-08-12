===============================
12.4 策略模式(Strategy)
===============================

定义
====================

定义一系列的算法,把它们一个个封装起来,并且使他们可以相互替换。本模式使得算法的变化可以独立于使用它的客户

应用场景
=====================

电商领域有个使用“策略”模式的经典案例，即根据客户的属性或订单中的商品计算折扣。

例子
=================

假如一个网店制定了下述折扣规则。

 - 有 1000 或以上积分的顾客，每个订单享 5% 折扣。
 - 同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣。
 - 订单中的不同商品达到 10 个或以上，享 7% 折扣。
 - 简单起见，我们假定一个订单一次只能享用一个折扣。

UML类图如下：|image1|

Promotion 抽象类提供了不同算法的公共接口,FidelityPromo、BulkPromo、LargeOrderPromo三个子类实现具体策略,具体策略有上下文类的客户选择

在这个示例中，实例化订单（Order 类）之前，系统会以某种方式选择一种促销折扣策略，然后把它传给 Order 构造方法。具体怎么选择策略，不在这个模式的职责范围内。（选择策略可以使用工厂模式。）

传统方法实现策略模式
--------------------------------

::

 from abc import ABC,abstractmethod
 from collections import namedtuple

 Customet = namedtuple('Customer','name fidelity')

 class LineItem:
    """订单中单个商品的数量和单价"""
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price*self.quantity 

 class Order:
    """"订单"""

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer 
        self.cart = list(cart)
        self.promotion = promotion 
    
    def total(self):
        if not hasattr(self, '__total'):

            self.total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() -discount

    def __repr__(self):
        fmt = '<订单 总价:{:.2f} 实付:{:.2f}>'
        return fmt.format(self.total(),self.due())

 class Promotion(ABC): # 策略:抽象基类
    @abstractmethod
    def discount(self,order):

        """返回折扣金额(正值)"""

        return 

 class FidelityPromo(Promotion): # 第一个具体策略
    """为积分1000或以上顾客提供5%折扣"""
    def discount(self,order):

        return order.total()*0.05 if order.customer.fidelity >= 1000 else 0

 class BulkItemPromo(Promotion): # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""
    def discount(self, order):

        discount = 0
        for item in oredr.cart:

            if item.quantity >= 20:
                discount += item.total()*01
        return discount

 class LargeOrderPromo(Promotion): # 第三个具体策略
    """订单中不同商品达到10个或以上时提供7%"""
    def discount(self, order):

        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:

            return order.total()*0.07

        return 0

 joe = Customer('John Doe', 0)
 ann = Customer('Ann Smith', 1100)

 cart = [LineItem('banan', 4, 0.5),
         LineItem('apple', 10, 1.5),
         LineItem('watermellon', 5, 5.0)]

 print('策略一：为积分为1000或以上的顾客提供5%折扣')
 print(Order(joe, cart, FidelityPromo()))
 print(Order(ann, cart, FidelityPromo()))

 banana_cart = [LineItem('banana', 30, 0.5),
               LineItem('apple', 10, 1.5)]

 print('策略二：单个商品为20个或以上时提供10%折扣')
 print(Order(joe, banana_cart, BulkItemPromo()))

 long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

 print('策略三：订单中的不同商品达到10个或以上时提供7%折扣')
 print(Order(joe, long_order, LargeOrderPromo()))
 print(Order(joe, cart, LargeOrderPromo()))
    
 
使用函数实现策略模式
--------------------------------











https://mp.weixin.qq.com/s/uafM8rzU2rP8LJ5KEqiadQ



.. |image1| image:: ./img/2019051301.webp