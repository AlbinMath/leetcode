class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for x in nums:
            nd = {}
            for s, c in dp.items():
                nd[s + x] = nd.get(s + x, 0) + c
                nd[s - x] = nd.get(s - x, 0) + c
            dp = nd
        return dp.get(target, 0)
