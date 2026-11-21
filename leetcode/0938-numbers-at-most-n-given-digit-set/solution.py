class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        L = len(s)
        D = len(digits)

        # shorter numbers
        count = sum(D ** k for k in range(1, L))

        # same length as n
        for i, c in enumerate(s):
            smaller = sum(d < c for d in digits)
            count += smaller * D ** (L - i - 1)
            if c not in digits:
                return count   # can't keep matching n's prefix

        return count + 1       # n itself is buildable
