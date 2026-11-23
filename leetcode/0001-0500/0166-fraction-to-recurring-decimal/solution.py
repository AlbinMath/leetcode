class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) != (denominator < 0):
            res.append('-')

        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        rem = num % den
        if rem == 0:
            return ''.join(res)

        res.append('.')
        seen = {}  # remainder -> index in res where its digit goes

        while rem:
            if rem in seen:
                res.insert(seen[rem], '(')
                res.append(')')
                break
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den

        return ''.join(res)
