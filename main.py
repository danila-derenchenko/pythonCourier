import math

orders = [[4, 5], [6, 9]]

class Curier:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, x, y, name):
        self.coordinate = Point(x, y)
        self.name = name
        self.coordinate.searchOrder()
class Point:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def searchOrder(self):
        min = 100000
        ind = 100000
        for i in range(len(orders)):
            if math.dist((self.x, self.y), (i[0], i[1])) < min:
                min = math.dist((self.x, self.y), (i[0], i[1]))
                ind = i
curier = Curier(4, 8, "Anton")