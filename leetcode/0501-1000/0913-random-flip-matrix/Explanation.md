# LeetCode 519: Random Flip Matrix

**LeetCode Problem #519 — Random Flip Matrix**
Solve LeetCode Random Flip Matrix using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Random Flip Matrix |
| LeetCode | #519 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  m x n  binary grid  matrix  with all the values set  0  initially. Design an algorithm to randomly pick an index  (i, j)  where  matrix[i][j] == 0  and flips it to  1 . All the indices  (i, j)  where  matrix[i][j] == 0  should be equally likely to be returned.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Random Flip Matrix**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [2556. Disconnect Path in a Binary Matrix by at Most One Flip](../../2501-3000/2641-disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
- [926. Flip String to Monotone Increasing](../../0501-1000/0962-flip-string-to-monotone-increasing/)
- [951. Flip Equivalent Binary Trees](../../0501-1000/0988-flip-equivalent-binary-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-flip-matrix/)
