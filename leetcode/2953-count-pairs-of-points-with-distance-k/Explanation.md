# LeetCode 2857: Count Pairs of Points With Distance k

**LeetCode Problem #2857 — Count Pairs of Points With Distance k**
Solve LeetCode Count Pairs of Points With Distance k using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs of Points With Distance k |
| LeetCode | #2857 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  2D  integer array  coordinates  and an integer  k , where  coordinates[i] = [x i , y i ]  are the coordinates of the  i th   point in a 2D plane.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Pairs of Points With Distance k**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2183. Count Array Pairs Divisible by K](../2301-count-array-pairs-divisible-by-k/)
- [4043. Count Rotations With Exactly K Equal Adjacent Pairs](../4411-count-rotations-with-exactly-k-equal-adjacent-pairs/)
- [1617. Count Subtrees With Max Distance Between Cities](../1740-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/)
