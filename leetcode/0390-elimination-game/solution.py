class Solution:
    def lastRemaining(self, n: int) -> int:
        head, step, remaining = 1, 1, n
        left_to_right = True

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head
