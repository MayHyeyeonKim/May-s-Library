# Complete the __gt__ method. A quarterback is considered greater than another only if that quarterback has both more wins and a higher quarterback passer rating.

# Once __gt__ is complete, compare Tom Brady's 2007 stats as well (yards: 4806, TDs: 50, completions: 398, attempts: 578, interceptions: 8, wins: 16).

class Quarterback:
    def __init__(self, yrds, tds, cmps, atts, ints, wins):
        self.wins = wins

        # Calculate quarterback passer rating (NCAA)
        self.rating = ((8.4*yrds) + (330*tds) + (100*cmps) - (200 * ints))/atts

    def __lt__(self, other):
        if (self.rating < other.rating) or (self.wins < other.wins):
            return True
        return False

    def __gt__(self, other):
        return True
        # Complete the method...

peyton = Quarterback(yrds=4700, atts=679, cmps=450, tds=33, ints=17, wins=10)
eli = Quarterback(yrds=4002, atts=539, cmps=339, tds=31, ints=25, wins=9)

if peyton > eli:
    print('Peyton is the better QB')
elif peyton < eli:
    print('Eli is the better QB')
else:
    print('It is not clear who the better QB is...')
