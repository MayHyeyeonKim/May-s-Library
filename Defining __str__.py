# Write the special method __str__() for CarRecord.

# Sample output with input: 2009 'ABC321'
# Year: 2009, VIN: ABC321

class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    # FIXME add __str__()

    def __str__(self):
        return f"Year: {self.year_made}, VIN: {self.car_vin}"

my_car = CarRecord()
my_car.year_made = int(input())
my_car.car_vin = input()

print(my_car)