# LeetCode 3097: Shortest Subarray With OR at Least K II

**LeetCode Problem #3097 — Shortest Subarray With OR at Least K II**
Solve LeetCode Shortest Subarray With OR at Least K II using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Subarray With OR at Least K II |
| LeetCode | #3097 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  nums  of  non-negative  integers and an integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Subarray With OR at Least K II**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [862. Shortest Subarray with Sum at Least K](../../0501-1000/0892-shortest-subarray-with-sum-at-least-k/)
- [3095. Shortest Subarray With OR at Least K I](../../3001-3500/3381-shortest-subarray-with-or-at-least-k-i/)
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../4001-4500/4152-minimum-subarray-length-with-distinct-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/)
