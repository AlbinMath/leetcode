class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = [0] * 26
        base = ord('a')
        
        for ch in s:
            diff[ord(ch) - base] += 1
            
        for ch in t:
            diff[ord(ch) - base] -= 1
            
        return sum(abs(count) for count in diff)
