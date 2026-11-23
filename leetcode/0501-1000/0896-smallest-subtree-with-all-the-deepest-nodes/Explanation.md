# LeetCode 865: Smallest Subtree with all the Deepest Nodes

**LeetCode Problem #865 — Smallest Subtree with all the Deepest Nodes**
Solve LeetCode Smallest Subtree with all the Deepest Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Subtree with all the Deepest Nodes |
| LeetCode | #865 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  root  of a binary tree, the depth of each node is  the shortest distance to the root .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Subtree with all the Deepest Nodes**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0877-shortest-path-visiting-all-nodes/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0893-all-nodes-distance-k-in-binary-tree/)
- [1557. Minimum Number of Vertices to Reach All Nodes](../../1501-2000/1661-minimum-number-of-vertices-to-reach-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)
