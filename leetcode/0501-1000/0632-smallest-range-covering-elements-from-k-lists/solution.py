import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        h = [(a[0], i, 0) for i, a in enumerate(nums)]
        heapq.heapify(h)
        right = max(a[0] for a in nums)
        best = [-10**9, 10**9]

        while True:
            left, i, j = heapq.heappop(h)
            if right - left < best[1] - best[0]:
                best = [left, right]
            if j + 1 == len(nums[i]):
                break
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(h, (v, i, j + 1))

        return best
