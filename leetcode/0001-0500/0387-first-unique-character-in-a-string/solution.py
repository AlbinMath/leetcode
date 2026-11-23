class Solution:
    def firstUniqChar(self, s):
        count = [0] * 26

        # Count each character
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Find the first character that appears once
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i

        return -1
