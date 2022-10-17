name = input("name: ")
surname = input("surname: ")
year = int(input("year: "))
city = input("city: ")
email = input("email: ")
telephone = input("telephone: ")


def my_func(name, surname, year, city, telephone):
    return " ".join([name, surname, year, city, email, telephone])


print(my_func(name="Irina", surname="Ledneva", year="1945", city="world", email="error404@mail.ru",
              telephone="not found"))
