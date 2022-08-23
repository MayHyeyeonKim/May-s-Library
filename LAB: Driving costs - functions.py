# Write a function driving_cost() with input parameters miles_per_gallon, dollars_per_gallon, and miles_driven, that returns the dollar cost to drive those miles. All items are of type float. The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.

# Define that function in a program whose inputs are the car's miles per gallon and the price of gas in dollars per gallon (both float). Output the gas cost for 10 miles, 50 miles, and 400 miles, by calling your driving_cost() function three times.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')

# Ex: If the input is:

# 20.0
# 3.1599
# the output is:

# 1.58
# 7.90
# 63.20
# Your program must define and call a function:
# def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return dollars_per_gallon / miles_per_gallon * miles_driven


def input_compute_and_print():
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    miles = [10, 50, 400]
    for i in miles:
        print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, i):.2f}')


def print_example():
    cost = driving_cost(20.0,3.1599, 50.0)
    print(f'{cost:.2f}')


if __name__ == '__main__':
    input_compute_and_print()
