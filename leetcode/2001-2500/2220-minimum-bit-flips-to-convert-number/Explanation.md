# LeetCode 2220: Minimum Bit Flips to Convert Number

**LeetCode Problem #2220 — Minimum Bit Flips to Convert Number**
Solve LeetCode Minimum Bit Flips to Convert Number using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Bit Flips to Convert Number |
| LeetCode | #2220 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **bit flip** of a number `x` is choosing a bit in the binary representation of `x` and **flipping** it from either `0` to `1` or `1` to `0`.

For example, for `x = 7`, the binary representation is `111` and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get `110`, flip the second bit from the right to get `101`, flip the fifth bit from the right (a leading zero) to get `10111`, etc.

Given two integers `start` and `goal`, return* the **minimum** number of **bit flips** to convert *`start`* to *`goal`.

## Constraints
- `0 <= start, goal <= 10^9`

## Examples
### Example 1
- **Input:** `start = 10, goal = 7`
- **Output:** `3`
- **Explanation:** The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 101 0 -> 101 1 .
- Flip the third bit from the right: 1 0 11 -> 1 1 11.
- Flip the fourth bit from the right: 1 111 -> 0 111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

### Example 2
- **Input:** `start = 3, goal = 4`
- **Output:** `3`
- **Explanation:** The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 01 1 -> 01 0 .
- Flip the second bit from the right: 0 1 0 -> 0 0 0.
- Flip the third bit from the right: 0 00 -> 1 00.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Bit Flips to Convert Number**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `start = 10, goal = 7`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 101 0 -> 101 1 .
- Flip the third bit from the right: 1 0 11 -> 1 1 11.
- Flip the fourth bit from the right: 1 111 -> 0 111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.

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

  def minBitFlips(self, start: int, goal: int) -> int:
    return (start ^ goal).bit_count()
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
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)
