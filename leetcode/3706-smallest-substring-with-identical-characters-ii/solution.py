class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        # run lengths
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
                # target 0101... : mismatches where s[i] != i % 2
                c = sum(1 for i, ch in enumerate(s) if int(ch) != i % 2)
                return min(c, n - c) <= numOps
            need = 0
            for L in runs:
                need += L // (m + 1)
                if need > numOps:
                    return False
            return True

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
