import numpy as np

class Solution(object):
    def maxProduct(self, nums):
        bits = max(nums).bit_length()
        size = 1 << bits
        full = size - 1

        arr = np.array(nums, dtype=np.int64)
        best = np.zeros(size, dtype=np.int64)
        best[arr] = arr  # best[m] = largest element that is a submask of m

        for b in range(bits):
            v = best.reshape(-1, 2, 1 << b)
            np.maximum(v[:, 1, :], v[:, 0, :], out=v[:, 1, :])

        partner = best[full ^ arr]   # largest element fitting inside the complement
        return int((arr * partner).max())
