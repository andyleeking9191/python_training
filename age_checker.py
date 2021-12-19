# Challenge: Create a function that uses an if statement to determine if you are 18 or older to power on.

user_age = input("How old are you? ")

def check_driver_age(age):
    if  len(age) == 0 or int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


check_driver_age(user_age)