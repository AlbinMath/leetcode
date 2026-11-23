# LeetCode 4059: Lexicographically Largest Power Array

**LeetCode Problem #4059 — Lexicographically Largest Power Array**
Solve LeetCode Lexicographically Largest Power Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Largest Power Array |
| LeetCode | #4059 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  of length  n . You may rearrange its elements to form any  permutation   perm .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Lexicographically Largest Power Array**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1718. Construct the Lexicographically Largest Valid Sequence](../../1501-2000/1819-construct-the-lexicographically-largest-valid-sequence/)
- [2948. Make Lexicographically Smallest Array by Swapping Elements](../../3001-3500/3219-make-lexicographically-smallest-array-by-swapping-elements/)
- [3403. Find the Lexicographically Largest String From the Box I](../../3501-4000/3683-find-the-lexicographically-largest-string-from-the-box-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-largest-power-array/)
