from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for qx, qy, r in queries:
            r2 = r * r
            cnt = 0
            for x, y in points:
                dx, dy = x - qx, y - qy
                if dx * dx + dy * dy <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans
