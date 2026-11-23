
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [float('inf')] * n

        # Left to right: nearest occurrence of c on the left
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Right to left: nearest occurrence of c on the right
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer

