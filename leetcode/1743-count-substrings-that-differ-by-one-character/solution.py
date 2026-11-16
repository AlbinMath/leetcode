class Solution(object):
    def countSubstrings(self, s, t):
        m, n = len(s), len(t)
        total = 0
        
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    left = 1
                    while i - left >= 0 and j - left >= 0 and s[i - left] == t[j - left]:
                        left += 1
                    
                    right = 1
                    while i + right < m and j + right < n and s[i + right] == t[j + right]:
                        right += 1
                    
                    total += left * right
                    
        return total
