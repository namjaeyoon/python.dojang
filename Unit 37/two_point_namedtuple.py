import math
import collections

Point2D = collections.namedtuple('Point2D', ['x', 'y'])    # namedtuple로 점 표현

p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2

a = p1.x - p2.x    # 선 a의 길이
b = p1.y - p2.y    # 선 b의 길이

c = math.sqrt((a * a) + (b * b))
print(c)    # 42.42640687119285
