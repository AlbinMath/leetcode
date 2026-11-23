from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all_vals = set()
        cur = set()
        for x in arr:
            cur = {v | x for v in cur}
            cur.add(x)
            all_vals |= cur
        return len(all_vals)
