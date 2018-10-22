class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height
print(area)
