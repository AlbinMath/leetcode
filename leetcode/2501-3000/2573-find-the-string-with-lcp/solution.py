from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        curr_char_code = ord('a')

        # Step 1: Greedy character assignment
        for i in range(n):
            if not word[i]:
                if curr_char_code > ord('z'):
                    return ""  # Exceeded 26 lowercase English letters
                assigned_char = chr(curr_char_code)
                curr_char_code += 1
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = assigned_char

        # Step 2: Validate the generated string against the LCP matrix
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)

                if lcp[i][j] != expected:
                    return ""

        return "".join(word)
