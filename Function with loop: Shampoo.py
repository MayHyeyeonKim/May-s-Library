# Write a function print_shampoo_instructions() with parameter num_cycles. 
# If num_cycles is less than 1, print "Too few.". If more than 4, print "Too many.". 
# Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, 
# followed by "Done.".

# Sample output with input: 2
# 1 : Lather and rinse.
# 2 : Lather and rinse.
# Done.
 
# Hint: Define and use a loop variable. 

def print_shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        for i in range(1, num_cycles+1, 1):
            print(i, ': Lather and rinse.')
        print('Done.')

user_cycles = int(input())
print_shampoo_instructions(user_cycles)