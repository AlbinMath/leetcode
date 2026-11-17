import numpy as np

class Solution(object):
    def maximizeXorAndXor(self, nums):
        n = len(nums)
        size = 1 << n
        BITS = max(nums).bit_length()
        ALL = (1 << BITS) - 1

        # XOR and AND of every subset, built by doubling
        xr = np.zeros(size, dtype=np.int32)
        an = np.full(size, ALL, dtype=np.int32)
        for i, v in enumerate(nums):
            xr[1 << i: 2 << i] = xr[:1 << i] ^ v
            an[1 << i: 2 << i] = an[:1 << i] & v
        an[0] = 0  # AND of an empty subset is 0

        idx = np.arange(size, dtype=np.int32)
        total_xor = xr[size - 1]
        X = total_xor ^ xr                 # XOR of the complement (rest) for each B
        notX = (~X) & ALL

        basis = [np.zeros(size, dtype=np.int32) for _ in range(BITS)]

        for i, v in enumerate(nums):
            in_rest = ((idx >> i) & 1) == 0
            cur = np.where(in_rest, notX & v, 0).astype(np.int32)
            for b in range(BITS - 1, -1, -1):
                has = ((cur >> b) & 1).astype(bool)
                nb = np.where(has & (basis[b] == 0), cur, basis[b])
                basis[b] = nb
                cur = np.where(has, cur ^ nb, cur)

        res = np.zeros(size, dtype=np.int32)
        for b in range(BITS - 1, -1, -1):
            res = np.maximum(res, res ^ basis[b])

        total = an.astype(np.int64) + X.astype(np.int64) + 2 * res.astype(np.int64)
        return int(total.max())
