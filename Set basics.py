#Given the user inputs, complete a program that does the following tasks:

#Define a set, fruits, containing the user inputs: my_fruit1, my_fruit2, and my_fruit3.
#Add the user inputs, your_fruit1 and your_fruit2, to fruits.
#Add the user input, their_fruit, to fruits.
#Add your_fruit1 to fruits.
#Remove my_fruit1 from fruits.
#Observe the output of each print statement carefully to understand what was done by each task of the program.

#Note: For testing purposes, sets are printed using sorted() for comparison, as in the book's examples.

#Ex: If the input is:

#apple
#peach
#lemon
#apple
#pear
#plum
#the output is:

#['apple', 'lemon', 'peach']
#['apple', 'lemon', 'peach', 'pear']
#['apple', 'lemon', 'peach', 'pear', 'plum']
#['apple', 'lemon', 'peach', 'pear', 'plum']
#['lemon', 'peach', 'pear', 'plum']




my_fruit1 = input()
my_fruit2 = input()
my_fruit3 = input()

your_fruit1 = input()
your_fruit2 = input()

their_fruit = input()

# 1. TODO: Define a set, fruits, containing my_fruit1, my_fruit2, and my_fruit3
fruits = {my_fruit1, my_fruit2, my_fruit3}
print(sorted(fruits))

# 2. TODO: Add your_fruit1 and your_fruit2 to fruits
fruits.add(your_fruit1)
fruits.add(your_fruit2)
print(sorted(fruits))

# 3. TODO: Add their_fruit to fruits
fruits.add(their_fruit)
print(sorted(fruits))

# 4. TODO: Add your_fruit1 to fruits
fruits.add(your_fruit1)
print(sorted(fruits))

# 5. TODO: Remove my_fruit1 from fruits
fruits.remove(my_fruit1)
print(sorted(fruits))
