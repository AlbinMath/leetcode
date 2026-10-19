from typing import List

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = [{}]
        for w in words:
            node = 0
            for ch in w:
                nxt = trie[node].get(ch)
                if nxt is None:
                    trie.append({})
                    nxt = len(trie) - 1
                    trie[node][ch] = nxt
                node = nxt

        m = len(target)
        INF = float('inf')
        dp = [INF] * (m + 1)
        dp[0] = 0
        for i in range(m):
            if dp[i] == INF:
                continue
            node = 0
            for j in range(i, m):
                node = trie[node].get(target[j])
                if node is None:
                    break
                if dp[i] + 1 < dp[j + 1]:
                    dp[j + 1] = dp[i] + 1
        return dp[m] if dp[m] != INF else -1
