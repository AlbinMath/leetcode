
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        ans = 0

        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
            ans += min(last) + 1

        return ans

