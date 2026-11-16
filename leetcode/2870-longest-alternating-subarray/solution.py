class Solution(object):
    def alternatingSubarray(self, nums):
        max_len = -1
        curr_len = 0
        expected_diff = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if curr_len > 0 and diff == expected_diff:
                curr_len += 1
                expected_diff = -expected_diff
                max_len = max(max_len, curr_len)
            elif diff == 1:
                curr_len = 2
                expected_diff = -1
                max_len = max(max_len, 2)
            else:
                curr_len = 0

        return max_len
