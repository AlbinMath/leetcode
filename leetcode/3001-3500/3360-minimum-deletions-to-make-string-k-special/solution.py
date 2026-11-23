from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(Counter(word).values())
        min_deletions = len(word)
        
        for base in freqs:
            deletions = 0
            max_allowed = base + k
            
            for f in freqs:
                if f < base:
                    deletions += f
                elif f > max_allowed:
                    deletions += f - max_allowed
                    
            if deletions < min_deletions:
                min_deletions = deletions
                
        return min_deletions
