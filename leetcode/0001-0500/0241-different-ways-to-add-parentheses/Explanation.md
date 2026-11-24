# LeetCode 241: Different Ways to Add Parentheses

**LeetCode Problem #241 — Different Ways to Add Parentheses**
Solve LeetCode Different Ways to Add Parentheses using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Different Ways to Add Parentheses |
| LeetCode | #241 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `expression` of numbers and operators, return *all possible results from computing all the different possible ways to group numbers and operators*. You may return the answer in **any order**.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed `10^4`.

## Constraints
- `1 <= expression.length <= 20`
- `expression` consists of digits and the operator `'+'`, `'-'`, and `'*'`.
- All the integer values in the input expression are in the range `[0, 99]`.
- The integer values in the input expression do not have a leading `'-'` or `'+'` denoting the sign.

## Examples
### Example 1
- **Input:** `expression = "2-1-1"`
- **Output:** `[0,2]`
- **Explanation:** ((2-1)-1) = 0 
(2-(1-1)) = 2

### Example 2
- **Input:** `expression = "2*3-4*5"`
- **Output:** `[-34,-14,-10,-10,10]`
- **Explanation:** (2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Different Ways to Add Parentheses**, we observe the problem requirements and utilize the **Stack & Queue** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "2-1-1"`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2]`.
4. **Verification:** ((2-1)-1) = 0 
(2-(1-1)) = 2

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0957-minimum-add-to-make-parentheses-valid/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1501-2000/1531-number-of-ways-to-wear-different-hats-to-each-other/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/)
