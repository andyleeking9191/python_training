# Challenge: Given the class below:
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# Instantiate the Cat object with 3 cats and create a function that finds the oldest cat
# and prints its name and age.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Spookie", 2)
cat2 = Cat("Mooch", 4)
cat3 = Cat("Terry", 1)


def print_oldest_cat(*args):
    oldest = args[0]
    for cat in args:
        if cat.age > oldest.age:
            oldest = cat
    print(f'The oldest cat is {oldest.name}, which is {oldest.age} years old.')
    return oldest


print_oldest_cat(cat1, cat2, cat3)
