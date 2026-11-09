class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        remaining = s.count(letter)
        need = repetition
        stack = []

        for i, c in enumerate(s):
            # remaining = copies of `letter` in s[i:], including s[i]
            while stack and stack[-1] > c and len(stack) - 1 + (n - i) >= k:
                top = stack[-1]
                if top == letter:
                    if need + 1 > remaining:
                        break
                    need += 1
                stack.pop()

            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    need -= 1
                elif k - len(stack) > max(need, 0):
                    stack.append(c)

            if c == letter:
                remaining -= 1

        return ''.join(stack)
