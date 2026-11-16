import random

class Solution(object):

    def __init__(self, nums):
        self.original = list(nums)
        self.array = list(nums)

    def reset(self):
        self.array = list(self.original)
        return self.array

    def shuffle(self):
        n = len(self.array)
        for i in range(n):
            swap_idx = random.randrange(i, n)
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
