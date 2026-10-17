class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)
        seen = set()
        for x in range(16):
            b = bin(x).count('1')
            if b <= presses and (presses - b) % 2 == 0:
                s = tuple(
                    1 ^ ((x & 1) != 0)
                    ^ (((x >> 1) & 1) != 0 and i % 2 == 0)
                    ^ (((x >> 2) & 1) != 0 and i % 2 == 1)
                    ^ (((x >> 3) & 1) != 0 and i % 3 == 1)
                    for i in range(1, n + 1)
                )
                seen.add(s)
        return len(seen)
