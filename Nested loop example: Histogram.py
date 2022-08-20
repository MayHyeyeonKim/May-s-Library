# Here is a nested loop example that graphically depicts an integer's magnitude by using asterisks, 
# creating what is commonly called a histogram:

# Run the program below and observe the output. 
# Modify the program to print one asterisk per 5 units. So if the user enters 40, print 8 asterisks.

num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(num):
            print('*', end=' ')
        print('\n')

print('Goodbye.')