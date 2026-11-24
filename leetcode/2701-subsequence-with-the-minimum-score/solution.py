class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        # suf[j]: largest start index in s matching t[j:] as a subsequence
        # suf[m] = n  (empty suffix)
        suf = [-1] * (m + 1)
        suf[m] = n
        k = n - 1
        for j in range(m - 1, -1, -1):
            while k >= 0 and s[k] != t[j]:
                k -= 1
            if k < 0:
                break               # suf[j..0] stay -1
            suf[j] = k
            k -= 1

        ans = m                      # remove everything
        j = 0                        # smallest j with suf[j] > prefix end
        p = -1                       # s-index where t[0:i] ends (-1 if i == 0)

        for i in range(m + 1):       # i = length of kept prefix
            if i > 0:
                # extend prefix by t[i-1]
                p += 1
                while p < n and s[p] != t[i - 1]:
                    p += 1
                if p == n:
                    break            # prefix no longer fits in s

            j = max(j, i)
            while j <= m and suf[j] <= p:
                j += 1
            # suf[m] = n > p always, so j <= m here
            ans = min(ans, j - i)

        return ans
