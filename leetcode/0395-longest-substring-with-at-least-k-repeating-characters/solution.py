class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        best = 0

        for t in range(1, 27):
            cnt = [0] * 26
            distinct = at_least_k = 0
            left = 0

            for right in range(n):
                r = ord(s[right]) - 97
                if cnt[r] == 0:
                    distinct += 1
                cnt[r] += 1
                if cnt[r] == k:
                    at_least_k += 1

                while distinct > t:
                    l = ord(s[left]) - 97
                    if cnt[l] == k:
                        at_least_k -= 1
                    cnt[l] -= 1
                    if cnt[l] == 0:
                        distinct -= 1
                    left += 1

                if distinct == t and at_least_k == t:
                    best = max(best, right - left + 1)

        return best
