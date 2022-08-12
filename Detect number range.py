#Write an expression that prints "Eligible" if user_age is between 18 and 25 inclusive. 
#Ex: 17 prints "Ineligible", 18 prints "Eligible". 


user_age = int(input())

if  (user_age >=18)and(user_age<=25):
    print('Eligible')
else:
    print('Ineligible')