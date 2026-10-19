# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        cache = {}

        def get(i: int) -> int:
            if i not in cache:
                cache[i] = mountain_arr.get(i)
            return cache[i]

        n = mountain_arr.length()

        # 1. find the peak index
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if get(mid) < get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        # 2. search the ascending part [0, peak]
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            v = get(mid)
            if v == target:
                return mid
            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # 3. search the descending part [peak + 1, n - 1]
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = get(mid)
            if v == target:
                return mid
            if v > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
