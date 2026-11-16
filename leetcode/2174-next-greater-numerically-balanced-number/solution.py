from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = n + 1
        while True:
            c = Counter(str(x))
            if all(int(d) == k for d, k in c.items()):
                return x
            x += 1
