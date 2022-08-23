# Define a function calc_total_inches, with parameters num_feet and num_inches, 
# that returns the total number of inches. Note: There are 12 inches in a foot. 
# Sample output with inputs: 5 8
# Total inches: 68

def calc_total_inches(feet, inches):
    result = feet * 12 + inches
    return result

feet = int(input())
inches = int(input())
print('Total inches:', calc_total_inches(feet, inches))

