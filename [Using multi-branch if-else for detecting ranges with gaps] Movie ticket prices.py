movie_ticket_price = None

user_age = int(input('Enter your age: '))

if user_age <= 12:     # Age 12 and under
   print('Child ticket discount.')
   movie_ticket_price = 11
elif user_age >= 65:   # Age 65 and older
   print('Senior ticket discount.') 
   movie_ticket_price = 12
else:                  # All other ages
   movie_ticket_price = 14

print(f'Movie ticket price: {movie_ticket_price}')