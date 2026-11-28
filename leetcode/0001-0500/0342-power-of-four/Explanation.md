# LeetCode 342: Power of Four

**LeetCode Problem #342 — Power of Four**
Solve LeetCode Power of Four using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Power of Four |
| LeetCode | #342 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *`true` if it is a power of four. Otherwise, return `false`*.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4^x`.

## Constraints
- `-2^31 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 16`
- **Output:** `true`

### Example 2
- **Input:** `n = 5`
- **Output:** `false`

### Example 3
- **Input:** `n = 1`
- **Output:** `true`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Power of Four**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 16`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False

        # Power of 4 must have exactly one set bit
        if n & (n - 1):
            return False

        # The set bit must be in an even position
        return (n & 0x55555555) != 0
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
- [1390. Four Divisors](../../1001-1500/1390-four-divisors/)
- [2160. Minimum Sum of Four Digit Number After Splitting Digits](../../2001-2500/2160-minimum-sum-of-four-digit-number-after-splitting-digits/)
- [231. Power of Two](../../0001-0500/0231-power-of-two/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/power-of-four/)
