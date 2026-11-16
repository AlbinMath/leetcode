class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(pos: int, prev: int) -> bool:
            if pos == n:
                return True
            val = 0
            for j in range(pos, n):
                val = val * 10 + int(s[j])
                if val > prev - 1:
                    break  # pieces only grow as they extend
                if val == prev - 1 and dfs(j + 1, val):
                    return True
            return False

        first = 0
        for i in range(n - 1):  # leave at least one character for a second piece
            first = first * 10 + int(s[i])
            if dfs(i + 1, first):
                return True
        return False
