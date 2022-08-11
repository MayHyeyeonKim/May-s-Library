#A 'Mad Libs' style game where user enters nouns,
#verbs, etc., and then a story using those words is output.

#Get user's words
relative = input('Enter a type of relative: ')
print()

food = input('Enter a type of food: ')
print()

adjective = input('Enter an adjective: ')
print()

period = input('Enter a time period: ')
print()

# Tell the story
print('My', relative, 'says eating', food)
print('will make me more', adjective)
print('so now I eat them every', period)
