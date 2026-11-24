from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        cnt = Counter(s)
        
        if all(cnt[c] <= target for c in "QWER"):
            return 0
            
        min_len = n
        left = 0
        
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while all(cnt[c] <= target for c in "QWER"):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cnt[s[left]] += 1
                left += 1
                
        return min_len
