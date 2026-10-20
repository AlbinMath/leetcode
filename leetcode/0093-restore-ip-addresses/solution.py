
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return

            for j in range(i + 1, min(i + 4, len(s) + 1)):
                part = s[i:j]
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue
                backtrack(j, parts + [part])

        backtrack(0, [])
        return res

