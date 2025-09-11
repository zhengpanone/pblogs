# 实用示例：计算向量点积
import operator as op
from functools import reduce

vector1 = [2, 4, 6]
vector2 = [1, 3, 5]

dot_product = reduce(op.add, map(op.mul, vector1, vector2))
print(f"点积结果: {dot_product}")  # 2*1 + 4*3 + 6*5 = 44

# 实用示例：多级排序
students = [
    {"name": "Alice", "grade": "B", "score": 85},
    {"name": "Bob", "grade": "A", "score": 90},
    {"name": "Charlie", "grade": "A", "score": 88}
]

# 先按grade升序，再按score降序
get_grade = op.itemgetter("grade")
get_score = op.itemgetter("score")
sorted_students = sorted(students, key=lambda x: (-ord(get_grade(x)), get_score(x)), reverse=True)
