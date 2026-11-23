class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        ca = [0] * 26
        cb = [0] * 26
        for ch in a:
            ca[ord(ch) - 97] += 1
        for ch in b:
            cb[ord(ch) - 97] += 1

        # condition 3
        best = min(m + n - ca[i] - cb[i] for i in range(26))

        # conditions 1 and 2: boundary c in 1..25
        pa = pb = 0  # counts of letters < c
        for c in range(1, 26):
            pa += ca[c - 1]
            pb += cb[c - 1]
            # a < c <= b
            best = min(best, (m - pa) + pb)
            # b < c <= a
            best = min(best, (n - pb) + pa)

        return best
