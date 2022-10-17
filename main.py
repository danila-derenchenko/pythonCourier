
curiers = [[400, 70], [200, 40], [40000, 100000]]

orders = [[10, 900], [6000, 300], [20, 400], [65, 23]]

result = {}

for i in range(len(orders)):
    distanse = []
    for j in range(len(curiers)):
        d = ((curiers[j][0] - orders[i][0]) ** 2 + (curiers[j][1] - orders[i][1]) ** 2) ** 0.5
        distanse.append(d)
    indexCurier = distanse.index(min(distanse))
    time = min(distanse) / 5
    result[i] = {
        "order": i,
        "curier": indexCurier,
        "time": time
    }
print(result)