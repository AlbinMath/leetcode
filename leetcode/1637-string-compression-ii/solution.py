from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        def enc(cnt: int) -> int:
            if cnt == 1:
                return 1
            return 1 + len(str(cnt))

        @lru_cache(maxsize=None)
        def dp(i: int, k: int) -> int:
            if n - i <= k:
                return 0  # can delete everything left

            # option 1: delete s[i]
            best = dp(i + 1, k - 1) if k > 0 else float('inf')

            # option 2: keep s[i], build a run, delete differing chars in between
            same = diff = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    same += 1
                else:
                    diff += 1
                    if diff > k:
                        break
                best = min(best, enc(same) + dp(j + 1, k - diff))

            return best

        return dp(0, k)
