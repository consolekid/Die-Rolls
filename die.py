from random import randint

class Die:
    """A class to represent a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """return a random value between q and number of sides."""
        return randint(1, self.num_sides)
