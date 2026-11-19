class Solution:
    def minOperations(self, k: int) -> int:
        ans = k  # upper bound: v = k, c = 1 gives k - 1
        for v in range(1, k + 1):
            c = (k + v - 1) // v
            ans = min(ans, v - 1 + c - 1)
        return ans
