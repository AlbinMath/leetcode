class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        p = bytearray(b'\x01') * (right + 1)
        p[0:2] = b'\x00\x00'
        for i in range(2, int(right**0.5) + 1):
            if p[i]:
                p[i*i:right+1:i] = b'\x00' * ((right - i*i) // i + 1)

        primes = [i for i in range(max(2, left), right + 1) if p[i]]
        ans, gap = [-1, -1], float('inf')
        for a, b in zip(primes, primes[1:]):
            if b - a < gap:
                ans, gap = [a, b], b - a
                if gap == 2:
                    break
        return ans
