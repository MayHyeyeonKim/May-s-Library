# Given num_rows and num_cols, print a list of all seats in a theater. 
# Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.

# Sample output with inputs: 2 3
# 1A 1B 1C 2A 2B 2C 


num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces


rows = 1                       #create a number to start counting from for rows
while rows <= num_rows:        #start iterating through number of rows
    cols = 1                   #create a number to start counting from for columns
    alpha = 'A'                #starting point for alphabet
    while cols <= num_cols:                    #iterates through number of columns
        print('%s%s' % (rows, alpha), end=' ')
        cols +=1                               #number of columns needs to increase
        alpha = chr(ord(alpha) + 1)            #alphabet needs to increase
    rows += 1 


print()

