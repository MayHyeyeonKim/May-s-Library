class MarathonRunner:
    race_distance = 42.195  # Marathon distance in Kilometers

    def __init__(self):
        # ...

    def get_speed(self):
        # ...

runner1 = MarathonRunner()
runner2 = MarathonRunner()

print(MarathonRunner.race_distance)  # Look in class namespace
print(runner1.race_distance)  # Look in instance namespace
print(runner2.race_distance)
