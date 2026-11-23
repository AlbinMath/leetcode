class Solution(object):
    def canSortArray(self, nums):
        prev_max = 0
        i = 0
        n = len(nums)
        while i < n:
            pc = bin(nums[i]).count('1')
            lo = hi = nums[i]
            j = i + 1
            while j < n and bin(nums[j]).count('1') == pc:
                lo = min(lo, nums[j])
                hi = max(hi, nums[j])
                j += 1
            if lo < prev_max:
                return False
            prev_max = hi
            i = j
        return True
