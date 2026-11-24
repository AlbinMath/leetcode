class Solution(object):
    def greatestLetter(self, s):
        seen = set(s)
        for code in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(code)
            if upper in seen and upper.lower() in seen:
                return upper
        return ""
