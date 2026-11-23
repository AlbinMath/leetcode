class Solution:
    def judgeSquareSum(self, c):
        a, b = 0, int(c**0.5)
        while a <= b:
            s = a*a + b*b
            if s == c:
                return True
            if s < c:
                a += 1
            else:
                b -= 1
        return False
