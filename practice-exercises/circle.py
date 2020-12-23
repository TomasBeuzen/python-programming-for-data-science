import math

class Circle:
    """A circle with a radius r."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2.0 * math.pi * self.radius

    def __str__(self):
        return f"A Circle with radius {self.radius}"