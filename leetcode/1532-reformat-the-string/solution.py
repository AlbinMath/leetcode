class Solution:
    def reformat(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        digits = [ch for ch in s if ch.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        result = []

        for i in range(len(first)):
            result.append(first[i])

            if i < len(second):
                result.append(second[i])

        return ''.join(result)
