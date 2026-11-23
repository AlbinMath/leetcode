class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                   "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                   "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
                "Eighty", "Ninety"]
        scales = ["", "Thousand", "Million", "Billion"]

        def three(n):
            parts = []
            if n >= 100:
                parts.append(below20[n // 100])
                parts.append("Hundred")
                n %= 100
            if n >= 20:
                parts.append(tens[n // 10])
                n %= 10
            if n > 0:
                parts.append(below20[n])
            return parts

        words = []
        i = 0
        while num > 0:
            chunk = num % 1000
            if chunk:
                words = three(chunk) + ([scales[i]] if scales[i] else []) + words
            num //= 1000
            i += 1
        return " ".join(words)
