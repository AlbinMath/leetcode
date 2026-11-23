class Solution(object):
    def sumImbalanceNumbers(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = [False] * (n + 2)
            seen[nums[i]] = True
            imbalance = 0

            for j in range(i + 1, n):
                x = nums[j]
                if not seen[x]:
                    seen[x] = True
                    if seen[x - 1] and seen[x + 1]:
                        imbalance -= 1
                    elif not seen[x - 1] and not seen[x + 1]:
                        imbalance += 1
                ans += imbalance

        return ans
