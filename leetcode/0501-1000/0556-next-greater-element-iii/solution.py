class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2

        # 1. find pivot
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1

        # 2. find rightmost digit greater than pivot
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # 3. swap
        digits[i], digits[j] = digits[j], digits[i]

        # 4. reverse suffix
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(digits))
        return result if result <= 2**31 - 1 else -1
