from typing import List

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        B = 15
        # trie as arrays: children c0, c1 and pass-through counts
        c0, c1, cnt = [0], [0], [0]

        def insert(v):
            node = 0
            for b in range(B - 1, -1, -1):
                if (v >> b) & 1:
                    if not c1[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c1[node] = len(cnt) - 1
                    node = c1[node]
                else:
                    if not c0[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c0[node] = len(cnt) - 1
                    node = c0[node]
                cnt[node] += 1

        def count_less(x, limit):
            # number of inserted y with x ^ y < limit
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                xb = (x >> b) & 1
                lb = (limit >> b) & 1
                if lb:
                    same = c1[node] if xb else c0[node]   # XOR bit 0
                    if same:
                        res += cnt[same]
                    node = c0[node] if xb else c1[node]   # XOR bit 1
                else:
                    node = c1[node] if xb else c0[node]   # XOR bit 0
                if not node:
                    break
            return res

        ans = 0
        for v in nums:
            ans += count_less(v, high + 1) - count_less(v, low)
            insert(v)
        return ans
