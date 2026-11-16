class Solution(object):
    def removeDigit(self, number, digit):
        last_idx = -1
        for i, ch in enumerate(number):
            if ch == digit:
                last_idx = i
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i + 1:]
        return number[:last_idx] + number[last_idx + 1:]
