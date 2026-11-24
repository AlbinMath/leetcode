class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stack.append(c)
                continue

            has_t = has_f = False
            while stack[-1] != '(':
                if stack.pop() == 't':
                    has_t = True
                else:
                    has_f = True
            stack.pop()        # '('
            op = stack.pop()   # operator

            if op == '!':
                res = has_f
            elif op == '&':
                res = not has_f
            else:  # '|'
                res = has_t
            stack.append('t' if res else 'f')

        return stack[0] == 't'
