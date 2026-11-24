class Solution(object):
    def placeWordInCrossword(self, board, word):
        n = len(word)
        rev = word[::-1]

        def can_fit(line):
            for slot in "".join(line).split("#"):
                if len(slot) == n:
                    if all(c == " " or c == w for c, w in zip(slot, word)):
                        return True
                    if all(c == " " or c == w for c, w in zip(slot, rev)):
                        return True
            return False

        for row in board:
            if can_fit(row):
                return True

        for col in zip(*board):
            if can_fit(col):
                return True

        return False
