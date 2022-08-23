class Time:
    gmt_offset = 0  # Class attribute. Changing alters print_time output
    
    def __init__(self):  # Methods are a class attribute too
        self.hours = 0  # Instance attribute
        self.minutes = 0  # Instance attribute

    def print_time(self):  # Methods are a class attribute too
        offset_hours = self.hours + self.gmt_offset  # Local variable
        
        print(f'Time -- {offset_hours}:{self.minutes}')

time1 = Time()
time1.hours = 10
time1.minutes = 15

time2 = Time()
time2.hours = 12
time2.minutes = 45

print ('Greenwich Mean Time (GMT):')
time1.print_time()
time2.print_time()

Time.gmt_offset = -8  # Change to PST time (-8 GMT)

print('\nPacific Standard Time (PST):')
time1.print_time()
time2.print_time()