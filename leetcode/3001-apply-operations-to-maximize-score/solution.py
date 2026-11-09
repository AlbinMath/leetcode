from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        mx = max(nums)

        # distinct prime factor counts via sieve
        omega = [0] * (mx + 1)
        for p in range(2, mx + 1):
            if omega[p] == 0:  # p is prime
                for m in range(p, mx + 1, p):
                    omega[m] += 1

        sc = [omega[x] for x in nums]

        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            # pop strictly smaller scores; remaining top has score >= sc[i]
            while stack and sc[stack[-1]] < sc[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = 1
        for i in sorted(range(n), key=lambda i: -nums[i]):
            cnt = (i - left[i]) * (right[i] - i)
            t = min(cnt, k)
            ans = ans * pow(nums[i], t, MOD) % MOD
            k -= t
            if k == 0:
                break

        return ans
