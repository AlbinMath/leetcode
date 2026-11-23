# LeetCode 1447: Simplified Fractions

**LeetCode Problem #1447 — Simplified Fractions**
Solve LeetCode Simplified Fractions using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Simplified Fractions |
| LeetCode | #1447 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *a list of all **simplified** fractions between *`0`* and *`1`* (exclusive) such that the denominator is less-than-or-equal-to *`n`. You can return the answer in **any order**.

## Constraints
- `1 <= n <= 100`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `["1/2"]`
- **Explanation:** "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

### Example 2
- **Input:** `n = 3`
- **Output:** `["1/2","1/3","2/3"]`

### Example 3
- **Input:** `n = 4`
- **Output:** `["1/2","1/3","1/4","2/3","3/4"]`
- **Explanation:** "2/4" is not a simplified fraction because it can be simplified to "1/2".

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Simplified Fractions**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["1/2"]`.
4. **Verification:** "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import gcd

class Solution(object):
    def simplifiedFractions(self, n):
        result = []

        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    result.append(str(numerator) + "/" + str(denominator))

        return result
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [48. Rotate Image](../../0001-0500/0048-rotate-image/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)
- [118. Pascal's Triangle](../../0001-0500/0118-pascals-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/simplified-fractions/)
