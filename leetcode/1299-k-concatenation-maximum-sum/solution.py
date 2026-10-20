class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        total = sum(arr)
        s = best = 0
        for x in arr * min(k, 2):
            s = max(0, s + x)
            best = max(best, s)
        return (best + max(0, total) * (k - 2)) % mod if k > 2 else best % mod
