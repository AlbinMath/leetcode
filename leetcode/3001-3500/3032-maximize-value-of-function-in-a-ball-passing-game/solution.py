import numpy as np

class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        n = len(receiver)
        LOG = k.bit_length()

        up = np.array(receiver, dtype=np.int64)
        sm = up.copy()                      # sum of the next 2^0 = 1 player
        cur = np.arange(n, dtype=np.int64)  # current position for every start
        score = cur.copy()                  # the starting index counts

        for j in range(LOG):
            if (k >> j) & 1:
                score += sm[cur]
                cur = up[cur]
            # build level j+1
            sm = sm + sm[up]
            up = up[up]

        return int(score.max())
