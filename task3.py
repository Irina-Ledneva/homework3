def my_func(one, two, free):
    my_list = [one, two, free]
    my_list.sort()
    return my_list[-1] + my_list[-2]


def my_func2(one, two, free):
    my_list = [one, two, free]
    i = 1
    while i > 0:
        for el in range(len(my_list) - 1):
            i = 0
            if my_list[el] > my_list[el + 1]:
                my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
                i += 1
    return my_list[-1] + my_list[-2]


my_summa = my_func(95, 78, 2)
print(f"Сумма посчитана с помощью sort: {my_summa}")
my_summa = my_func2(95, 78, 2)
print(f"Сумма посчитана без sort: {my_summa}")
