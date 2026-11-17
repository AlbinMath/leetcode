class Solution(object):
    def alternatingXOR(self, nums, target1, target2):
        MOD = 10**9 + 7
        A = {0: 1}  # sums of dp2 (plus the empty prefix) by prefix xor
        B = {}      # sums of dp1 by prefix xor
        P = 0
        dp1 = dp2 = 0
        for x in nums:
            P ^= x
            dp1 = A.get(P ^ target1, 0)
            dp2 = B.get(P ^ target2, 0)
            A[P] = (A.get(P, 0) + dp2) % MOD
            B[P] = (B.get(P, 0) + dp1) % MOD
        return (dp1 + dp2) % MOD
