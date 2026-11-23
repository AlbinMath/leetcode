
class Solution:
    def totalBeauty(self, nums):
        MOD = 10**9 + 7
        M = max(nums)

        # Precompute all divisors for every number.
        divisors = [[] for _ in range(M + 1)]
        for g in range(1, M + 1):
            for x in range(g, M + 1, g):
                divisors[x].append(g)

        # Fenwick tree for each divisor g.
        # Tree g stores subsequences whose elements
        # are all divisible by g.
        trees = [None] * (M + 1)
        for g in range(1, M + 1):
            trees[g] = [0] * (M // g + 1)

        def update(tree, i, value):
            while i < len(tree):
                tree[i] = (tree[i] + value) % MOD
                i += i & -i

        def query(tree, i):
            result = 0
            while i > 0:
                result = (result + tree[i]) % MOD
                i -= i & -i
            return result

        # Count strictly increasing subsequences
        # whose elements are all divisible by g.
        for x in nums:
            for g in divisors[x]:
                tree = trees[g]
                pos = x // g

                # Start a new subsequence with x,
                # or extend a subsequence ending at a smaller value.
                ways = (1 + query(tree, pos - 1)) % MOD
                update(tree, pos, ways)

        # divisible_count[g] counts subsequences whose
        # GCD is a multiple of g.
        divisible_count = [0] * (M + 1)
        for g in range(1, M + 1):
            divisible_count[g] = query(
                trees[g], M // g
            )

        # Recover the number of subsequences with GCD exactly g.
        exact = [0] * (M + 1)
        ans = 0

        for g in range(M, 0, -1):
            count = divisible_count[g]

            for multiple in range(2 * g, M + 1, g):
                count -= exact[multiple]
                count %= MOD

            exact[g] = count
            ans = (ans + g * count) % MOD

        return ans

