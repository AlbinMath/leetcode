# LeetCode 2242: Maximum Score of a Node Sequence

**LeetCode Problem #2242 — Maximum Score of a Node Sequence**
Solve LeetCode Maximum Score of a Node Sequence using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score of a Node Sequence |
| LeetCode | #2242 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  undirected  graph with  n  nodes, numbered from  0  to  n - 1 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Score of a Node Sequence**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1092-maximum-difference-between-node-and-ancestor/)
- [2374. Node With Highest Edge Score](../../2001-2500/2455-node-with-highest-edge-score/)
- [3068. Find the Maximum Sum of Node Values](../../3001-3500/3307-find-the-maximum-sum-of-node-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-of-a-node-sequence/)
