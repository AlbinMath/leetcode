from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        cand = primes[:]  # cand[j] = ugly[idx[j]] * primes[j]
        for i in range(1, n):
            nxt = min(cand)
            ugly[i] = nxt
            for j in range(k):
                if cand[j] == nxt:
                    idx[j] += 1
                    cand[j] = ugly[idx[j]] * primes[j]
        return ugly[-1]
