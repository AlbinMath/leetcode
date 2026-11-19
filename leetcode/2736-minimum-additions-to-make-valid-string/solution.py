class Solution:
    def addMinimum(self, word: str) -> int:
        k = 1 + sum(word[i] <= word[i - 1] for i in range(1, len(word)))
        return 3 * k - len(word)
