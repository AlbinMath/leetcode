class Solution(object):
    def doesValidArrayExist(self, derived):
        x = 0
        for d in derived:
            x ^= d
        return x == 0
