
import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        # Get the index of the value to remove
        idx = self.indices[val]

        # Get the last element
        last = self.nums[-1]

        # Move the last element into the removed element's position
        self.nums[idx] = last
        self.indices[last] = idx

        # Remove the last element
        self.nums.pop()
        del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

