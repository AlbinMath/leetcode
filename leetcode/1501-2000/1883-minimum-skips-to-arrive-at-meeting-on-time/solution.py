class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        target = hoursBefore * speed
        
        if sum(dist) > target:
            return -1
            
        INF = float('inf')
        dp = [INF] * n
        dp[0] = 0
        
        for i, d in enumerate(dist):
            if i == n - 1:
                for j in range(i + 1):
                    dp[j] += d
            else:
                for j in range(i + 1, -1, -1):
                    no_skip = ((dp[j] + d + speed - 1) // speed) * speed if dp[j] < INF else INF
                    
                    with_skip = dp[j - 1] + d if j > 0 else INF
                    
                    dp[j] = no_skip if no_skip < with_skip else with_skip
                    
        for j in range(n):
            if dp[j] <= target:
                return j
                
        return -1
