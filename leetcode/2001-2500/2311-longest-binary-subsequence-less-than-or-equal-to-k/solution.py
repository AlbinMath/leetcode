class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        bit = 1
        for c in reversed(s):
            if c == '0':
                count += 1
            elif bit <= k and value + bit <= k:
                value += bit
                count += 1
            if bit <= k:
                bit <<= 1
        return count
