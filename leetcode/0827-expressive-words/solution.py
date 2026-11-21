from itertools import groupby

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groups(string: str):
            return [(ch, len(list(g))) for ch, g in groupby(string)]

        target = groups(s)

        def stretchy(word: str) -> bool:
            g = groups(word)
            if len(g) != len(target):
                return False
            for (c1, sc), (c2, wc) in zip(target, g):
                if c1 != c2:
                    return False
                if sc < wc:
                    return False
                if sc > wc and sc < 3:
                    return False
            return True

        return sum(stretchy(w) for w in words)
