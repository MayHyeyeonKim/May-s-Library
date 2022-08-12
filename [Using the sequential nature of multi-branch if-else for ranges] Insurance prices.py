user_age = int(input('Enter your age: '))

if user_age < 16:          # Age 15 and under
   print('Too young.')
   insurance_price = 0

elif user_age < 25:        # Age 16 - 24
   insurance_price = 4800

elif user_age < 40:         # Age 25 - 39
   insurance_price = 2350

else:                      # Age 40 and up
   insurance_price = 2100

print('Annual price: $', insurance_price)