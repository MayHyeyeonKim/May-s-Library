# The below program uses a for loop to calculate savings and interest.
# Try changing the range() function to print every three years instead,
# using the three-argument alternate version of range().
# Modify the interest calculation inside the loop to compute three years
# worth of savings instead of one.

'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(f' Savings in year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)

print('\n')
