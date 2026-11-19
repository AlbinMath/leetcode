class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        # runs of identical characters
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append(j - i)
            i = j

        def ok(m: int) -> bool:
            if m == 1:
                mism = sum(ch != str(i & 1) for i, ch in enumerate(s))
                return min(mism, n - mism) <= numOps
            return sum(L // (m + 1) for L in runs) <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
