class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        previous = -1

        for i, num in enumerate(nums):
            if num == 1:
                if previous != -1 and i - previous <= k:
                    return False

                previous = i

        return True
