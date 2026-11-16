import random

class Solution(object):

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.rem = self.total
        self.flipped = {}

    def flip(self):
        r = random.randint(0, self.rem - 1)
        self.rem -= 1
        
        actual = self.flipped.get(r, r)
        self.flipped[r] = self.flipped.get(self.rem, self.rem)
        
        return [actual // self.n, actual % self.n]

    def reset(self):
        self.rem = self.total
        self.flipped.clear()
