# LeetCode 461: Hamming Distance

**LeetCode Problem #461 — Hamming Distance**
Solve LeetCode Hamming Distance using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Hamming Distance |
| LeetCode | #461 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return *the **Hamming distance** between them*.

## Constraints
- `0 <= x, y <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `x = 1, y = 4`
- **Output:** `2`
- **Explanation:** 1 (0 0 0 1)
4 (0 1 0 0)
 &uarr; &uarr;
The above arrows point to positions where the corresponding bits are different.

### Example 2
- **Input:** `x = 3, y = 1`
- **Output:** `1`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Hamming Distance**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = 1, y = 4`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 1 (0 0 0 1)
4 (0 1 0 0)
 &uarr; &uarr;
The above arrows point to positions where the corresponding bits are different.

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
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0

        while xor:
            count += xor & 1
            xor >>= 1

        return count
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
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)
- [1722. Minimize Hamming Distance After Swap Operations](../../1501-2000/1722-minimize-hamming-distance-after-swap-operations/)
- [72. Edit Distance](../../0001-0500/0072-edit-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/hamming-distance/)
