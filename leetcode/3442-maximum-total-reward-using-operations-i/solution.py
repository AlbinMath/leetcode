class Solution(object):
    def maxTotalReward(self, rewardValues):
        dp = 1  # total reward 0 is reachable
        for v in sorted(set(rewardValues)):
            dp |= (dp & ((1 << v) - 1)) << v
        return dp.bit_length() - 1
