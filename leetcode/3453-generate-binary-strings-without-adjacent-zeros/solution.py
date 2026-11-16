from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(prev_zero: bool) -> None:
            if len(path) == n:
                res.append("".join(path))
                return
            path.append("1")
            dfs(False)
            path.pop()
            if not prev_zero:
                path.append("0")
                dfs(True)
                path.pop()

        dfs(False)
        return res
