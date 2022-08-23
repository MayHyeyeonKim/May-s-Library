class MarathonRunner:
    race_distance = 42.195  # Marathon distance in Kilometers

    def __init__(self):
        self.speed = 0
        # ...

    def get_speed(self):
        # ...

runner1 = MarathonRunner()
runner1.speed = 7.5

runner2 = MarathonRunner()
runner2.speed = 8.0

print('Runner 1 speed:', runner1.speed)
print('Runner 2 speed:', runner2.speed)
