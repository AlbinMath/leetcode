# LeetCode 2049: Count Nodes With the Highest Score

**LeetCode Problem #2049 — Count Nodes With the Highest Score**
Solve LeetCode Count Nodes With the Highest Score using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Nodes With the Highest Score |
| LeetCode | #2049 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a  binary  tree rooted at  0  consisting of  n  nodes. The nodes are labeled from  0  to  n - 1 . You are given a  0-indexed  integer array  parents  representing the tree, where  parents[i]  is the parent of node  i . Since node  0  is the root,  parents[0] == -1 .

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Nodes With the Highest Score**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [222. Count Complete Tree Nodes](../0222-count-complete-tree-nodes/)
- [1448. Count Good Nodes in Binary Tree](../1544-count-good-nodes-in-binary-tree/)
- [1782. Count Pairs Of Nodes](../1891-count-pairs-of-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-nodes-with-the-highest-score/)
