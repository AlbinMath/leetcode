from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = [{}]
        cnt = [0]
        ans = 0
        for w in words:
            L = len(w)
            node = 0
            for k in range(L):
                key = (w[k], w[L - 1 - k])
                nxt = trie[node].get(key)
                if nxt is None:
                    trie.append({})
                    cnt.append(0)
                    nxt = len(trie) - 1
                    trie[node][key] = nxt
                node = nxt
                ans += cnt[node]
            cnt[node] += 1
        return ans
