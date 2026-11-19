class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        diff = 0
        min_flips = n
        
        for i in range(2 * n):
            curr = s[i if i < n else i - n]
            if int(curr) != (i & 1):
                diff += 1
                
            if i >= n:
                left = i - n
                if int(s[left]) != (left & 1):
                    diff -= 1
                    
            if i >= n - 1:
                min_flips = min(min_flips, diff, n - diff)
                
        return min_flips
