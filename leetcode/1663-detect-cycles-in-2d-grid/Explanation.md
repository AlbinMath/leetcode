# LeetCode 1559: Detect Cycles in 2D Grid

**LeetCode Problem #1559 — Detect Cycles in 2D Grid**
Solve LeetCode Detect Cycles in 2D Grid using Python and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Detect Cycles in 2D Grid |
| LeetCode | #1559 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a 2D array of characters  grid  of size  m x n , you need to find if there exists any cycle consisting of the  same value  in  grid .

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Floyd Cycle Detection**. By maintaining state efficiently in a **Linked List / Pointer**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Detect Cycles in 2D Grid**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1260. Shift 2D Grid](../1386-shift-2d-grid/)
- [3311. Construct 2D Grid Matching Graph Layout](../3578-construct-2d-grid-matching-graph-layout/)
- [74. Search a 2D Matrix](../0074-search-a-2d-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/)
