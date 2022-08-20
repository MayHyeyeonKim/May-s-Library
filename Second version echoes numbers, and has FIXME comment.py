
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
    if '0' <= character <= '9':
        phone_number += character
    else:
        #FIXME: Add elif branches for letters and hyphen
        phone_number += '?'

print(f'Numbers only: {phone_number}')