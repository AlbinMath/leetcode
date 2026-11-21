class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = [''] * n
        for i in range(n - 1, -1, -1):
            val = min(26, k - i)  # leave at least 1 for each of the i earlier chars
            res[i] = chr(96 + val)
            k -= val
        return ''.join(res)
