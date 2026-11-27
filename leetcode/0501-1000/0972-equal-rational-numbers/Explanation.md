# LeetCode 972: Equal Rational Numbers

**LeetCode Problem #972 — Equal Rational Numbers**
Solve LeetCode Equal Rational Numbers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Equal Rational Numbers |
| LeetCode | #972 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `t`, each of which represents a non-negative rational number, return `true` if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

A **rational number** can be represented using up to three parts: `<IntegerPart>`, `<NonRepeatingPart>`, and a `<RepeatingPart>`. The number will be represented in one of the following three ways:

`<IntegerPart>`

For example, `12`, `0`, and `123`. 
 
 
 `<IntegerPart>**<.>**<NonRepeatingPart>`
 
 For example, `0.5`, `1.`, `2.12`, and `123.0001`. 
 
 
 `<IntegerPart>**<.>**<NonRepeatingPart>**<(>**<RepeatingPart>**<)>**`
 
 For example, `0.1(6)`, `1.(9)`, `123.00(1212)`.

The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets. For example:

`1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)`.

## Constraints
- Each part consists only of digits.
- The `<IntegerPart>` does not have leading zeros (except for the zero itself).
- `1 <= <IntegerPart>.length <= 4`
- `0 <= <NonRepeatingPart>.length <= 4`
- `1 <= <RepeatingPart>.length <= 4`

## Examples
### Example 1
- **Input:** `s = "0.(52)", t = "0.5(25)"`
- **Output:** `true`
- **Explanation:** Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.

### Example 2
- **Input:** `s = "0.1666(6)", t = "0.166(66)"`
- **Output:** `true`

### Example 3
- **Input:** `s = "0.9(9)", t = "1."`
- **Output:** `true`
- **Explanation:** "0.9(9)" represents 0.999999999... repeated forever, which equals 1. [ See this link for an explanation. ]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Equal Rational Numbers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0.(52)", t = "0.5(25)"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.

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
- [1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](../../1501-2000/1577-number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/equal-rational-numbers/)
