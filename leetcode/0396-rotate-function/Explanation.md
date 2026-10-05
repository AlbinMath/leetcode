# LeetCode 396: Rotate Function

**LeetCode Problem #396 — Rotate Function**
Solve LeetCode Rotate Function using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate Function |
| LeetCode | #396 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  of length  n .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a mathematical relationship between consecutive rotation functions to compute all values in $O(N)$ time.

1. **Compute F(0) and Sum:** It first calculates the sum of all elements (`sum`) and `F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]`.
2. **Recurrence Relation:** There is a mathematical relationship: `F(k) = F(k-1) + sum - n * nums[n-k]`. This is derived from the observation that when rotating, every element's weight increases by 1 (adding `sum`), except the element that wraps around from the end to position 0 (which loses `n` times its value).
3. It iterates from `k = 1` to `k = n-1`, computing each `F(k)` using the formula and tracking the maximum.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Rotate Function**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [48. Rotate Image](../0048-rotate-image/)
- [61. Rotate List](../0061-rotate-list/)
- [796. Rotate String](../0812-rotate-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-function/)
