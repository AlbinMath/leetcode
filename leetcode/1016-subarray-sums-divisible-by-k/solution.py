class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = [0] * k
        cnt[0] = 1
        s = 0
        res = 0
        for v in nums:
            s = (s + v) % k
            res += cnt[s]
            cnt[s] += 1
        return res
