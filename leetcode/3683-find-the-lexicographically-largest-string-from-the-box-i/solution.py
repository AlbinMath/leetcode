class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        L = n - numFriends + 1
        return max(word[i:i + L] for i in range(n))
