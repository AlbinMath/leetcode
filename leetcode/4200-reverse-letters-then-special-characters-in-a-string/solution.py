class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        specials = [c for c in s if not c.isalpha()]
        letters.reverse()
        specials.reverse()

        res = []
        li = si = 0
        for c in s:
            if c.isalpha():
                res.append(letters[li])
                li += 1
            else:
                res.append(specials[si])
                si += 1
        return ''.join(res)
