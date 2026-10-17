
from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        R, C = len(grid), len(grid[0])
        pos = [(r, c) for r in range(R) for c in range(C)
               if grid[r][c] != '#']
        ids = {p: i for i, p in enumerate(pos)}
        n = len(pos)
        m = next(ids[(r,c)] for r in range(R) for c in range(C) if grid[r][c]=='M')
        c = next(ids[(r,c)] for r in range(R) for c in range(C) if grid[r][c]=='C')
        f = next(ids[(r,c)] for r in range(R) for c in range(C) if grid[r][c]=='F')

        def moves(p, jump):
            r, col = pos[p]
            out = [p]
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                for k in range(1, jump+1):
                    x, y = r+dr*k, col+dc*k
                    if not (0 <= x < R and 0 <= y < C) or grid[x][y]=='#':
                        break
                    out.append(ids[(x,y)])
            return out

        M = [moves(i, mouseJump) for i in range(n)]
        K = [moves(i, catJump) for i in range(n)]
        revM = [[] for _ in range(n)]
        revK = [[] for _ in range(n)]
        for i in range(n):
            for j in M[i]: revM[j].append(i)
            for j in K[i]: revK[j].append(i)

        # 0 unknown, 1 mouse wins, 2 cat wins
        color = [[[0]*2 for _ in range(n)] for _ in range(n)]
        deg = [[[len(M[i]), len(K[j])] for j in range(n)] for i in range(n)]
        q = deque()

        for i in range(n):
            for t in range(2):
                color[f][i][t] = 1
                q.append((f, i, t, 1))
                color[i][f][t] = 2
                q.append((i, f, t, 2))
            for t in range(2):
                color[i][i][t] = 2
                q.append((i, i, t, 2))

        while q:
            a, b, t, res = q.popleft()
            if t == 0:
                parents = ((a, x, 1) for x in revK[b] if x != f)
            else:
                parents = ((x, b, 0) for x in revM[a])

            for x, y, pt in parents:
                if color[x][y][pt]:
                    continue
                if (pt == 0 and res == 1) or (pt == 1 and res == 2):
                    color[x][y][pt] = res
                    q.append((x, y, pt, res))
                else:
                    deg[x][y][pt] -= 1
                    if deg[x][y][pt] == 0:
                        winner = 2 if pt == 0 else 1
                        color[x][y][pt] = winner
                        q.append((x, y, pt, winner))

        # Any unresolved state is a draw; the mouse cannot force a win.
        return color[m][c][0] == 1

