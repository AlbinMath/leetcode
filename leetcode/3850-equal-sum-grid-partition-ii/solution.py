from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g: List[List[int]]) -> bool:
            m, n = len(g), len(g[0])
            total = sum(map(sum, g))
            top = Counter()
            bot = Counter()
            for row in g:
                bot.update(row)

            acc = 0
            for i in range(m - 1):
                acc += sum(g[i])
                top.update(g[i])
                bot.subtract(g[i])

                A, B = acc, total - acc
                if A == B:
                    return True

                if A > B:
                    diff = A - B
                    rows = i + 1
                    # top section: rows 0..i
                    if rows >= 2 and n >= 2:
                        if top[diff] > 0:
                            return True
                    elif rows == 1:
                        # single row of length n
                        if n >= 2 and (g[0][0] == diff or g[0][n - 1] == diff):
                            return True
                    else:
                        # rows >= 2, n == 1: vertical strip, only ends removable
                        if g[0][0] == diff or g[i][0] == diff:
                            return True
                else:
                    diff = B - A
                    rows = m - i - 1
                    # bottom section: rows i+1..m-1
                    if rows >= 2 and n >= 2:
                        if bot[diff] > 0:
                            return True
                    elif rows == 1:
                        if n >= 2 and (g[m - 1][0] == diff or g[m - 1][n - 1] == diff):
                            return True
                    else:
                        # rows >= 2, n == 1
                        if g[i + 1][0] == diff or g[m - 1][0] == diff:
                            return True
            return False

        if check(grid):
            return True
        transposed = [list(col) for col in zip(*grid)]
        return check(transposed)
