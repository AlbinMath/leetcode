class Solution(object):
    def sumOfNumberAndReverse(self, num):
        return any(x + int(str(x)[::-1]) == num for x in range(num // 2, num + 1))
