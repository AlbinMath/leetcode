class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda ch: ord(ch) - 96

        pk = pow(power, k - 1, modulo)       # p^(k-1) mod m

        # hash of the last window s[n-k:], computed directly
        h = 0
        for i in range(n - 1, n - k - 1, -1):
            h = (h * power + val(s[i])) % modulo   # Horner, highest power first

        best = n - k if h == hashValue else -1

        for i in range(n - k - 1, -1, -1):
            h = ((h - val(s[i + k]) * pk) * power + val(s[i])) % modulo
            if h == hashValue:
                best = i                        # smaller index overrides

        return s[best:best + k]
