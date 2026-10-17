from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        seen = {"0000"}

        while q:
            s, steps = q.popleft()
            if s == target:
                return steps

            for i in range(4):
                for d in (-1, 1):
                    c = str((int(s[i]) + d) % 10)
                    nxt = s[:i] + c + s[i + 1:]
                    if nxt not in dead and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))

        return -1
