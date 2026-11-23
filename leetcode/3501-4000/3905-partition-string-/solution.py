from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        cur = []
        for ch in s:
            cur.append(ch)
            seg = ''.join(cur)
            if seg not in seen:
                seen.add(seg)
                res.append(seg)
                cur = []
        return res
