class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        ans = ""
        for w in sorted(words):
            if all(w[:i] in s for i in range(1, len(w))):
                if len(w) > len(ans):
                    ans = w
        return ans
