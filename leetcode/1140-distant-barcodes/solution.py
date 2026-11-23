from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        cnt = Counter(barcodes)
        ordered = []
        for v, c in cnt.most_common():
            ordered.extend([v] * c)

        n = len(barcodes)
        res = [0] * n
        res[0::2] = ordered[:(n + 1) // 2]
        res[1::2] = ordered[(n + 1) // 2:]
        return res
