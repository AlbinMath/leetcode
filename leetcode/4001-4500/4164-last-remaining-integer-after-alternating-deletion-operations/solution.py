class Solution:
    def lastInteger(self, n: int) -> int:
        lengths = []
        m = n
        while m > 1:
            lengths.append(m)
            m = (m + 1) // 2

        j = 1
        for k in range(len(lengths) - 1, -1, -1):
            m = lengths[k]
            m2 = (m + 1) // 2
            if k % 2 == 0:          # left operation
                j = 2 * j - 1
            else:                   # right operation
                j = m - 2 * m2 + 2 * j
        return j
