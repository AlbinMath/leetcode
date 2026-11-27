from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        order = sorted(range(len(plantTime)), key=lambda i: -growTime[i])
        t = 0
        ans = 0
        for i in order:
            t += plantTime[i]
            ans = max(ans, t + growTime[i])
        return ans
