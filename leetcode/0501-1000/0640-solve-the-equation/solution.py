import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(side: str):
            coef = const = 0
            for term in re.findall(r'[+-]?[^+-]+', side):
                if term[-1] == 'x':
                    num = term[:-1]
                    if num in ('', '+'):
                        coef += 1
                    elif num == '-':
                        coef -= 1
                    else:
                        coef += int(num)
                else:
                    const += int(term)
            return coef, const

        left, right = equation.split('=')
        lc, lk = parse(left)
        rc, rk = parse(right)

        a = lc - rc   # net x coefficient
        b = rk - lk   # net constant, moved to the right side

        if a == 0:
            return "Infinite solutions" if b == 0 else "No solution"
        return f"x={b // a}"
