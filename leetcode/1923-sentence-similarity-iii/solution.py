class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a, b = sentence1.split(), sentence2.split()
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        i = 0
        while i < n and a[i] == b[i]:
            i += 1

        j = 0
        while j < n - i and a[n - 1 - j] == b[len(b) - 1 - j]:
            j += 1

        return i + j == n
