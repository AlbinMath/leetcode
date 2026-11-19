class Solution:
    def longestAwesome(self, s: str) -> int:
        first = [None] * 1024
        first[0] = -1
        mask = 0
        ans = 0

        for j, ch in enumerate(s):
            mask ^= 1 << (ord(ch) - 48)

            if first[mask] is not None:
                ans = max(ans, j - first[mask])
            else:
                first[mask] = j

            for d in range(10):
                i = first[mask ^ (1 << d)]
                if i is not None:
                    ans = max(ans, j - i)

        return ans
