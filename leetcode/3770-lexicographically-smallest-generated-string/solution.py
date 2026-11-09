class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        word = [''] * L

        # Step 1: place all 'T' windows
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    ch = word[i + j]
                    if ch and ch != str2[j]:
                        return ""
                    word[i + j] = str2[j]

        fixed = [bool(c) for c in word]

        # Step 2: fill free cells with 'a'
        for i in range(L):
            if not word[i]:
                word[i] = 'a'

        # Step 3: fix 'F' windows that accidentally equal str2
        for i in range(n):
            if str1[i] != 'F':
                continue
            if ''.join(word[i:i + m]) != str2:
                continue
            for p in range(i + m - 1, i - 1, -1):
                if not fixed[p]:
                    word[p] = 'b'
                    break
            else:
                return ""

        return ''.join(word)
