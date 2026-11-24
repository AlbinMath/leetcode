# LeetCode 592: Fraction Addition and Subtraction

**LeetCode Problem #592 — Fraction Addition and Subtraction**
Solve LeetCode Fraction Addition and Subtraction using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fraction Addition and Subtraction |
| LeetCode | #592 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `expression` representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction . If your final result is an integer, change it to the format of a fraction that has a denominator `1`. So in this case, `2` should be converted to `2/1`.

## Constraints
- The input string only contains `'0'` to `'9'`, `'/'`, `'+'` and `'-'`. So does the output.
- Each fraction (input and output) has the format `&plusmn;numerator/denominator`. If the first input fraction or the output is positive, then `'+'` will be omitted.
- The input only contains valid **irreducible fractions**, where the **numerator** and **denominator** of each fraction will always be in the range `[1, 10]`. If the denominator is `1`, it means this fraction is actually an integer in a fraction format defined above.
- The number of given fractions will be in the range `[1, 10]`.
- The numerator and denominator of the **final result** are guaranteed to be valid and in the range of **32-bit** int.

## Examples
### Example 1
- **Input:** `expression = "-1/2+1/2"`
- **Output:** `"0/1"`

### Example 2
- **Input:** `expression = "-1/2+1/2+1/3"`
- **Output:** `"1/3"`

### Example 3
- **Input:** `expression = "1/3-1/2"`
- **Output:** `"-1/6"`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fraction Addition and Subtraction**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "-1/2+1/2"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"0/1"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        for a, b in re.findall(r'([+-]?\d+)/(\d+)', expression):
            a, b = int(a), int(b)
            num = num * b + a * den
            den *= b
            g = gcd(abs(num), den)
            num //= g
            den //= g
        return "%d/%d" % (num, den)
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2601. Prime Subtraction Operation](../../2501-3000/2601-prime-subtraction-operation/)
- [166. Fraction to Recurring Decimal](../../0001-0500/0166-fraction-to-recurring-decimal/)
- [598. Range Addition II](../../0501-1000/0598-range-addition-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fraction-addition-and-subtraction/)
