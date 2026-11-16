class Solution(object):
    def minimizeResult(self, expression):
        left, right = expression.split('+')
        best_val = float('inf')
        best_expr = ""

        for i in range(len(left)):
            a = int(left[:i]) if i > 0 else 1
            b = int(left[i:])

            for j in range(1, len(right) + 1):
                c = int(right[:j])
                d = int(right[j:]) if j < len(right) else 1

                val = a * (b + c) * d
                if val < best_val:
                    best_val = val
                    best_expr = left[:i] + "(" + left[i:] + "+" + right[:j] + ")" + right[j:]

        return best_expr
