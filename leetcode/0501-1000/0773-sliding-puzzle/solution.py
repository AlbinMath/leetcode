from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = ''.join(map(str, sum(board, [])))
        target = "123450"
        moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        q = deque([(start, 0)])
        seen = {start}

        while q:
            s, steps = q.popleft()
            if s == target:
                return steps
            i = s.index('0')
            for j in moves[i]:
                t = list(s)
                t[i], t[j] = t[j], t[i]
                nxt = ''.join(t)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
        return -1
