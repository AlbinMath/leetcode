from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # sieve of primes up to 1000
        N = 1000
        is_p = [True] * (N + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, int(N ** 0.5) + 1):
            if is_p[i]:
                for j in range(i * i, N + 1, i):
                    is_p[j] = False

        # largest_below[x] = largest prime strictly less than x, or 0 if none
        largest_below = [0] * (N + 2)
        last = 0
        for x in range(N + 2):
            largest_below[x] = last
            if x <= N and is_p[x]:
                last = x

        prev = 0
        for x in nums:
            if x <= prev:
                return False
            p = largest_below[x - prev]  # prime < x - prev, so x - p > prev
            x -= p  # p == 0 means no subtraction
            prev = x
        return True
