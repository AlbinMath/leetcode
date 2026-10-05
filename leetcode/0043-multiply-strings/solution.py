class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        # Multiply every digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                product = a * b

                pos2 = i + j + 1
                pos1 = i + j

                result[pos2] += product

                # Handle carry
                result[pos1] += result[pos2] // 10
                result[pos2] %= 10

        # Remove leading zeros
        start = 0

        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))
