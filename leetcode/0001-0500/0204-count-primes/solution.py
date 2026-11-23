class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        p = bytearray(b'\x01') * n
        p[0:2] = b'\x00\x00'
        for i in range(2, int(n**0.5) + 1):
            if p[i]:
                p[i*i:n:i] = b'\x00' * (((n - 1 - i*i) // i) + 1)
        return sum(p)
