from collections import Counter

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        c = Counter(arr)
        ans = 0
        for x in range(101):
            if c[x] == 0:
                continue
            for y in range(x, 101):
                if c[y] == 0:
                    continue
                z = target - x - y
                if z < y or z > 100 or c[z] == 0:
                    continue
                if x == y == z:
                    ans += c[x] * (c[x] - 1) * (c[x] - 2) // 6
                elif x == y:
                    ans += c[x] * (c[x] - 1) // 2 * c[z]
                elif y == z:
                    ans += c[x] * (c[y] * (c[y] - 1) // 2)
                else:
                    ans += c[x] * c[y] * c[z]
        return ans % MOD
