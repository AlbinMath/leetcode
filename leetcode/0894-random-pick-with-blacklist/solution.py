import random

class Solution(object):

    def __init__(self, n, blacklist):
        self.m = n - len(blacklist)
        self.mapping = {}
        black_set = set(blacklist)
        
        last = n - 1
        for b in blacklist:
            if b < self.m:
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        r = random.randrange(self.m)
        return self.mapping.get(r, r)
