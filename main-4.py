import math
x = float(input())
y = float(input())
z = float(input())

your_value1 = x**z
your_value2 = x**(y**z)
your_value3 = abs(x-y)
your_value4 = math.sqrt(x**z)

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')
