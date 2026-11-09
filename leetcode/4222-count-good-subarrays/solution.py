from typing import List

class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        B = 30

        # L: previous index with value >= nums[i]; R: next index with value > nums[i]
        L = [-1] * n
        R = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)

        # badL / badR: nearest index holding a bit that nums[i] lacks
        badL = [-1] * n
        last = [-1] * B
        for i in range(n):
            x = nums[i]
            m = -1
            for b in range(B):
                if not (x >> b) & 1 and last[b] > m:
                    m = last[b]
            badL[i] = m
            for b in range(B):
                if (x >> b) & 1:
                    last[b] = i

        badR = [n] * n
        nxt = [n] * B
        for i in range(n - 1, -1, -1):
            x = nums[i]
            m = n
            for b in range(B):
                if not (x >> b) & 1 and nxt[b] < m:
                    m = nxt[b]
            badR[i] = m
            for b in range(B):
                if (x >> b) & 1:
                    nxt[b] = i

        ans = 0
        for i in range(n):
            left = i - max(L[i], badL[i])
            right = min(R[i], badR[i]) - i
            ans += left * right
        return ans
