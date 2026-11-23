from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        letters = sorted((c for c in cnt if cnt[c] >= k), reverse=True)

        def ok(seq: str) -> bool:
            # is seq * k a subsequence of s?
            i, rep, m = 0, 0, len(seq)
            for ch in s:
                if ch == seq[i]:
                    i += 1
                    if i == m:
                        i = 0
                        rep += 1
                        if rep == k:
                            return True
            return False

        best = ""
        q = deque([""])
        while q:
            cur = q.popleft()
            for c in letters:
                nxt = cur + c
                if ok(nxt):
                    if len(nxt) > len(best) or (len(nxt) == len(best) and nxt > best):
                        best = nxt
                    q.append(nxt)
        return best
