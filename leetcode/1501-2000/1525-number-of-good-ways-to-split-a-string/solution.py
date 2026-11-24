from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        right = Counter(s)
        right_distinct = len(right)
        left = set()
        ans = 0

        for ch in s[:-1]:
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                right_distinct -= 1
            if len(left) == right_distinct:
                ans += 1

        return ans
