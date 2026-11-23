# LeetCode 65: Valid Number

**LeetCode Problem #65 — Valid Number**
Solve LeetCode Valid Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Number |
| LeetCode | #65 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return whether `s` is a **valid number**. 
 
For example, all the following are valid numbers: `"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"`, while the following are not valid numbers: `"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"`.

Formally, a **valid number** is defined using one of the following definitions:

An **integer number** followed by an **optional exponent**. 
 A **decimal number** followed by an **optional exponent**.

An **integer number** is defined with an **optional sign** `'-'` or `'+'` followed by **digits**.

A **decimal number** is defined with an **optional sign** `'-'` or `'+'` followed by one of the following definitions:

**Digits** followed by a **dot** `'.'`. 
 **Digits** followed by a **dot** `'.'` followed by **digits**. 
 A **dot** `'.'` followed by **digits**.

An **exponent** is defined with an **exponent notation** `'e'` or `'E'` followed by an **integer number**.

The **digits** are defined as one or more digits.

## Constraints
- `1 <= s.length <= 20`
- `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+'`, minus `'-'`, or dot `'.'`.

## Examples
### Example 1
- **Input:** `s = "0"`
- **Output:** `true`

### Example 2
- **Input:** `s = "e"`
- **Output:** `false`

### Example 3
- **Input:** `s = "."`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Valid Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

            elif ch in '+-':
                # Sign is allowed only at the beginning
                # or immediately after e/E
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif ch == '.':
                # Dot is not allowed after an exponent
                # and only one dot is allowed
                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            elif ch in 'eE':
                # Only one exponent is allowed
                # and exponent must have a digit before it
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                seen_digit = False

            else:
                return False

        return seen_digit
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
- [611. Valid Triangle Number](../../0501-1000/0611-valid-triangle-number/)
- [1178. Number of Valid Words for Each Puzzle](../../1001-1500/1282-number-of-valid-words-for-each-puzzle/)
- [2047. Number of Valid Words in a Sentence](../../2001-2500/2173-number-of-valid-words-in-a-sentence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-number/)
