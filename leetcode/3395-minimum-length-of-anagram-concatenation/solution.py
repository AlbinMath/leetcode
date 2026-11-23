from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        total_counts = Counter(s)
        g = reduce(gcd, total_counts.values())
        min_len = n // g
        
        for length in range(min_len, n, min_len):
            if n % length != 0:
                continue
                
            target_freq = Counter(s[:length])
            if all(Counter(s[i : i + length]) == target_freq for i in range(length, n, length)):
                return length
                
        return n
