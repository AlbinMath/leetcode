class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        first = [-2] * 32
        first[0] = -1
        mask = 0
        ans = 0

        for j, ch in enumerate(s):
            if ch in bit:
                mask ^= bit[ch]
            if first[mask] != -2:
                ans = max(ans, j - first[mask])
            else:
                first[mask] = j

        return ans
