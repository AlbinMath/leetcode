class Solution:
    def findSecretWord(self, words, master):
        def match(a, b):
            return sum(x == y for x, y in zip(a, b))

        for _ in range(30):
            guess = min(words, key=lambda w: max(
                [sum(match(w, x) == i for x in words)
                 for i in range(7)]
            ))
            res = master.guess(guess)
            if res == 6:
                return
            words = [w for w in words if match(w, guess) == res]
