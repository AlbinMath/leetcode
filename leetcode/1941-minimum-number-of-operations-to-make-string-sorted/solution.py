class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        def mod_pow(a, b):
            res = 1
            while b:
                if b & 1:
                    res = res * a % MOD
                a = a * a % MOD
                b >>= 1
            return res

        inv_fact[n] = mod_pow(fact[n], MOD - 2)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = 0
        remaining = n

        for ch in s:
            x = ord(ch) - ord('a')
            smaller = sum(freq[:x])

            ways = fact[remaining - 1] * smaller % MOD
            for count in freq:
                ways = ways * inv_fact[count] % MOD

            ans = (ans + ways) % MOD

            freq[x] -= 1
            remaining -= 1

        return ans
