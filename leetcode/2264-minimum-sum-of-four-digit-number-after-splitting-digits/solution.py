class Solution:
    def minimumSum(self, num: int) -> int:
        a, b, c, d = sorted(str(num))
        return 10 * (int(a) + int(b)) + int(c) + int(d)
