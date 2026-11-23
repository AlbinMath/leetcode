# LeetCode 1529: Minimum Suffix Flips

**LeetCode Problem #1529 — Minimum Suffix Flips**
Solve LeetCode Minimum Suffix Flips using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Suffix Flips |
| LeetCode | #1529 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** binary string `target` of length `n`. You have another binary string `s` of length `n` that is initially set to all zeros. You want to make `s` equal to `target`.

In one operation, you can pick an index `i` where `0 <= i < n` and flip all bits in the **inclusive** range `[i, n - 1]`. Flip means changing `'0'` to `'1'` and `'1'` to `'0'`.

Return *the minimum number of operations needed to make *`s`* equal to *`target`.

## Constraints
- `n == target.length`
- `1 <= n <= 10^5`
- `target[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `target = "10111"`
- **Output:** `3`
- **Explanation:** Initially, s = "00000".
Choose index i = 2: "00 000 " -> "00 111 "
Choose index i = 0: " 00111 " -> " 11000 "
Choose index i = 1: "1 1000 " -> "1 0111 "
We need at least 3 flip operations to form target.

### Example 2
- **Input:** `target = "101"`
- **Output:** `3`
- **Explanation:** Initially, s = "000".
Choose index i = 0: " 000 " -> " 111 "
Choose index i = 1: "1 11 " -> "1 00 "
Choose index i = 2: "10 0 " -> "10 1 "
We need at least 3 flip operations to form target.

### Example 3
- **Input:** `target = "00000"`
- **Output:** `0`
- **Explanation:** We do not need any operations since the initial s already equals target.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Suffix Flips**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = "10111"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Initially, s = "00000".
Choose index i = 2: "00 000 " -> "00 111 "
Choose index i = 0: " 00111 " -> " 11000 "
Choose index i = 1: "1 1000 " -> "1 0111 "
We need at least 3 flip operations to form target.

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
    def minFlips(self, target: str) -> int:
        prev = '0'
        flips = 0

        for ch in target:
            if ch != prev:
                flips += 1
                prev = ch

        return flips
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
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1409-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1318. Minimum Flips to Make a OR b Equal to c](../../1001-1500/1441-minimum-flips-to-make-a-or-b-equal-to-c/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-suffix-flips/)
