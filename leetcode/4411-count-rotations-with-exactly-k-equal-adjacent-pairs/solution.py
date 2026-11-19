class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for r in range(n):
            t = s[r:] + s[:r]
            score = sum(t[i] == t[i + 1] for i in range(n - 1))
            if score == k:
                ans += 1
        return ans
