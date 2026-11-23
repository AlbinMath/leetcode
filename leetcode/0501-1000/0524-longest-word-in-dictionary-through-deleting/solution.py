class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(word: str) -> bool:
            it = iter(s)
            return all(ch in it for ch in word)

        best = ""
        for word in dictionary:
            if len(word) < len(best):
                continue
            if len(word) == len(best) and word >= best:
                continue
            if is_subseq(word):
                best = word
        return best
