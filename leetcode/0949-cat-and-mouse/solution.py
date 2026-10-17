
from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        color = [[[0]*2 for _ in range(n)] for _ in range(n)]
        deg = [[[0]*2 for _ in range(n)] for _ in range(n)]
        q = deque()

        for m in range(n):
            for c in range(1, n):
                deg[m][c][0] = len(graph[m])
                deg[m][c][1] = sum(x != 0 for x in graph[c])

        for c in range(1, n):
            for t in range(2):
                color[0][c][t] = 1
                q.append((0, c, t, 1))
                color[c][c][t] = 2
                q.append((c, c, t, 2))

        while q:
            m, c, t, res = q.popleft()

            if t == 0:  # Previous move was by cat
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if color[m][pc][1]:
                        continue
                    if res == 2:
                        color[m][pc][1] = 2
                        q.append((m, pc, 1, 2))
                    else:
                        deg[m][pc][1] -= 1
                        if deg[m][pc][1] == 0:
                            color[m][pc][1] = 1
                            q.append((m, pc, 1, 1))
            else:  # Previous move was by mouse
                for pm in graph[m]:
                    if color[pm][c][0]:
                        continue
                    if res == 1:
                        color[pm][c][0] = 1
                        q.append((pm, c, 0, 1))
                    else:
                        deg[pm][c][0] -= 1
                        if deg[pm][c][0] == 0:
                            color[pm][c][0] = 2
                            q.append((pm, c, 0, 2))

        return color[1][2][0]

