class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        s = 0
        best = 0
        for j, v in enumerate(nums):
            s += 1 if v else -1
            if s in first:
                best = max(best, j - first[s])
            else:
                first[s] = j
        return best
