class Time24:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'

    def __gt__(self, other): 
        if self.hours > other.hours: 
            return True 
        else: 
            if self.hours == other.hours: 
                if self.minutes > other.minutes: 
                    return True 
        return False

    def __sub__(self, other):
        """ Calculate absolute distance between two times """
        if self > other:
            larger = self
            smaller = other
        else:
            larger = other
            smaller = self

        hrs = larger.hours - smaller.hours
        mins = larger.minutes - smaller.minutes
        if mins < 0:
            mins += 60
            hrs -=1

        # Check if times wrap to new day
        if hrs > 12:
            hrs = 24 - (hrs + 1)
            mins = 60 - mins

        # Return new Time24 instance 
        return Time24(hrs, mins)

t1 = input('Enter time1 (hours:minutes): ')
tokens = t1.split(':')
time1 = Time24(int(tokens[0]), int(tokens[1]))

t2 = input('Enter time2 (hours:minutes): ')
tokens = t2.split(':')
time2 = Time24(int(tokens[0]), int(tokens[1]))

print('Time difference:', time1 - time2)