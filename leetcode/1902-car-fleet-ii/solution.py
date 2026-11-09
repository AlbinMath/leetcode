from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            p, s = cars[i]
            while stack:
                j = stack[-1]
                pj, sj = cars[j]
                if s <= sj:
                    stack.pop()
                    continue
                t = (pj - p) / (s - sj)
                if ans[j] != -1 and t > ans[j]:
                    stack.pop()
                    continue
                ans[i] = t
                break
            stack.append(i)

        return ans
