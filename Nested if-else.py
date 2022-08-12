user_choice = 2  # Hardcoded values for this tool. Could be input()...
num_items = 5
	
if user_choice == 1:    
	    print('user_choice is 1')
elif user_choice == 2:
    if num_items < 0:
        print('user_choice is 2 and num_items < 0')
    else:
        print('user_choice is 2 and num_items >= 0')
else:
    print('user_choice is neither 1 or 2')
    

