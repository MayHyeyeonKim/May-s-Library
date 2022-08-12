#Commonly, a program may need to detect several specific values of a variable.
#An if-else statement can be extended to have three (or more) branches. 
# Each branch's expression is checked in sequence. As soon as one branch's expression is found to be true, 
# that branch's statement executes (and no subsequent branch is considered). 
# If no expression is true, the else branch executes. The example below detects values of 1, 25, or 50 for variable num_years.

if expression1:
   # Statements that execute when expression1 is true
   # (first branch)
elif expression2:
   # Statements that execute when expression1 is false and expression2 is true
   # (second branch)
else:
   # Statements that execute when expression1 is false and expression2 is false
   # (third branch)

