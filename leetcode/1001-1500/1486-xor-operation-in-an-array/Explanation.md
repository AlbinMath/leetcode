# LeetCode 1486: XOR Operation in an Array

**LeetCode Problem #1486 — XOR Operation in an Array**
Solve LeetCode XOR Operation in an Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | XOR Operation in an Array |
| LeetCode | #1486 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an integer `start`.

Define an array `nums` where `nums[i] = start + 2 * i` (**0-indexed**) and `n == nums.length`.

Return *the bitwise XOR of all elements of* `nums`.

## Constraints
- `1 <= n <= 1000`
- `0 <= start <= 1000`
- `n == nums.length`

## Examples
### Example 1
- **Input:** `n = 5, start = 0`
- **Output:** `8`
- **Explanation:** Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

### Example 2
- **Input:** `n = 4, start = 3`
- **Output:** `8`
- **Explanation:** Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **XOR Operation in an Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, start = 0`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

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
    def xorOperation(self, n: int, start: int) -> int:
        result = 0

        for i in range(n):
            result ^= start + 2 * i

        return result
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1707-maximum-xor-with-an-element-from-array/)
- [2433. Find The Original Array of Prefix Xor](../../2001-2500/2433-find-the-original-array-of-prefix-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/xor-operation-in-an-array/)
