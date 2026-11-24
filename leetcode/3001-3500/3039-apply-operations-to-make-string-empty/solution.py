from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = Counter(s)
        max_freq = max(freq.values())
        
        seen = set()
        result = []
        
        for ch in reversed(s):
            if freq[ch] == max_freq and ch not in seen:
                seen.add(ch)
                result.append(ch)
                
        return "".join(reversed(result))
