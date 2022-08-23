# The problem below uses the function get_numbers() 
# to read a number of integers from the user. 
# Three unfinished functions are defined, which should print only certain types of numbers that the user entered. 
# Complete the unfinished functions, adding loops and branches where necessary. 
# Match the output with the below sample:


size = 5

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:')

def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:')

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)