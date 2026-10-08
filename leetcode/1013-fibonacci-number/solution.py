class Solution:
    def fib(self, n):
        prev = 0
        curr = 1

        for i in range(n):
            prev, curr = curr, prev + curr

        return prev
