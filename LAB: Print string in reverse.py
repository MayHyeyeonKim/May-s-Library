# Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# done
# then the output is:

# ereht olleH
# yeH


var1 = str(input())
word = ['done', 'd', 'Done']
while var1 not in word:
    print(var1[::-1])
    var1 = str(input())