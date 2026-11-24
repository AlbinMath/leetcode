class Solution:
    def kthDigit(self, k: int) -> int:
        if k <= 9:
            return k
        k -= 9
        d = 2
        while True:
            nblocks = 9 * 10 ** (d - 2)
            total = nblocks * 10 * d
            if k > total:
                k -= total
                d += 1
            else:
                break
        blk, off = divmod(k - 1, 10 * d)
        b = 10 ** (d - 2) + blk
        pos, ch = divmod(off, d)
        num = 10 * b + pos if b % 2 == 0 else 10 * b + 9 - pos
        return int(str(num)[ch])
