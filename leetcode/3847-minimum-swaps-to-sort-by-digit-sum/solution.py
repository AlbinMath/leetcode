class Solution:
    def minSwaps(self, nums):
        a = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(nums)}
        p = [pos[x] for x in a]
        ans = 0
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                ans += 1
        return ans
