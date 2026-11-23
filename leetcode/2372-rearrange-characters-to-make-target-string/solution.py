from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)
        
        return min(s_counts[ch] // req for ch, req in target_counts.items())
