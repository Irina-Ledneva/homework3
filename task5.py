def int_func(my_text):
    return my_text.capitalize()


my_text = input("Введите строку:")

my_list = my_text.split()
for my_word in my_list:
    print(int_func(my_word), end=" ")
