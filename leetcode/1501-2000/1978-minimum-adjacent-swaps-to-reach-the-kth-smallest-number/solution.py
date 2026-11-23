class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        target = list(num)

        def next_perm(a):
            i = len(a) - 2
            while i >= 0 and a[i] >= a[i + 1]:
                i -= 1
            j = len(a) - 1
            while a[j] <= a[i]:
                j -= 1
            a[i], a[j] = a[j], a[i]
            a[i + 1:] = reversed(a[i + 1:])

        for _ in range(k):
            next_perm(target)

        cur = list(num)
        n = len(cur)
        swaps = 0

        for i in range(n):
            if cur[i] == target[i]:
                continue
            j = i + 1
            while cur[j] != target[i]:
                j += 1
            # bubble cur[j] left to position i
            while j > i:
                cur[j], cur[j - 1] = cur[j - 1], cur[j]
                j -= 1
                swaps += 1

        return swaps
