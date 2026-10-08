class Solution:
    def countSegments(self, s):
        count = 0

        for i in range(len(s)):
            # Current character is not a space
            # and either it's the first character
            # or the previous character is a space
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1

        return count
