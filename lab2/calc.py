# Простой калькулятор для лабораторной работы 2

def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def main():
    print("1 - сложение")
    print("2 - вычитание")
    choice = input("Выберите операцию: ")
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    if choice == "1":
        print("Результат:", add(a, b))
    elif choice == "2":
        print("Результат:", sub(a, b))
    else:
        print("Нет такой операции")


main()
