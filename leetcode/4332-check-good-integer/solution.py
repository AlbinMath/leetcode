class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = square_sum = 0
        while n:
            d = n % 10
            digit_sum += d
            square_sum += d * d
            n //= 10
        return square_sum - digit_sum >= 50
