# The following program allows the user to enter a phone number that includes letters, 
# which appear on phone keypads along with numbers and are commonly used by companies 
# as a marketing tactic (e.g., 1-555-HOLIDAY). 
# The program then outputs the phone number using numbers only.

# The first program version simply prints each element of the string to ensure 
# the loop iterates properly through each string element.

user_input = input('Enter phone number: ')

index = 0
for character in user_input:
    print(f'Element {index} is: {character}')
    index += 1