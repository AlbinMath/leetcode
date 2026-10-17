class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(cur):
            first = last = cur
            total = 0
            while first <= n:
                total += min(n, last) - first + 1
                first *= 10
                last = last * 10 + 9
            return total

        cur = 1
        k -= 1
        while k > 0:
            steps = count(cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
