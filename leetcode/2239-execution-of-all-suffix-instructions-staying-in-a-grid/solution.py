class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        delta = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        m = len(s)
        ans = []

        for i in range(m):
            r, c = startPos
            count = 0
            for j in range(i, m):
                dr, dc = delta[s[j]]
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    break
                r, c = nr, nc
                count += 1
            ans.append(count)

        return ans
