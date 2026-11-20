# Простой калькулятор для лабораторной работы 2

def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return None
    return a / b

a = float(input("Первое число: "))
b = float(input("Второе число: "))
print("Сумма:", add(a, b))
print("Разность:", sub(a, b))
print("Произведение:", mul(a, b))
if b == 0:
    print("На ноль делить нельзя")
else:
    print("Частное:", div(a, b))
