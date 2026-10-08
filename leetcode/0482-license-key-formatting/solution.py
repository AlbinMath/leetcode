class Solution:
    def licenseKeyFormatting(self, s, k):
        # Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()

        result = []

        # Start from the right
        i = len(s)

        while i > 0:
            start = max(0, i - k)
            result.append(s[start:i])
            i = start

        # Groups were created from right to left
        result.reverse()

        return "-".join(result)
