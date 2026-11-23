class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            freq = [0] * 26
            distinct = 0
            max_freq = 0
            
            for j in range(i - 1, -1, -1):
                idx = ord(s[j]) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                if freq[idx] > max_freq:
                    max_freq = freq[idx]
                    
                if distinct * max_freq == i - j:
                    if dp[j] + 1 < dp[i]:
                        dp[i] = dp[j] + 1
                        
        return dp[n]
