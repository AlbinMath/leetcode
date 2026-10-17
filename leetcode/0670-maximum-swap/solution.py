class Solution:
    def maximumSwap(self, num: int) -> int:
        a = list(str(num))
        last = {int(x): i for i, x in enumerate(a)}
        for i, x in enumerate(a):
            for d in range(9, int(x), -1):
                if d in last and last[d] > i:
                    a[i], a[last[d]] = a[last[d]], a[i]
                    return int(''.join(a))
        return num
