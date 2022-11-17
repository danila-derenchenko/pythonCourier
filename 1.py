print("Program 1")
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
group = input("Введите номер группы: ")

print(name + " " + surname + " (" + group + ")")

print("Program 2")

year = int(input("Введите год: "))
if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("Високосный год")
else:
    print("Невисокосный год")