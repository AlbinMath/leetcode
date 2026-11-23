from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        keys = sorted(cnt)
        ans = []
        while len(ans) < len(nums):
            for k in keys:
                if cnt[k] > 0:
                    ans.append(k)
                    cnt[k] -= 1
        return ans
