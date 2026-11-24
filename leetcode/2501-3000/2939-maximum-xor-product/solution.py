class Solution(object):
    def maximumXorProduct(self, a, b, n):
        MOD = 10**9 + 7
        A = (a >> n) << n
        B = (b >> n) << n
        for i in range(n - 1, -1, -1):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            if ai == bi:
                A |= 1 << i
                B |= 1 << i
            elif A <= B:
                A |= 1 << i
            else:
                B |= 1 << i
        return (A * B) % MOD
