def my_posit_argum(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Пытаетесь делить на 0!")


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Результат: {my_posit_argum(a, b)}")
