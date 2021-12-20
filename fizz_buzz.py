n = int(input())

for num in range(1, n):
    odd_numbers = []
    if num % 2 != 0:
        odd_numbers.append(num)
    for odd_num in odd_numbers:
        if odd_num % 3 == 0 and odd_num % 5 == 0:
            print("Python Is Awesome")
        elif odd_num % 3 == 0:
            print("Python")
        elif odd_num % 5 == 0:
            print("Is Awesome")
        else:
            print(odd_num)