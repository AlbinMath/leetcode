from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque()
        h = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    h[i][j] = 0
                    q.append((i,j))
        for i,j in q:
            pass
        while q:
            i,j = q.popleft()
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0 <= x < m and 0 <= y < n and h[x][y] == -1:
                    h[x][y] = h[i][j] + 1
                    q.append((x,y))
        return h
