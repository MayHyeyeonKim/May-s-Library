# Loops are commonly used to process a series of input values. 
# A sentinel value is used to terminate a loop's processing. 
# The example below computes the average of an input list of positive integers, 
# ending with 0. The 0 is not included in the average.

'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5
'''

values_sum = 0
num_values = 0

curr_value = int(input())
   
while curr_value > 0: # Get values until 0 (or less)
    values_sum += curr_value
    num_values += 1
    curr_value = int(input())

print(f'Average: {values_sum / num_values:.0f}\n')
