from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, t):
            drop = len(nums) - t
            st = []
            for d in nums:
                while drop and st and st[-1] < d:
                    st.pop()
                    drop -= 1
                st.append(d)
            return st[:t]

        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a[0])
                    a = a[1:]
                else:
                    res.append(b[0])
                    b = b[1:]
            return res

        m, n = len(nums1), len(nums2)
        best = []
        for i in range(max(0, k - n), min(k, m) + 1):
            cand = merge(pick(nums1, i), pick(nums2, k - i))
            if cand > best:
                best = cand
        return best
