from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        unpaired = defaultdict(int)
        length = 0
        sym_unpaired = 0
        
        for word in words:
            rev = word[1] + word[0]
            if unpaired[rev] > 0:
                unpaired[rev] -= 1
                length += 4
                if word == rev:
                    sym_unpaired -= 1
            else:
                unpaired[word] += 1
                if word == rev:
                    sym_unpaired += 1
                    
        if sym_unpaired > 0:
            length += 2
            
        return length
