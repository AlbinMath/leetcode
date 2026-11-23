from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        p = k - 1
        shift = 0
        for i, op in enumerate(operations):
            if (p >> i) & 1:
                shift += op
        return chr(ord('a') + shift % 26)
