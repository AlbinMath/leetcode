class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        a, b = 1, 9 if s[0] == '*' else int(s[0] != '0')

        for i in range(1, len(s)):
            c = 9 if s[i] == '*' else int(s[i] != '0')
            if s[i-1] == '*' and s[i] == '*':
                d = 15
            elif s[i-1] == '*':
                d = 2 if s[i] <= '6' else 1
            elif s[i] == '*':
                d = 9 if s[i-1] == '1' else 6 if s[i-1] == '2' else 0
            else:
                d = int(10 <= int(s[i-1:i+1]) <= 26)

            a, b = b, (b*c + a*d) % MOD
        return b
