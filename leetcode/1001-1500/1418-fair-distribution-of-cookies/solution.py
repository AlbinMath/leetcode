from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)  # big bags first prunes faster
        loads = [0] * k
        best = float('inf')

        def dfs(i: int) -> None:
            nonlocal best
            if i == len(cookies):
                best = min(best, max(loads))
                return
            seen = set()
            for c in range(k):
                if loads[c] in seen:
                    continue  # symmetric to an earlier child
                if loads[c] + cookies[i] >= best:
                    continue  # can't improve
                seen.add(loads[c])
                loads[c] += cookies[i]
                dfs(i + 1)
                loads[c] -= cookies[i]

        dfs(0)
        return best
