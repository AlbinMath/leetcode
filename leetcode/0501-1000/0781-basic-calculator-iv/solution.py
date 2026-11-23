from typing import List
from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        env = dict(zip(evalvars, evalints))

        def add(p, q, sign=1):
            r = defaultdict(int, p)
            for k, v in q.items():
                r[k] += sign * v
            return {k: v for k, v in r.items() if v != 0}

        def mul(p, q):
            r = defaultdict(int)
            for k1, v1 in p.items():
                for k2, v2 in q.items():
                    r[tuple(sorted(k1 + k2))] += v1 * v2
            return {k: v for k, v in r.items() if v != 0}

        def make(tok):
            if tok.isdigit():
                v = int(tok)
                return {(): v} if v else {}
            if tok in env:
                v = env[tok]
                return {(): v} if v else {}
            return {(tok,): 1}

        # tokenize
        tokens = []
        i, n = 0, len(expression)
        while i < n:
            c = expression[i]
            if c == ' ':
                i += 1
            elif c in '+-*()':
                tokens.append(c)
                i += 1
            else:
                j = i
                while j < n and expression[j].isalnum():
                    j += 1
                tokens.append(expression[i:j])
                i = j

        prec = {'+': 1, '-': 1, '*': 2}
        vals, ops = [], []

        def apply():
            op = ops.pop()
            b = vals.pop()
            a = vals.pop()
            if op == '+':
                vals.append(add(a, b))
            elif op == '-':
                vals.append(add(a, b, -1))
            else:
                vals.append(mul(a, b))

        for tok in tokens:
            if tok == '(':
                ops.append(tok)
            elif tok == ')':
                while ops[-1] != '(':
                    apply()
                ops.pop()
            elif tok in prec:
                while ops and ops[-1] != '(' and prec[ops[-1]] >= prec[tok]:
                    apply()
                ops.append(tok)
            else:
                vals.append(make(tok))
        while ops:
            apply()

        poly = vals[0]
        keys = sorted(poly, key=lambda k: (-len(k), k))
        res = []
        for k in keys:
            c = poly[k]
            res.append('*'.join([str(c)] + list(k)))
        return res
