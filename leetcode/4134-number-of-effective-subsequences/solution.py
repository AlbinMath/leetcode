
from typing import List

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total_or = 0
        for x in nums:
            total_or |= x

        bits = [b for b in range(20) if total_or & (1 << b)]
        d = len(bits)
        size = 1 << d
        full = size - 1

        # Compress each number into the relevant bit positions.
        freq = [0] * size

        for x in nums:
            mask = 0
            for i, b in enumerate(bits):
                if x & (1 << b):
                    mask |= 1 << i
            freq[mask] += 1

        # SOS DP: count elements whose masks are subsets of each mask.
        for i in range(d):
            bit = 1 << i
            for mask in range(size):
                if mask & bit:
                    freq[mask] += freq[mask ^ bit]

        # Powers of 2 modulo MOD.
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        # Count subsequences whose removal preserves the original OR.
        ineffective = 0

        for mask in range(size):
            ways = pow2[freq[mask]]

            if (d - mask.bit_count()) % 2 == 0:
                ineffective += ways
            else:
                ineffective -= ways

            ineffective %= MOD

        # All subsequences minus ineffective subsequences.
        return (pow2[n] - ineffective) % MOD

