from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        if n - 1 < k:
            return [0] * n

        # trie with counts
        nxt = [{}]
        cnt = [0]
        for w in words:
            node = 0
            for ch in w:
                c = nxt[node].get(ch)
                if c is None:
                    nxt.append({})
                    cnt.append(0)
                    c = len(nxt) - 1
                    nxt[node][ch] = c
                node = c
                cnt[node] += 1

        maxlen = max(len(w) for w in words)
        good = [0] * (maxlen + 2)      # good[d] = nodes at depth d with cnt >= k

        # compute depth of each node via BFS over the trie
        depth = [0] * len(nxt)
        stack = [0]
        while stack:
            u = stack.pop()
            for v in nxt[u].values():
                depth[v] = depth[u] + 1
                stack.append(v)
                if cnt[v] >= k:
                    good[depth[v]] += 1

        ans = [0] * n
        for i, w in enumerate(words):
            # path nodes by depth
            path = []
            node = 0
            for ch in w:
                node = nxt[node][ch]
                path.append(node)
            L = len(path)

            best = 0
            # depths beyond this word's length: only other words' nodes exist there
            for d in range(maxlen, L, -1):
                if good[d] > 0:
                    best = d
                    break
            if best == 0:
                for d in range(L, 0, -1):
                    v = path[d - 1]
                    others = good[d] - (1 if cnt[v] >= k else 0)
                    if others > 0 or cnt[v] >= k + 1:
                        best = d
                        break
            ans[i] = best
        return ans
