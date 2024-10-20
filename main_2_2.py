number1 = int(input("Введите число: "))
number2 = int(input("Введите число: "))
number3 = int(input("Введите число: "))
if number1 == number2 == number3:
    print("Вывод: 3")
elif number1 == number2 or number1 == number3 or number2 == number1:
    print("Вывод: 2")
else:
    print("Вывод: 0")