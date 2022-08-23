class Employee:
    def __init__(self, name, wage=8.25, hours=20):
        """
        Default employee is part time (20 hours/week)
        and earns minimum wage
        """
        self.name = name
        self.wage = wage
        self.hours = hours

    # ...


todd = Employee('Todd')  # Typical part-time employee
jason = Employee('Jason')  # Typical part-time employee
tricia = Employee('Tricia', wage=12.50, hours=40)  # Manager employee

employees = [todd, jason, tricia]

for e in employees:
    print (f'{e.name} earns {e.wage*e.hours:.2f} per week')