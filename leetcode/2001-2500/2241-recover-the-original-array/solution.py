from collections import Counter

class Solution(object):
    def recoverArray(self, nums):
        nums.sort()
        n2 = len(nums)
        base_counts = Counter(nums)

        for i in range(1, n2 // 2 + 1):
            diff = nums[i] - nums[0]
            if diff == 0 or diff % 2 != 0:
                continue
            if i > 1 and nums[i] == nums[i - 1]:
                continue

            k = diff // 2
            counts = base_counts.copy()
            ans = []
            valid = True

            for x in nums:
                if counts[x] == 0:
                    continue
                if counts[x + diff] == 0:
                    valid = False
                    break
                counts[x] -= 1
                counts[x + diff] -= 1
                ans.append(x + k)

            if valid:
                return ans

        return []
