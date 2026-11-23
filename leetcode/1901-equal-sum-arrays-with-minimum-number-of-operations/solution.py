class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s2 - s1

        gains = [0] * 6
        for x in nums1:
            gains[6 - x] += 1      # raise to 6
        for y in nums2:
            gains[y - 1] += 1      # lower to 1

        ops = 0
        for g in range(5, 0, -1):
            if diff <= 0:
                break
            # number of ops with gain g needed, capped by availability
            need = (diff + g - 1) // g
            use = min(need, gains[g])
            ops += use
            diff -= use * g
        return ops if diff <= 0 else -1
