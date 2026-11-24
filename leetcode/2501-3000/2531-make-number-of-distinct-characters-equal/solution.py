from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        d1, d2 = len(count1), len(count2)
        
        for ch1 in count1:
            for ch2 in count2:
                if ch1 == ch2:
                    if d1 == d2:
                        return True
                else:
                    new_d1 = d1 - (count1[ch1] == 1) + (count1[ch2] == 0)
                    new_d2 = d2 - (count2[ch2] == 1) + (count2[ch1] == 0)
                    if new_d1 == new_d2:
                        return True
                        
        return False
