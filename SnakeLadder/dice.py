import random
class Dice:
    def __init__(self, min_value, max_value):
        self.max_value = max_value
        self.min_value = min_value
    def roll(self):
        return random.randint(self.min_value, self.max_value)