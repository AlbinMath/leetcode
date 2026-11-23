class Solution:
    def evaluate(self, expression: str) -> int:
        s = expression
        n = len(s)
        scopes = []

        def read_token(i):
            j = i
            while j < n and s[j] != ' ' and s[j] != ')':
                j += 1
            return s[i:j], j

        def lookup(name):
            for sc in reversed(scopes):
                if name in sc:
                    return sc[name]

        def parse(i):
            # returns (value, next index)
            if s[i] != '(':
                tok, j = read_token(i)
                if tok[0].isdigit() or tok[0] == '-':
                    return int(tok), j
                return lookup(tok), j

            i += 1  # skip '('
            op, i = read_token(i)
            i += 1  # skip space after keyword

            if op == 'add' or op == 'mult':
                a, i = parse(i)
                i += 1  # skip space
                b, i = parse(i)
                i += 1  # skip ')'
                return (a + b if op == 'add' else a * b), i

            # let
            scopes.append({})
            while True:
                if s[i] == '(':
                    val, i = parse(i)
                    break
                tok, j = read_token(i)
                if s[j] == ')':
                    # last token is the result expression
                    val, i = parse(i)
                    break
                # tok is a variable name
                i = j + 1
                v, i = parse(i)
                scopes[-1][tok] = v
                i += 1  # skip space
            scopes.pop()
            i += 1  # skip ')'
            return val, i

        return parse(0)[0]
