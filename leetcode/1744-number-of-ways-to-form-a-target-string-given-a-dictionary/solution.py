class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)

        # cnt[k][c]: number of words with letter c at column k
        cnt = [[0] * 26 for _ in range(m)]
        for w in words:
            for k, ch in enumerate(w):
                cnt[k][ord(ch) - 97] += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for k in range(m):
            row = cnt[k]
            # iterate i downward so column k is used for at most one target char
            for i in range(min(k, n - 1), -1, -1):
                c = row[ord(target[i]) - 97]
                if c and dp[i]:
                    dp[i + 1] = (dp[i + 1] + dp[i] * c) % MOD

        return dp[n]
