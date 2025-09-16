from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
     
    # 将函数伪装成属性
    @property   
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError('Radius must be a positive number')
        self._radius = value
        
    @property   
    def area(self):
        return pi * self.radius ** 2
      
if __name__ == '__main__':
    c = Circle(1)
    print(c.__dict__)
    print(c.area)
    c.radius = 2
    print(c.__dict__)
    print(c.area)
    
    c.radius = -1
    print(c.__dict__)
    print(c.area)