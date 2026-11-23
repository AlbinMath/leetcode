# LeetCode 640: Solve the Equation

**LeetCode Problem #640 — Solve the Equation**
Solve LeetCode Solve the Equation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Solve the Equation |
| LeetCode | #640 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Solve a given equation and return the value of `'x'` in the form of a string `"x=#value"`. The equation contains only `'+'`, `'-'` operation, the variable `'x'` and its coefficient. You should return `"No solution"` if there is no solution for the equation, or `"Infinite solutions"` if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of `'x'` is an integer.

## Constraints
- `3 <= equation.length <= 1000`
- `equation` has exactly one `'='`.
- `equation` consists of integers with an absolute value in the range `[0, 100]` without any leading zeros, and the variable `'x'`.
- The input is generated that if there is a single solution, it will be an integer.

## Examples
### Example 1
- **Input:** `equation = "x+5-3+x=6+x-2"`
- **Output:** `"x=2"`

### Example 2
- **Input:** `equation = "x=x"`
- **Output:** `"Infinite solutions"`

### Example 3
- **Input:** `equation = "2x=x"`
- **Output:** `"x=0"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Solve the Equation**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `equation = "x+5-3+x=6+x-2"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"x=2"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1237. Find Positive Integer Solution for a Given Equation](../../1001-1500/1358-find-positive-integer-solution-for-a-given-equation/)
- [1499. Max Value of Equation](../../1501-2000/1622-max-value-of-equation/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/solve-the-equation/)
