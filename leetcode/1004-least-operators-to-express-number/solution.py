class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = 0
        while target:
            target, d = divmod(target, x)
            if k == 0:
                pos, neg = d * 2, (x - d) * 2
            else:
                pos, neg = (
                    min(d * k + pos, (d + 1) * k + neg),
                    min((x - d) * k + pos, (x - d - 1) * k + neg),
                )
            k += 1
        return min(pos, k + neg) - 1
