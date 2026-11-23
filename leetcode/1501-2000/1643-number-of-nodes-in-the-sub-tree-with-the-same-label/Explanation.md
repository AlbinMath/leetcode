# LeetCode 1519: Number of Nodes in the Sub-Tree With the Same Label

**LeetCode Problem #1519 — Number of Nodes in the Sub-Tree With the Same Label**
Solve LeetCode Number of Nodes in the Sub-Tree With the Same Label using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Nodes in the Sub-Tree With the Same Label |
| LeetCode | #1519 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of  n  nodes numbered from  0  to  n - 1  and exactly  n - 1   edges . The  root  of the tree is the node  0 , and each node of the tree has  a label  which is a lower-case character given in the string  labels  (i.e. The node with the number  i  has the label  labels[i] ).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Nodes in the Sub-Tree With the Same Label**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [1524. Number of Sub-arrays With Odd Sum](../../1501-2000/1631-number-of-sub-arrays-with-odd-sum/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)
