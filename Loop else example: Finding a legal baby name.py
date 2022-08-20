# The country of Denmark allows parents to pick from around 7,000 names for newborn infants. Names not on the list must receive special approval from the Names Investigation Department of Copenhagen University. (Surprisingly, many countries have naming laws, probably to avoid names like "Brfxxccxxmnpcccclllmmnprxvclmnckssqlbb11116", pronounced "Albin".)

#The program below checks if a user-entered name is an appropriate Danish name. If the name is not found in the list of legal names, then a suggestion is made to a close match. If no close matches are found, the loop else clause informs the user. Note that the program uses a function called edit_distance, which calculates string edit distance, or how many characters are different between two strings. For example, the edit distance of "DOG" and "DIG" is 1, because changing the middle character would make the strings equivalent.
# 
# Run the program below.
# 
# Enter the acceptable name "Bjork".
# Try the name "Michaal", which is not an acceptable name – the program will suggest a replacement based on the edit distance.
# Try the name "Zoidberg", which is not close at all to any acceptable Danish names – the program will print a special message and terminate.

import edit_distance

#A few legal, acceptable Danish names
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn', 
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne', 
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia', 
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne', 
    'Dorte'
]

user_name = input('Enter desired name:\n')
if user_name in legal_names:
    print(f'{user_name} is an acceptable Danish name. Congratulations.')
else:
    print(f'{user_name} is not acceptable.')
    for name in legal_names:
        if edit_distance.distance(name, user_name)  < 2:
            print(f'You might consider: {name},', end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')
