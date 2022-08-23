def __sub__(self, other):
    if isinstance(other, int): # right op is integer
        return Time24(self.hours - other, self.minutes)

    if isinstance(other, Time24):  # right op is Time24
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

    print(f'{type(other)} unsupported')
    raise NotImplementedError