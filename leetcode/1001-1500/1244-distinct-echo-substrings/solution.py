class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()
        for L in range(1, n // 2 + 1):
            cnt = 0
            for i in range(n - L):
                if text[i] == text[i + L]:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == L:
                    seen.add(text[i - L + 1:i + L + 1])
                    cnt -= 1
        return len(seen)
