class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        length = [0] * (n + 2)
        cnt = [0] * (n + 2)
        ans = -1

        for i, p in enumerate(arr, 1):
            left, right = length[p - 1], length[p + 1]
            total = left + right + 1

            cnt[left] -= 1
            cnt[right] -= 1
            cnt[total] += 1

            length[p - left] = total
            length[p + right] = total

            if cnt[m] > 0:
                ans = i

        return ans
