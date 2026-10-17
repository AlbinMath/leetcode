class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)
        for m in range(60, 1, -1):
            lo, hi = 2, int(N ** (1.0 / m)) + 2
            while lo < hi:
                mid = (lo + hi) // 2
                if mid ** m >= N:
                    hi = mid
                else:
                    lo = mid + 1
            # candidates: lo and lo - 1 (root guess may be off by one)
            for k in (lo - 1, lo):
                if k >= 2 and (k ** (m + 1) - 1) // (k - 1) == N:
                    return str(k)
        return str(N - 1)
