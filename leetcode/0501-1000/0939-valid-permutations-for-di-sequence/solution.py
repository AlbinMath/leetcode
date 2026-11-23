class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1]  # one element, rank 0

        for i in range(1, n + 1):
            # prefix[k] = sum(dp[0..k-1])
            prefix = [0]
            for v in dp:
                prefix.append((prefix[-1] + v) % MOD)

            new = [0] * (i + 1)
            for j in range(i + 1):
                if s[i - 1] == 'I':
                    new[j] = prefix[j]                   # old ranks 0..j-1
                else:
                    new[j] = (prefix[i] - prefix[j]) % MOD  # old ranks j..i-1
            dp = new

        return sum(dp) % MOD
