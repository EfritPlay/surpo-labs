# Простой калькулятор для лабораторной работы 2

def add(a, b):
    return a + b


def sub(a, b):
    return a - b

a = float(input("Первое число: "))
b = float(input("Второе число: "))
print("Сумма:", add(a, b))
print("Разность:", sub(a, b))
