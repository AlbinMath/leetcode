class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(target + 1)]
        
        if houses[0] != 0:
            dp[1][houses[0]] = 0
        else:
            for c in range(1, n + 1):
                dp[1][c] = cost[0][c - 1]
                
        for i in range(1, m):
            next_dp = [[INF] * (n + 1) for _ in range(target + 1)]
            max_k = min(i + 1, target)
            
            for k in range(1, max_k + 1):
                min1 = min2 = INF
                min1_color = -1
                if k > 1:
                    for c in range(1, n + 1):
                        val = dp[k - 1][c]
                        if val < min1:
                            min2 = min1
                            min1 = val
                            min1_color = c
                        elif val < min2:
                            min2 = val
                            
                colors = [houses[i]] if houses[i] != 0 else range(1, n + 1)
                
                for c in colors:
                    paint_cost = 0 if houses[i] != 0 else cost[i][c - 1]
                    
                    best_prev = dp[k][c]
                    
                    if k > 1:
                        diff_color_cost = min2 if c == min1_color else min1
                        if diff_color_cost < best_prev:
                            best_prev = diff_color_cost
                            
                    if best_prev < INF:
                        next_dp[k][c] = paint_cost + best_prev
                        
            dp = next_dp
            
        ans = min(dp[target][1:])
        return ans if ans < INF else -1
