from typing import List

class Solution:
    def generateValidStrings(self, n: int, k: int) -> List[str]:
        res = []
        path = []

        def dfs(i: int, cost: int, prev_one: bool) -> None:
            if i == n:
                res.append("".join(path))
                return
            path.append("0")
            dfs(i + 1, cost, False)
            path.pop()
            if not prev_one and cost + i <= k:
                path.append("1")
                dfs(i + 1, cost + i, True)
                path.pop()

        dfs(0, 0, False)
        return res
