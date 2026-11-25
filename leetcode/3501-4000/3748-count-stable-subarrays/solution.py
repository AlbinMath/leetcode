from typing import List

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        run_id = [0] * n
        starts, ends = [0], []
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                ends.append(i - 1)
                starts.append(i)
            run_id[i] = len(starts) - 1
        ends.append(n - 1)

        k = len(starts)
        pre = [0] * (k + 1)
        for j in range(k):
            L = ends[j] - starts[j] + 1
            pre[j + 1] = pre[j] + L * (L + 1) // 2

        ans = []
        for l, r in queries:
            a, b = run_id[l], run_id[r]
            if a == b:
                L = r - l + 1
                ans.append(L * (L + 1) // 2)
            else:
                l1 = ends[a] - l + 1
                l2 = r - starts[b] + 1
                ans.append(l1 * (l1 + 1) // 2 + pre[b] - pre[a + 1] + l2 * (l2 + 1) // 2)
        return ans
