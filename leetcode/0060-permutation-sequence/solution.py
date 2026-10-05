import math

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        result = []

        k -= 1

        for i in range(n, 0, -1):
            factorial = math.factorial(i - 1)

            index = k // factorial

            result.append(str(numbers[index]))
            numbers.pop(index)

            k %= factorial

        return ''.join(result)
