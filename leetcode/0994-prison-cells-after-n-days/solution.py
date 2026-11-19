from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        state = 0
        for i, c in enumerate(cells):
            state |= c << i

        def step(x: int) -> int:
            return ~((x << 1) ^ (x >> 1)) & 0b01111110

        seen = {}
        day = 0
        while day < n:
            if state in seen:
                cycle = day - seen[state]
                n = day + (n - day) % cycle
                if day == n:
                    break
                seen.clear()   # avoid re-triggering the cycle shortcut
            seen[state] = day
            state = step(state)
            day += 1

        return [(state >> i) & 1 for i in range(8)]
