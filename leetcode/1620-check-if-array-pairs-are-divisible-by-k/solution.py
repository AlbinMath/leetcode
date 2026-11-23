class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        cnt = [0] * k
        for x in arr:
            cnt[x % k] += 1
        if cnt[0] % 2:
            return False
        for r in range(1, k // 2 + 1):
            if r == k - r:
                if cnt[r] % 2:
                    return False
            elif cnt[r] != cnt[k - r]:
                return False
        return True
