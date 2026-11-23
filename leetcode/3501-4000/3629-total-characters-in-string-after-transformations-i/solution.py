class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26
        
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
            
        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[0] + cnt[25]) % MOD
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
            
        return sum(cnt) % MOD
