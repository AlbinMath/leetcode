class Solution:
    def mostWordsFound(self, sentences):
        return max(s.count(' ') + 1 for s in sentences)
