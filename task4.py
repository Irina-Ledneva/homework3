def my_func(x, y):
    my_degree = x
    for i in range(-y - 1):
        my_degree *= x
    return 1 / my_degree


try:
    x = float(input("Введите действительное положительное число х: "))
    y = int(input("Введите целое отрицательное число y: "))
    print(f"Возведение числа {x} в степень {y} дает результат {my_func(x, y)}")
except ValueError:
    print("Неверный ввод")
