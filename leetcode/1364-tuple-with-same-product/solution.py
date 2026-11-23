from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                cnt[nums[i] * nums[j]] += 1
        return sum(4 * m * (m - 1) for m in cnt.values())
