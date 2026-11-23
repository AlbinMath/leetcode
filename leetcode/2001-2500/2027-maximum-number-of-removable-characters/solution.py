class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        INF = len(removable) + 1
        removed_at = [INF] * n
        for step, idx in enumerate(removable):
            removed_at[idx] = step

        def ok(k: int) -> bool:
            j = 0
            m = len(p)
            for i in range(n):
                if removed_at[i] < k:
                    continue
                if s[i] == p[j]:
                    j += 1
                    if j == m:
                        return True
            return False

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
