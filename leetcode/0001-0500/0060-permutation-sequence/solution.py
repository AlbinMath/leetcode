from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(map(str, range(1, n + 1)))
        k -= 1
        res = ""
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            res += nums.pop(k // f)
            k %= f
        return res
