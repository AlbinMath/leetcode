class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        curr_cost = 0
        
        for right in range(len(s)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            if curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
                
        return len(s) - left
