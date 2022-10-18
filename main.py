import math


class Tochka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Точка с координатами (" + str(self.x) + ", " + str(self.y) + ")"

    def get_distanse(self, other_point):
        return math.dist((self.x, self.y), (other_point.x, other_point.y))

a = Tochka(4, 9)
b = Tochka(6, 9)
print(a.get_distanse(b))