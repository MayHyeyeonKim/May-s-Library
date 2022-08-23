class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours}:{self.minutes}'

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

num_times = 3
times = []

# Obtain times from user input
for i in range(num_times):
    user_input = input('Enter time (Hrs:Mins): ')
    tokens = user_input.split(':')
    times.append(Time(int(tokens[0]), int(tokens[1])))

min_time = times[0]
for t in times:
    if t < min_time :
        min_time = t

print('\nEarliest time is', min_time)