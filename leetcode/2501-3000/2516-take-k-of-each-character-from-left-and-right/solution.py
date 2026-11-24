class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
            
        total = [s.count('a'), s.count('b'), s.count('c')]
        if min(total) < k:
            return -1
            
        win = [0, 0, 0]
        max_middle = 0
        left = 0
        base = ord('a')
        
        for right, ch in enumerate(s):
            idx = ord(ch) - base
            win[idx] += 1
            
            while win[idx] > total[idx] - k:
                win[ord(s[left]) - base] -= 1
                left += 1
                
            if right - left + 1 > max_middle:
                max_middle = right - left + 1
                
        return len(s) - max_middle
