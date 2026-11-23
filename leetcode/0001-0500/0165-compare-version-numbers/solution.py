from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for a, b in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            x, y = int(a), int(b)
            if x < y:
                return -1
            if x > y:
                return 1
        return 0
