class Solution:
    def findNthDigit(self, n: int) -> int:
        digits, count, start = 1, 9, 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // digits
        return int(str(num)[(n - 1) % digits])
