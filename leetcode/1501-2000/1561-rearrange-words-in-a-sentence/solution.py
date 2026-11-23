class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        words.sort(key=len)
        res = ' '.join(words)
        return res[0].upper() + res[1:]
