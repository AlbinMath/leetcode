from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def dfs(i, expr, cur, last):
            if i == n:
                if cur == target:
                    res.append(expr)
                return
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                s = num[i:j + 1]
                v = int(s)
                if i == 0:
                    dfs(j + 1, s, v, v)
                else:
                    dfs(j + 1, expr + '+' + s, cur + v, v)
                    dfs(j + 1, expr + '-' + s, cur - v, -v)
                    dfs(j + 1, expr + '*' + s, cur - last + last * v, last * v)

        dfs(0, "", 0, 0)
        return res
