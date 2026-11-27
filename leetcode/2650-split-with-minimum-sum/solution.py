class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        a = ''.join(digits[0::2])
        b = ''.join(digits[1::2])
        return int(a) + int(b or '0')
