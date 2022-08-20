'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(f' Savings at beginning of year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')
