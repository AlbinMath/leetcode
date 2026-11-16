class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 10        # k = 0 and k = 1: the numbers 0..9
        unique = 9        # count of k-digit numbers with unique digits
        avail = 9         # choices for the next digit
        for _ in range(2, n + 1):
            unique *= avail
            total += unique
            avail -= 1
        return total
