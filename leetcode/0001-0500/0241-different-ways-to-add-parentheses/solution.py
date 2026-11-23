from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @lru_cache(None)
        def compute(expr: str) -> list[int]:
            res = []
            
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Split into left and right subexpressions
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i + 1:])
                    
                    # Combine all pairs of results
                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            # Base case: expr is just a single number
            if not res:
                res.append(int(expr))
                
            return res

        return compute(expression)
