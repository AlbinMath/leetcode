class Solution:
    def minimumBoxes(self, n: int) -> int:
        k = 0
        used = 0
        # largest full pyramid
        while used + (k + 1) * (k + 2) // 2 <= n:
            k += 1
            used += k * (k + 1) // 2

        floor = k * (k + 1) // 2
        rem = n - used

        j = 0
        while j * (j + 1) // 2 < rem:
            j += 1

        return floor + j
