from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size
        used = [False] * (n + 1)

        def dfs(pos: int) -> bool:
            while pos < size and res[pos]:
                pos += 1
            if pos == size:
                return True
            for v in range(n, 0, -1):
                if used[v]:
                    continue
                if v == 1:
                    res[pos] = 1
                    used[1] = True
                    if dfs(pos + 1):
                        return True
                    res[pos] = 0
                    used[1] = False
                else:
                    j = pos + v
                    if j < size and res[j] == 0:
                        res[pos] = res[j] = v
                        used[v] = True
                        if dfs(pos + 1):
                            return True
                        res[pos] = res[j] = 0
                        used[v] = False
            return False

        dfs(0)
        return res
