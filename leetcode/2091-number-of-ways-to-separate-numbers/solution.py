class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0':
            return 0
            
        MOD = 10**9 + 7
        n = len(num)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = 1 + lcp[i + 1][j + 1]
        def is_less_or_equal(a: int, b: int, l: int) -> bool:
            common = lcp[a][b]
            if common >= l:
                return True
            return num[a + common] < num[b + common]
        pref = [[0] * (n + 1) for _ in range(n)]
        
        for i in range(n):
            for l in range(1, i + 2):
                start = i - l + 1
                ways = 0
                if num[start] != '0':
                    if start == 0:
                        ways = 1
                    else:
                        prev_end = start - 1
                        max_prev_len = min(l - 1, prev_end + 1)
                        ways = pref[prev_end][max_prev_len]
                        prev_start = prev_end - l + 1
                        if prev_start >= 0 and is_less_or_equal(prev_start, start, l):
                            same_len_ways = (pref[prev_end][l] - pref[prev_end][l - 1]) % MOD
                            ways = (ways + same_len_ways) % MOD
                            
                pref[i][l] = (pref[i][l - 1] + ways) % MOD
                
        return pref[n - 1][n]
