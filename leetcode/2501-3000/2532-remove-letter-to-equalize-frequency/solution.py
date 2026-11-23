from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        
        for ch in list(freq.keys()):
            freq[ch] -= 1
            remaining = {count for count in freq.values() if count > 0}
            
            if len(remaining) == 1:
                return True
                
            freq[ch] += 1
            
        return False
