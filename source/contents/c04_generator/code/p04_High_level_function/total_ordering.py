from functools import total_ordering

@total_ordering
class Student:
  def __init__(self, name, age, score: int) -> None:
    self.name = name
    self.age = age
    self.score = score
    
  def __eq__(self, value: 'Student') -> bool:
    return self.score == value.score
  
  def __lt__(self, value: 'Student') -> bool:
    return self.score < value.score
  
if __name__ == '__main__':
  
  s1 = Student('Tom', 18, 90)
  s2 = Student('Jack', 19, 90)
  s3 = Student('Bob', 20, 90)
  s4 = Student('Alice', 18, 90)
  
  print(s1 >= s2) # True
  print(s1 < s2) # False
  print(s1 < s3) # True
  print(s1 < s4) # False  