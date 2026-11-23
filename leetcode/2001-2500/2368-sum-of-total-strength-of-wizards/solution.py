from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        P = [0] * (n + 1)
        for i, x in enumerate(strength):
            P[i + 1] = P[i] + x
        PP = [0] * (n + 2)
        for k in range(n + 1):
            PP[k + 1] = PP[k] + P[k]

        total = 0
        stack = []
        for j in range(n + 1):
            cur = strength[j] if j < n else 0   # sentinel flushes the stack
            while stack and strength[stack[-1]] >= cur:
                i = stack.pop()
                L = stack[-1] if stack else -1
                R = j
                right = PP[R + 1] - PP[i + 1]
                left = PP[i + 1] - PP[L + 1]
                total += strength[i] * ((i - L) * right - (R - i) * left)
            stack.append(j)

        return total % MOD
        
