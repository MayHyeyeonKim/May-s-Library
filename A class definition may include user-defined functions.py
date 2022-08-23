class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def print_time(self):
        print('Hours:', self.hours, end=' ')
        print('Minutes:', self.minutes)


time1 = Time()
time1.hours = 7
time1.minutes = 15
time1.print_time()