class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        total = sum(nums)
        T = max(0, (total - k + k - 1) // k)   # ceil((total - k) / k)
        return (T * (T + 1) // 2) % MOD
