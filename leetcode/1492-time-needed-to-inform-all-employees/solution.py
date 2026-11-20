from collections import deque, defaultdict
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for emp, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(emp)

        ans = 0
        q = deque([(headID, 0)])  # (employee, time they learn the news)
        while q:
            emp, t = q.popleft()
            ans = max(ans, t)
            for sub in children[emp]:
                q.append((sub, t + informTime[emp]))
        return ans
