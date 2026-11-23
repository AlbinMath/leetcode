# LeetCode 1787: Make the XOR of All Segments Equal to Zero

**LeetCode Problem #1787 — Make the XOR of All Segments Equal to Zero**
Solve LeetCode Make the XOR of All Segments Equal to Zero using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make the XOR of All Segments Equal to Zero |
| LeetCode | #1787 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  nums ​​​ and an integer  k ​​​​​. The  XOR  of a segment  [left, right]  where  left <= right  is the  XOR  of all the elements with indices between  left  and  right , inclusive:  nums[left] XOR nums[left+1] XOR ... XOR nums[right] .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make the XOR of All Segments Equal to Zero**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../../1501-2000/1576-reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
- [2357. Make Array Zero by Subtracting Equal Amounts](../../2001-2500/2436-make-array-zero-by-subtracting-equal-amounts/)
- [3354. Make Array Elements Equal to Zero](../../3501-4000/3616-make-array-elements-equal-to-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/)
