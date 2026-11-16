from typing import List

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        n = len(nums)
        best = 0
        for i in range(n):
            for v in (nums[i][i], nums[i][n - 1 - i]):
                if v > best and is_prime(v):
                    best = v
        return best
