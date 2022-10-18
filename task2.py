name = input("name: ")
surname = input("surname: ")
year = int(input("year: "))
city = input("city: ")
email = input("email: ")
telephone = input("telephone: ")


def my_func(name, surname, year, city, telephone):
    return " ".join([name, surname, year, city, email, telephone])


print(my_func(name=name, surname=surname, year=year, city=city, email=email,
              telephone=telephone))
