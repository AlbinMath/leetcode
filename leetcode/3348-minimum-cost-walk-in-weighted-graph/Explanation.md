# LeetCode 3108: Minimum Cost Walk in Weighted Graph

**LeetCode Problem #3108 — Minimum Cost Walk in Weighted Graph**
Solve LeetCode Minimum Cost Walk in Weighted Graph using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Walk in Weighted Graph |
| LeetCode | #3108 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an undirected weighted graph with  n  vertices labeled from  0  to  n - 1 .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost Walk in Weighted Graph**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2203. Minimum Weighted Subgraph With the Required Paths](../2321-minimum-weighted-subgraph-with-the-required-paths/)
- [3553. Minimum Weighted Subgraph With the Required Paths II](../3853-minimum-weighted-subgraph-with-the-required-paths-ii/)
- [1130. Minimum Cost Tree From Leaf Values](../1228-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/)
