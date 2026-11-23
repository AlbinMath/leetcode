class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        cnt = [0] * 60
        ans = 0
        for t in time:
            r = t % 60
            ans += cnt[(60 - r) % 60]
            cnt[r] += 1
        return ans
