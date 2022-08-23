# Normal printing

class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age


truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)

# <__main__.Toy instance at 0xb74cb98c>

# Customized printing
class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age

    def __str__(self):
        return (f'{self.name} costs only ${self.price:.2f}.'
                f' Not for children under {self.min_age}!')

truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)

# Monster Truck XX costs only $14.99. Not for children under 5!

