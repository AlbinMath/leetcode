from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    rest = [nums[k] for k in range(n) if k != i and k != j]
                    cands = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        cands.append(a / b)
                    if abs(a) > EPS:
                        cands.append(b / a)
                    for c in cands:
                        if solve(rest + [c]):
                            return True
            return False

        return solve([float(c) for c in cards])
