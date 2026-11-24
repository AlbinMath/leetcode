class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        K = min(n, maxValue.bit_length())      # max distinct values: 2^(K-1) <= maxValue

        # C(n-1, j) for j = 0..K-1, via multiplicative formula with modular inverses
        comb = [1] * K
        for j in range(1, K):
            comb[j] = comb[j - 1] * (n - j) % MOD * pow(j, MOD - 2, MOD) % MOD

        cur = [0] + [1] * maxValue              # chains of length 1
        ans = sum(cur) % MOD * comb[0] % MOD    # k = 1: C(n-1, 0) = 1

        for k in range(2, K + 1):
            nxt = [0] * (maxValue + 1)
            for v in range(1, maxValue + 1):
                c = cur[v]
                if c:
                    for m in range(2 * v, maxValue + 1, v):
                        nxt[m] = (nxt[m] + c) % MOD
            ans = (ans + sum(nxt) % MOD * comb[k - 1]) % MOD
            cur = nxt
        return ans
