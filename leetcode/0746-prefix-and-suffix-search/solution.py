class WordFilter:

    def __init__(self, words: list[str]):
        self.table = {}
        for idx, w in enumerate(words):
            n = len(w)
            for i in range(1, n + 1):
                pre = w[:i]
                for j in range(n):
                    self.table[pre + '#' + w[j:]] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.table.get(pref + '#' + suff, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
