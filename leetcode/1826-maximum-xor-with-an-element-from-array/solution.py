from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i][1])

        # trie stored as two child arrays
        left = [0]   # child for bit 0 (0 means none; root is node 0)
        right = [0]  # child for bit 1

        def insert(v):
            node = 0
            for b in range(29, -1, -1):
                if (v >> b) & 1:
                    if not right[node]:
                        left.append(0); right.append(0)
                        right[node] = len(left) - 1
                    node = right[node]
                else:
                    if not left[node]:
                        left.append(0); right.append(0)
                        left[node] = len(left) - 1
                    node = left[node]

        ans = [-1] * len(queries)
        p = 0
        n = len(nums)
        for qi in order:
            x, m = queries[qi]
            while p < n and nums[p] <= m:
                insert(nums[p])
                p += 1
            if p == 0:
                continue  # no element <= m
            node = 0
            res = 0
            for b in range(29, -1, -1):
                bit = (x >> b) & 1
                if bit:  # want a 0 child
                    if left[node]:
                        res |= 1 << b
                        node = left[node]
                    else:
                        node = right[node]
                else:    # want a 1 child
                    if right[node]:
                        res |= 1 << b
                        node = right[node]
                    else:
                        node = left[node]
            ans[qi] = res
        return ans
