
class Solution:
    def countQuadruplets(self, nums):
        n = len(nums)
        ans = 0
        freq = [0] * (n + 1)

        for j in range(n):
            less = [0] * (n + 1)
            count = 0

            for v in range(1, n + 1):
                less[v] = count
                count += freq[v]

            right_greater = sum(
                1 for k in range(j + 1, n)
                if nums[k] > nums[j]
            )

            for k in range(j + 1, n):
                if nums[k] > nums[j]:
                    right_greater -= 1
                elif nums[k] < nums[j]:
                    ans += less[nums[k]] * right_greater

            freq[nums[j]] += 1

        return ans

