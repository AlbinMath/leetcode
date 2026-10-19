import math
import random
from typing import List

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.cx = x_center
        self.cy = y_center

    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2 * math.pi)
        d = self.r * math.sqrt(random.random())
        return [self.cx + d * math.cos(theta),
                self.cy + d * math.sin(theta)]
