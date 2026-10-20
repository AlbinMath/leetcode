from typing import List

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        p = list(range(n))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        ans = []
        for u, v in requests:
            a, b = find(u), find(v)
            if a == b:
                ans.append(True)
                continue

            if any(find(x) == a and find(y) == b or
                   find(x) == b and find(y) == a
                   for x, y in restrictions):
                ans.append(False)
            else:
                p[a] = b
                ans.append(True)

        return ans
