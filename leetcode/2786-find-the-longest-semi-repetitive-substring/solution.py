class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        last_pair_idx = 0
        max_len = 1
        
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                if last_pair_idx > 0:
                    left = last_pair_idx
                last_pair_idx = right
            if right - left + 1 > max_len:
                max_len = right - left + 1
                
        return max_len
