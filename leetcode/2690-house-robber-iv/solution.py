class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def can(c: int) -> bool:
            count = 0
            i = 0
            while i < n:
                if nums[i] <= c:
                    count += 1
                    if count >= k:
                        return True
                    i += 2
                else:
                    i += 1
            return False

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
