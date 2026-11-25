class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first = {0: -1}
        s = 0
        for j, v in enumerate(nums):
            s = (s + v) % k
            if s in first:
                if j - first[s] >= 2:
                    return True
            else:
                first[s] = j
        return False
