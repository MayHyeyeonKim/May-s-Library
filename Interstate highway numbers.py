#Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

#Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

#Ex: If the input is:

#90
#the output is:

#I-90 is primary, going east/west.
#Ex: If the input is:

#290
#the output is:

#I-290 is auxiliary, serving I-90, going east/west.
#Ex: If the input is:

#0
#the output is:

#0 is not a valid interstate highway number. 
#Ex: If the input is:

#200
#the output is:

#200 is not a valid interstate highway number. 



highway_number = int(input(''))

if highway_number >= 1 and highway_number <= 99:
    prim = 'is primary,'
    if (highway_number % 2) == 0:
        print('I-'+str(highway_number), prim, 'going east/west.')
    else:
        print('I-' + str(highway_number), prim, 'going north/south.')
elif highway_number >= 100 and highway_number <= 999:
    aux = 'is auxiliary,'
    if (highway_number % 100) == 0:
        print(highway_number, 'is not a valid interstate highway number.')
    elif (highway_number % 2) == 0:
        print('I-'+ str(highway_number), aux, 'serving I-%d, going east/west.' % (highway_number%100))
    else:
        print('I-' + str(highway_number), aux, 'serving I-%d, going north/south.' % (highway_number%100))
else:
    print(highway_number, 'is not a valid interstate highway number.')
    