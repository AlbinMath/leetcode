class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        d = list(str(n))
        mark = len(d)  # first index to be filled with '9'
        for i in range(len(d) - 1, 0, -1):
            if d[i - 1] > d[i]:
                d[i - 1] = str(int(d[i - 1]) - 1)
                mark = i
        for i in range(mark, len(d)):
            d[i] = '9'
        return int(''.join(d))
