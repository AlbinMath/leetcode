from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def value(x: str) -> Fraction:
            if '.' not in x:
                return Fraction(int(x))

            integer, frac = x.split('.')
            result = Fraction(int(integer))

            if '(' in frac:
                non_rep, rep = frac.split('(')
                rep = rep[:-1]                       # drop ')'
            else:
                non_rep, rep = frac, ''

            if non_rep:
                result += Fraction(int(non_rep), 10 ** len(non_rep))
            if rep:
                result += Fraction(int(rep),
                                   10 ** len(non_rep) * (10 ** len(rep) - 1))
            return result

        return value(s) == value(t)
