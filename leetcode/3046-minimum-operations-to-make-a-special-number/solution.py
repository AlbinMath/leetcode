class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n - 1 if '0' in num else n   # reduce to "0" or to empty (= 0)

        for p, q in ("00", "25", "50", "75"):
            j = num.rfind(q)
            if j <= 0:
                continue
            i = num.rfind(p, 0, j)
            if i != -1:
                ans = min(ans, n - i - 2)
        return ans
