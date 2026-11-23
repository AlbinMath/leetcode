class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        pos = [i for i, ch in enumerate(s) if ch == '1']
        ones = len(pos)

        if ones % 3:
            return 0
        if ones == 0:
            return ((n - 1) * (n - 2) // 2) % MOD

        t = ones // 3
        first = pos[t] - pos[t - 1]
        second = pos[2 * t] - pos[2 * t - 1]
        return (first * second) % MOD
