class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Case 1: Characters match or pattern has '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Case 2: We found '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: Mismatch, but we have seen a '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: Mismatch and no '*'
            else:
                return False

        # Remaining pattern must contain only '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
