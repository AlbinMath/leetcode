class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        
        for r in rods:
            new_dp = dp.copy()
            for diff, short in dp.items():
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), short)
                new_diff = abs(diff - r)
                new_short = short + min(diff, r)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_short)
                
            dp = new_dp
            
        return dp[0]
