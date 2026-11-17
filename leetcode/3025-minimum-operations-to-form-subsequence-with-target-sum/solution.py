class Solution(object):
    def minOperations(self, nums, target):
        if sum(nums) < target:
            return -1
        cnt = [0] * 33
        for x in nums:
            cnt[x.bit_length() - 1] += 1

        ops = 0
        for b in range(32):
            if (target >> b) & 1:
                if cnt[b] == 0:
                    j = b + 1
                    while j < 33 and cnt[j] == 0:
                        j += 1
                    # split 2^j down to 2^b
                    cnt[j] -= 1
                    for t in range(b, j):
                        cnt[t] += 1
                    cnt[b] += 1
                    ops += j - b
                cnt[b] -= 1
            # merge leftover pairs upward
            cnt[b + 1] += cnt[b] // 2
        return ops
