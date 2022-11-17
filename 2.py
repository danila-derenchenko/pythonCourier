import math

print("Program 3")
count = int(input("Введите количество точек: "))

tochki = []

for i in range(count):
    tochka = input("Введите точку : ")
    x, y = tochka.split()
    tochki.append([int(x), int(y)])
min = 100000000
minTochka = []
max = 0
maxTochka = []
for i in range(len(tochki)):
    for a in range(i + 1, len(tochki)):
        dist = math.dist((tochki[i][0], tochki[i][1]), (tochki[a][0], tochki[a][1]))
        if dist > max:
            max = dist
            maxTochka = [tochki[i], tochki[a]]
        if dist < min:
            min = dist
            minTochka = [tochki[i], tochki[a]]
print("min distanse between (" + str(minTochka[0][0]) + ", " + str(minTochka[0][1]) + ") and (" + str(minTochka[1][0]) + ", " + str(minTochka[1][1]) + "): " + str(min))

print("max distanse between (" + str(maxTochka[0][0]) + ", " + str(maxTochka[0][1]) + ") and (" + str(maxTochka[1][0]) + ", " + str(maxTochka[1][1]) + "): " + str(max))