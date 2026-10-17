import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        i = self.idx[val].pop()
        last = self.nums[-1]
        last_pos = len(self.nums) - 1
        self.nums[i] = last
        self.idx[last].add(i)
        self.idx[last].discard(last_pos)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
