# LeetCode 1252: Cells with Odd Values in a Matrix

**LeetCode Problem #1252 — Cells with Odd Values in a Matrix**
Solve LeetCode Cells with Odd Values in a Matrix using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cells with Odd Values in a Matrix |
| LeetCode | #1252 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  m x n  matrix that is initialized to all  0 &#39;s. There is also a 2D array  indices  where each  indices[i] = [r i , c i ]  represents a  0-indexed location  to perform some increment operations on the matrix.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Cells with Odd Values in a Matrix**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1030. Matrix Cells in Distance Order](../../1001-1500/1094-matrix-cells-in-distance-order/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../../2501-3000/2818-maximum-strictly-increasing-cells-in-a-matrix/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1228-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/)
