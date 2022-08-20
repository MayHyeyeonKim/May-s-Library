# "Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) 
# and the user must repeat the sequence. 
# Create a for loop that compares each character of the two strings. 
# For each matching character, add one point to user_score. Upon a mismatch, end the loop.

# Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
# User score: 4

user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in simon_pattern:
   if user_pattern[user_score] == simon_pattern[user_score]:
      user_score += 1
   else:
      break

print('User score:', user_score)
