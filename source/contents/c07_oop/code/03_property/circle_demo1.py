from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
     
    # 将函数伪装成属性
    @property   
    def area(self):
        return pi * self.radius ** 2
      
if __name__ == '__main__':
    c = Circle(1)
    print(c.area)
    c.radius = 2
    print(c.area)