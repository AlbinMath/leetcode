class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for w in stones:
            for s in range(target, w - 1, -1):
                if dp[s - w]:
                    dp[s] = True
                    
        for s in range(target, -1, -1):
            if dp[s]:
                return total_sum - 2 * s
                
        return 0
