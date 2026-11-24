from collections import deque
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = [False] * 1001
        visited[start] = True
        q = deque([(start, 0)])
        while q:
            x, d = q.popleft()
            for v in nums:
                for y in (x + v, x - v, x ^ v):
                    if y == goal:
                        return d + 1
                    if 0 <= y <= 1000 and not visited[y]:
                        visited[y] = True
                        q.append((y, d + 1))
        return -1
