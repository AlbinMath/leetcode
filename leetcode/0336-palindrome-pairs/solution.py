from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rev = {w[::-1]: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            n = len(w)
            for j in range(n + 1):
                prefix, suffix = w[:j], w[j:]
                if prefix == prefix[::-1]:
                    k = rev.get(suffix)
                    if k is not None and k != i:
                        res.append([k, i])
                if j != n and suffix == suffix[::-1]:
                    k = rev.get(prefix)
                    if k is not None and k != i:
                        res.append([i, k])
        return res
