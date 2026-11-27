class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        valid_cols = []
        
        def backtrack(row: int, current: list[int]) -> None:
            if row == m:
                valid_cols.append(tuple(current))
                return
            for color in range(3):
                if row == 0 or current[-1] != color:
                    current.append(color)
                    backtrack(row + 1, current)
                    current.pop()
                    
        backtrack(0, [])
        num_states = len(valid_cols)
        
        adj = [[] for _ in range(num_states)]
        for i in range(num_states):
            for j in range(i + 1, num_states):
                if all(a != b for a, b in zip(valid_cols[i], valid_cols[j])):
                    adj[i].append(j)
                    adj[j].append(i)
                    
        dp = [1] * num_states
        for _ in range(n - 1):
            next_dp = [0] * num_states
            for i in range(num_states):
                total = 0
                for prev in adj[i]:
                    total += dp[prev]
                next_dp[i] = total % MOD
            dp = next_dp
            
        return sum(dp) % MOD
