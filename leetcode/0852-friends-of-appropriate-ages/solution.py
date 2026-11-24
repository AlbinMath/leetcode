from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for a in ages:
            cnt[a] += 1

        total = 0
        for a in range(1, 121):
            if cnt[a] == 0:
                continue
            for b in range(a // 2 + 8, a + 1):
                total += cnt[a] * cnt[b]
                if a == b:
                    total -= cnt[a]

        return total
