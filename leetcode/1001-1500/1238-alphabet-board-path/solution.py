class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        r = c = 0

        for ch in target:
            idx = ord(ch) - ord('a')
            nr, nc = divmod(idx, 5)

            if nr < r:
                res.append('U' * (r - nr))
            if nc < c:
                res.append('L' * (c - nc))
            if nr > r:
                res.append('D' * (nr - r))
            if nc > c:
                res.append('R' * (nc - c))

            res.append('!')
            r, c = nr, nc

        return ''.join(res)
