from typing import List
from collections import Counter

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        d = [int(c) for c in s[0::2]]
        op = s[1::2]
        m = len(d)
        LIM = 1000

        # correct value
        total = 0
        term = d[0]
        for i in range(m - 1):
            if op[i] == '*':
                term *= d[i + 1]
            else:
                total += term
                term = d[i + 1]
        total += term
        correct = total

        # S[i][j]: values <= LIM obtainable from d[i..j]
        # Z[i][j]: True if the interval can evaluate to 0 even through an
        #          over-limit value (so a product with a zero side gives 0)
        S = [[set() for _ in range(m)] for _ in range(m)]
        for i in range(m):
            S[i][i].add(d[i])
        for length in range(2, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                cur = S[i][j]
                for k in range(i, j):
                    L, R = S[i][k], S[k + 1][j]
                    if op[k] == '+':
                        for a in L:
                            for b in R:
                                v = a + b
                                if v <= LIM:
                                    cur.add(v)
                    else:
                        for a in L:
                            for b in R:
                                v = a * b
                                if v <= LIM:
                                    cur.add(v)
                        # an over-limit side times a zero side gives 0
                        if 0 in L or 0 in R:
                            cur.add(0)

        possible = S[0][m - 1]
        cnt = Counter(answers)
        score = 0
        for v, c in cnt.items():
            if v == correct:
                score += 5 * c
            elif v in possible:
                score += 2 * c
        return score
