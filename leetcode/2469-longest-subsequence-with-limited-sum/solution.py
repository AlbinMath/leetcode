class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        k, total = 0, 0
        for qi in order:
            while k < len(nums) and total + nums[k] <= queries[qi]:
                total += nums[k]
                k += 1
            ans[qi] = k
        return ans
