class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        blocked = set(map(tuple, blocked))
        limit = len(blocked) * (len(blocked) - 1) // 2

        def bfs(start, end):
            q, seen = [tuple(start)], {tuple(start)}
            while q and len(seen) <= limit:
                x, y = q.pop()
                if [x, y] == end:
                    return True
                for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    p = (nx, ny)
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and p not in blocked and p not in seen:
                        seen.add(p)
                        q.append(p)
            return len(seen) > limit

        return bfs(source, target) and bfs(target, source)
