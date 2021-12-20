# Challenge: Create a function that takes a list and prints out the highest even number in the list.

my_list = [13, 23, 10, 61, 33]

   
def highest_even(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0 and num != 0:
            even_numbers.append(num)
    if len(even_numbers) == 0:
        print('There are no even numbers in the list')
        return
    else: 
        max_even = max(even_numbers)
        print(f'{max_even} is the largest even number in the list')
        return max_even

highest_even(my_list)