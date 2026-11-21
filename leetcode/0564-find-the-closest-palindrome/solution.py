class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        num = int(n)

        # candidates where the digit count changes
        candidates = {10 ** (L - 1) - 1, 10 ** L + 1}

        prefix = int(n[:(L + 1) // 2])
        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)
            if L % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]  # skip the middle digit when mirroring
            candidates.add(int(pal))

        candidates.discard(num)  # must not return n itself
        return str(min(candidates, key=lambda x: (abs(x - num), x)))
