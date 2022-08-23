class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


my_time = Time()
my_time.hours = 7
my_time.minutes = 15

print(f'{my_time.hours} hours', end=' ')
print(f'and {my_time.minutes} minutes')