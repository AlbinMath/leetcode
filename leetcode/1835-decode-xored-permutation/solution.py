from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        total = 0
        for i in range(1, n + 1):
            total ^= i

        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]

        perm = [total ^ odd]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
