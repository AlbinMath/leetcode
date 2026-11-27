class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] <= k:
            fib.append(fib[-1] + fib[-2])
        count = 0
        for f in reversed(fib):
            if k == 0:
                break
            if f <= k:
                k -= f
                count += 1
        return count
