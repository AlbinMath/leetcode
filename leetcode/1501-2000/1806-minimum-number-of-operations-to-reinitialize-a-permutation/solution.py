class Solution:
    def reinitializePermutation(self, n: int) -> int:
        pos = 1
        steps = 0
        while True:
            pos = 2 * pos if pos < n // 2 else 2 * pos - (n - 1)
            steps += 1
            if pos == 1:
                return steps
