# Challenge: Create a simple login that takes in the username and password of the user
# and then prints out the name of the user and the password length.

username = input("Enter your username: ")
password = input("Enter your password: ")

password_length = len(password)
hidden_password = '*' * password_length

login_message = f'{username}, your password ' + '{' + f'{hidden_password}' + '}' + f' is {password_length} digits long'

print(login_message)