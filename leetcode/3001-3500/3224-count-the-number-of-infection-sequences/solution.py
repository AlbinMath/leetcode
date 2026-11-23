class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10**9 + 7
        m = n - len(sick)

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        ans = fact[m]

        # Uninfected people before the first initially infected person
        ans = ans * inv_fact[sick[0]] % MOD

        # Uninfected people after the last initially infected person
        ans = ans * inv_fact[n - 1 - sick[-1]] % MOD

        # Gaps between initially infected people
        for i in range(1, len(sick)):
            gap = sick[i] - sick[i - 1] - 1
            ans = ans * inv_fact[gap] % MOD

            if gap > 1:
                ans = ans * pow(2, gap - 1, MOD) % MOD

        return ans
