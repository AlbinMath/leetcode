class Solution(object):
    def countPalindromePaths(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        mask = [0] * n
        order = [0]
        for u in order:  # BFS; appending while iterating is fine
            for v in children[u]:
                mask[v] = mask[u] ^ (1 << (ord(s[v]) - 97))
                order.append(v)

        cnt = {}
        ans = 0
        for m in mask:
            ans += cnt.get(m, 0)
            for c in range(26):
                ans += cnt.get(m ^ (1 << c), 0)
            cnt[m] = cnt.get(m, 0) + 1
        return ans
