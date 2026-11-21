class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = list(s)
        total = 0

        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            res[i] = chr((ord(s[i]) - 97 + total) % 26 + 97)

        return ''.join(res)
