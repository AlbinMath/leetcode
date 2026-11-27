class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        NEG_INF = float('-inf')
        dp = [NEG_INF] * (target + 1)
        dp[0] = 0
        
        for t in range(1, target + 1):
            for c in cost:
                if t >= c and dp[t - c] + 1 > dp[t]:
                    dp[t] = dp[t - c] + 1
                    
        if dp[target] < 0:
            return "0"
            
        res = []
        rem = target
        for d in range(9, 0, -1):
            c = cost[d - 1]
            while rem >= c and dp[rem] == dp[rem - c] + 1:
                res.append(str(d))
                rem -= c
                
        return "".join(res)
