class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        curr_len = 1
        distinct = 1
        max_len = 0
        
        for i in range(1, len(word)):
            if word[i] > word[i - 1]:
                curr_len += 1
                distinct += 1
            elif word[i] == word[i - 1]:
                curr_len += 1
            else:
                curr_len = 1
                distinct = 1
                
            if distinct == 5 and curr_len > max_len:
                max_len = curr_len
                
        return max_len
