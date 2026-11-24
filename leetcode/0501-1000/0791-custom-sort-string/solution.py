from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []

        for ch in order:
            if ch in count:
                res.append(ch * count.pop(ch))

        for ch, freq in count.items():
            res.append(ch * freq)

        return ''.join(res)
