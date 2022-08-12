#A cable TV provider may have regular channels numbered 2-499, 
#and high-definition channels numbered 1002-1499. 
#A program may set a character variable to 's' for standard, 
#'h' for high-definition, and 'e' for error.


if (user_channel >= 2) and (user_channel <= 499):
   channel_type = 's'
elif (user_channel >= 1002) and (user_channel <= 1499):
   channel_type = 'h'
else:
   channel_type = 'e'
print('Channel type:', channel_type)