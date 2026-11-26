class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        MOD = 10**9 + 7
        n, m = len(word1), len(word2)

        cur = [[0] * (m + 1) for _ in range(n + 1)]
        cur[0][0] = 1

        for c in target:
            R = [[0] * (m + 1) for _ in range(n + 1)]
            C = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                for j in range(m + 1):
                    R[i][j] = (cur[i][j] + (R[i - 1][j] if i else 0)) % MOD
                    C[i][j] = (cur[i][j] + (C[i][j - 1] if j else 0)) % MOD

            new = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                for j in range(m + 1):
                    v = 0
                    if i >= 1 and word1[i - 1] == c:
                        v += R[i - 1][j]
                    if j >= 1 and word2[j - 1] == c:
                        v += C[i][j - 1]
                    new[i][j] = v % MOD
            cur = new

        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                res += cur[i][j]
        return res % MOD
