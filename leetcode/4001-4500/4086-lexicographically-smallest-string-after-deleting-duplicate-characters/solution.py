from collections import Counter

class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        total = Counter(s)
        stack = []
        for c in s:
            while stack and stack[-1] > c and total[stack[-1]] > 1:
                total[stack.pop()] -= 1
            stack.append(c)

        while stack and total[stack[-1]] > 1:
            total[stack.pop()] -= 1

        return ''.join(stack)
