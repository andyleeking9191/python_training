# Challenge: Take a list and write a program that prints out all the elements of the list that are less than 5.

number_list = [1, 4, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = []

for num in number_list:
    if num < 5:
        less_than_5.append(num)

print(less_than_5)
