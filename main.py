import math
import random

class Curier:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, x, y, name, id, speed):
        self.coordinate = Point(x, y)
        self.name = name
        self.id = id
        self.speed = speed
        self.history = History()
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
            timer = math.ceil((math.dist((curierCoordinate[0], curierCoordinate[1]), (order[0], order[1])) + math.dist((order[0], order[1]), (0, 0))) / self.speed)
            self.history.addOrder(math.ceil(math.dist((curierCoordinate[0], curierCoordinate[1]), (order[0], order[1])) / self.speed), {"x": curierCoordinate[0], "y": curierCoordinate[1]}, {"x": order[0], "y": order[1]}, "Доставка")
            self.coordinate.relocate(order[0], order[1])
            self.history.addOrder(math.ceil(math.dist((order[0], order[1]), (0, 0)) / self.speed), {"x": order[0], "y": order[1]}, {"x": 0, "y": 0}, "Доставка")
            self.coordinate.relocate(0, 0)
            print("Заказ доставлен за время " + str(timer) + " " + str(self.id))
        else:
            print("Заказов больше нет. Курьер " + str(self.id))
            self.history.getHistory()
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

class History:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self):
        self.history = []
    def addOrder(self, timer, fromStart, toFinish, orders):
        self.history.append({
            "time": timer,
            "from": fromStart,
            "to": toFinish,
            "orders": orders
        })
    def getHistory(self):
        print(self.history)
curiers = []
orders = []

for i in range(random.randint(5, 10)):
    curiers.append(Curier(random.randint(0, 100), random.randint(0, 100), "Alexey", i + 1, random.randint(4, 8)))

for i in range(10):
    orders.append([random.randint(0, 100), random.randint(0, 100)])

while len(orders) > 0:
    for i in curiers:
        i.searchOrders()