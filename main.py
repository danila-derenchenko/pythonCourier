import math
import random

class Curier:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, x, y, name, id):
        self.coordinate = Point(x, y)
        self.name = name
        self.id = id
    def restartSearch(self):
        self.searchOrders()
    def searchOrders(self):
        if len(orders) > 0:
            minDist = 100000000000000000000000000000000
            minInd = 0
            curierCoordinate = self.coordinate.getCoordinate()
            for i in orders:
                if math.dist((i[0], i[1]), (curierCoordinate[0], curierCoordinate[1])) < minDist:
                    minDist = math.dist((i[0], i[1]), (curierCoordinate[0], curierCoordinate[1]))
                    minInd = orders.index(i)
            order = orders[minInd]
            orders.remove(order)
            print(orders)
            self.coordinate.relocate(order[0], order[1])
            self.coordinate.relocate(0, 0)
            print("Заказ доставлен")
            self.restartSearch()
        else:
            print("Заказов больше нет")
class Point:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def relocate(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def getCoordinate(self):
        return [self.x, self.y]

curiers = []
orders = []

for i in range(random.randint(4, 10)):
    curiers.append(Curier(random.randint(0, 100), random.randint(0, 100), "Alexey", i + 1))

for i in range(random.randint(4, 10)):
    orders.append([random.randint(0, 100), random.randint(0, 100)])

for i in curiers:
    i.searchOrders()