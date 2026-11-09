class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        n = len(s)
        A, B, C = p.split('*')
        INF = float('inf')

        def z_function(t: str) -> list:
            L = len(t)
            z = [0] * L
            l = r = 0
            for i in range(1, L):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < L and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            return z

        def occurrences(x: str) -> list:
            # occ[i] is True if x occurs in s starting at i, for i in 0..n
            if not x:
                return [True] * (n + 1)
            m = len(x)
            z = z_function(x + '#' + s)
            occ = [False] * (n + 1)
            for i in range(n - m + 1):
                if z[m + 1 + i] >= m:
                    occ[i] = True
            return occ

        occA, occB, occC = occurrences(A), occurrences(B), occurrences(C)
        la, lb, lc = len(A), len(B), len(C)

        # prevA[j]: largest a <= j with occA[a], else -1
        prevA = [-1] * (n + 1)
        for j in range(n + 1):
            prevA[j] = j if occA[j] else (prevA[j - 1] if j else -1)

        # nextC[j]: smallest c >= j with occC[c], else INF
        nextC = [INF] * (n + 2)
        for j in range(n, -1, -1):
            nextC[j] = j if occC[j] else nextC[j + 1]

        ans = INF
        for b in range(n + 1):
            if not occB[b] or b - la < 0 or b + lb > n:
                continue
            a = prevA[b - la]
            if a == -1:
                continue
            c = nextC[b + lb]
            if c == INF:
                continue
            ans = min(ans, c + lc - a)

        return -1 if ans == INF else ans
