class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay():  # Programmer forgot self parameter
        return self.wage * self.hours_worked


alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice earned {alice.calculate_pay():.2f}')


# Traceback (most recent call last):
#   File "<stdin>", line 13, in <module>
# TypeError: calculate_pay() takes 0 positional arguments but 1 was given
