import random
from typing import List


class Solution:
    """
    This solution randomly generates samples within a rectangle surrounding
    the circle and rejects samples that are outside the circle until a valid
    sample within the circle is found.
    """
    def __init__(self,
                 radius: float,
                 x_center: float,
                 y_center: float) -> None:
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:

        # Square radius to avoid expensive math.sqrt call in loop
        radius_squared = self.radius ** 2

        while True:

            x = self.x + random.uniform(-self.radius, self.radius)
            y = self.y + random.uniform(-self.radius, self.radius)

            if ((x - self.x) ** 2 + (y - self.y) ** 2) <= radius_squared:
                return [x, y]
