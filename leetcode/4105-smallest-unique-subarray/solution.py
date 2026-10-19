from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [{}]
        link = [-1]
        ln = [0]
        cnt = [0]
        last = 0

        for c in nums:
            cur = len(ln)
            nxt.append({})
            link.append(0)
            ln.append(ln[last] + 1)
            cnt.append(1)
            p = last
            while p != -1 and c not in nxt[p]:
                nxt[p][c] = cur
                p = link[p]
            if p != -1:
                q = nxt[p][c]
                if ln[p] + 1 == ln[q]:
                    link[cur] = q
                else:
                    cl = len(ln)
                    nxt.append(dict(nxt[q]))
                    link.append(link[q])
                    ln.append(ln[p] + 1)
                    cnt.append(0)
                    while p != -1 and nxt[p].get(c) == q:
                        nxt[p][c] = cl
                        p = link[p]
                    link[q] = cl
                    link[cur] = cl
            last = cur

        order = sorted(range(1, len(ln)), key=lambda v: -ln[v])
        for v in order:
            cnt[link[v]] += cnt[v]

        ans = n
        for v in range(1, len(ln)):
            if cnt[v] == 1:
                cand = ln[link[v]] + 1
                if cand < ans:
                    ans = cand
        return ans
