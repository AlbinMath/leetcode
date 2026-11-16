from typing import List

class Solution:
    def elevatorRequests(self, n: int, start: int, requests: List[List[int]]) -> int:
        m = len(requests)
        arr = [r[0] for r in requests]
        flr = [r[1] for r in requests]
        INF = float('inf')
        full = (1 << m) - 1

        dp = [[INF] * m for _ in range(1 << m)]
        for j in range(m):
            dp[1 << j][j] = max(abs(start - flr[j]), arr[j])

        for mask in range(1, 1 << m):
            row = dp[mask]
            for last in range(m):
                t = row[last]
                if t == INF:
                    continue
                fl = flr[last]
                for j in range(m):
                    if mask >> j & 1:
                        continue
                    nt = t + abs(fl - flr[j])
                    if nt < arr[j]:
                        nt = arr[j]
                    nm = mask | (1 << j)
                    if nt < dp[nm][j]:
                        dp[nm][j] = nt

        return min(dp[full])
